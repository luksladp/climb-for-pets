import bpy, bmesh, numpy as np, math, random
from mathutils import Vector, Matrix

MATS = {}  # r13: pedra em grafite neutro (sem lilás), como o Lava Titan da rodada 13
HS = 1.6  # escala da cabeça (v10)
def head_x(p):
    return tuple(a + (b - a) * HS + o for a, b, o in zip((2.6, 0, 4.9), p, (0.3, 0, 0.18)))
def mat(name, col, rough=0.5, metal=0.0, emit=None, estr=0.0):
    if name in MATS: return MATS[name]
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    c = tuple(int(col[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c)
    b.inputs['Base Color'].default_value = (*lin, 1)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    if emit:
        e = tuple(int(emit[i:i + 2], 16) / 255 for i in (0, 2, 4))
        e = tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in e)
        b.inputs['Emission Color'].default_value = (*e, 1)
        b.inputs['Emission Strength'].default_value = estr
    MATS[name] = m
    return m

def materials():
    return dict(
        obsidian=mat('obsidian', '3A3A3F', 0.88),
        obsidian_edge=mat('obsidian_edge', '56565C', 0.85),
        obsidian_dark=mat('obsidian_dark', '1F1F23', 0.9),
        basalt=mat('basalt', '2D2C30', 0.8),
        magma=mat('magma', 'FF7A1A', 0.5, emit='FF5A0E', estr=2.4),
        lava=mat('lava', 'FF6E28', 0.85, emit='FF4A10', estr=1.0),
        lava_dark=mat('lava_dark', 'A84014', 0.85, emit='F05010', estr=0.9),
        lava_vein=mat('lava_vein', 'FF7A1A', 0.8, emit='FF5A0E', estr=2.4),
        gold=mat('gold', 'C08A1C', 0.55, 0.75),
        gold_edge=mat('gold_edge', 'D49A2A', 0.5, 0.75),
        eye=mat('eye', 'FFD030', 1.0, emit='FFC020', estr=4.6),
        eye_core=mat('eye_core', 'FFEC88', 1.0, emit='FFE070', estr=3.2),
        pupil=mat('pupil', '0E080A', 0.95),
        tooth=mat('tooth', 'E8DCC4', 0.45),
        skin=mat('skin', '5A3A30', 0.75),
        wing_dark=mat('wing_dark', '2E2E33', 0.85),
        wing_dark2=mat('wing_dark2', '252529', 0.85),
        eye_halo=mat('eye_halo', 'FF6A14', 0.5, emit='FF6010', estr=2.5),
        eye_rim=mat('eye_rim', '140E12', 0.6),
        glint=mat('glint', 'FFFFFF', 0.2, emit='FFFFFF', estr=6.0),
        mouth_in=mat('mouth_in', '4A1A10', 0.8, emit='D8460C', estr=0.35),  # r15: interior escuro na frente, garganta acesa no fundo
        tongue=mat('tongue', '8A2C12', 0.7, emit='E04A10', estr=0.6),
        magma_body=mat('magma_body', 'E8681A', 0.6, emit='FF5A0E', estr=1.5),
        lava_wing=mat('lava_wing', '6A2A10', 0.85, emit='B03808', estr=0.32),
        magma_head=mat('magma_head', 'B8501A', 0.7, emit='FF5A0E', estr=0.55),
        jewel=mat('jewel', 'FF5A6A', 0.15, emit='FF6A50', estr=5.0),
    )

class MB:
    """mesh builder: verts + faces with material names, flat or smooth"""
    def __init__(self): self.v = []; self.f = []; self.m = []
    def add_v(self, p): self.v.append(tuple(p)); return len(self.v) - 1
    def face(self, idx, mname): self.f.append(list(idx)); self.m.append(mname)
    def extend(self, other):
        o = len(self.v); self.v += other.v
        self.f += [[i + o for i in f] for f in other.f]; self.m += other.m

def to_object(mb, name, mats, smooth=False, coll=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata(mb.v, [], mb.f)
    names = sorted(set(mb.m))
    for n in names: me.materials.append(mats[n])
    idx = {n: i for i, n in enumerate(names)}
    me.polygons.foreach_set('material_index', [idx[n] for n in mb.m])
    me.polygons.foreach_set('use_smooth', [smooth] * len(mb.f))
    me.update()
    ob = bpy.data.objects.new(name, me)
    (coll or bpy.context.scene.collection).objects.link(ob)
    return ob

def basis(n):
    n = Vector(n).normalized()
    a = Vector((0, 0, 1)) if abs(n.z) < 0.9 else Vector((1, 0, 0))
    t = n.cross(a).normalized(); b = n.cross(t)
    return t, b, n

def prism_chain(mb, pts, radii, sides, mname, cap_mat=None, twist=0.0, jitter=0.0, rng=None, end_point=True):
    """faceted tube along pts (list of Vector) with per-point radii; tip closes to a point if end radius ~0"""
    rings = []
    prev_t = None
    for i, p in enumerate(pts):
        d = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        if prev_t is None:
            t, b, _ = basis(d)
        else:
            t = (prev_t - d * prev_t.dot(d)).normalized(); b = d.cross(t)
        prev_t = t
        r = radii[i]; ring = []
        for k in range(sides):
            a = 2 * math.pi * k / sides + twist * i
            jj = 1 + (rng.uniform(-jitter, jitter) if rng else 0)
            ring.append(mb.add_v(p + (t * math.cos(a) + b * math.sin(a)) * r * jj))
        rings.append(ring)
    for i in range(len(rings) - 1):
        for k in range(sides):
            k2 = (k + 1) % sides
            mb.face([rings[i][k], rings[i][k2], rings[i + 1][k2], rings[i + 1][k]], mname)
    mb.face(list(reversed(rings[0])), cap_mat or mname)
    mb.face(rings[-1], cap_mat or mname)
    return rings
