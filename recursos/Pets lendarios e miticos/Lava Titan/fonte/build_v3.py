# Lava Titan v3 — procedural build in Blender (bpy). Units = studs, Z up, front = +Y.
# Base: build_v2_origem.py (lava-titan-v2). v3 = régua Steal An Egg: corpo mais largo, punhos maiores,
# rede de fendas de magma larga e contínua, rocha fosca mais clara, olhos e estrela maiores, 3 malhas
# (Rock, Crystal, Magma) com 1 material e 1 textura de paleta cada, rig e 4 clipes.
import bpy, bmesh, math, random, os, sys
import numpy as np
from mathutils import Vector, Matrix, Quaternion
from mathutils.bvhtree import BVHTree

OUT = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else '/tmp/lt'
os.makedirs(OUT, exist_ok=True)
rng = random.Random(7)
bpy.ops.wm.read_factory_settings(use_empty=True)

def hexc(h, a=1.0):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    lin = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return (*lin, a)

# ---------------------------------------------------------------- materials
def mat(name, col, rough=0.6, emit=None, strength=0.0, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = hexc(col)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    if emit:
        b.inputs['Emission Color'].default_value = hexc(emit)
        b.inputs['Emission Strength'].default_value = strength
    return m

M_STONE_L = mat('stone_light', '9C9490', 0.92)
M_STONE_M = mat('stone_mid', '6B605B', 0.94)
M_STONE_D = mat('stone_dark', '3A3233', 0.96)
M_OBS = mat('obsidian', '17131C', 0.55)
M_OBS_HI = mat('obsidian_highlight', '4A3A5A', 0.45)
M_GLOW = mat('glow_magma', 'FF6A18', 0.5, 'FF5A14', 6.0)
M_GLOW_HOT = mat('glow_hot', 'FFC040', 0.5, 'FFB830', 9.0)

# magma core: tileable voronoi crack texture (color + emissive)
def crack_texture(size=1024, cells=11, seed=3):
    r = np.random.default_rng(seed)
    pts = (np.arange(cells)[:, None, None] * 0 + 0)  # placeholder
    gx, gy = np.meshgrid(np.arange(cells), np.arange(cells), indexing='ij')
    jit = r.random((cells, cells, 2)) * 0.8 + 0.1
    P = (np.stack([gx, gy], -1) + jit) / cells  # in [0,1)
    P = P.reshape(-1, 2)
    allp = np.concatenate([P + np.array([dx, dy]) for dx in (-1, 0, 1) for dy in (-1, 0, 1)])
    u = (np.arange(size) + 0.5) / size
    U, V = np.meshgrid(u, u, indexing='ij')
    F1 = np.full(U.shape, 9.0); F2 = np.full(U.shape, 9.0); ID = np.zeros(U.shape, int)
    for i, p in enumerate(allp):
        d = np.sqrt((U - p[0]) ** 2 + (V - p[1]) ** 2)
        m2 = d < F2
        newF2 = np.where(d < F1, F1, np.where(m2, d, F2))
        ID = np.where(d < F1, i % len(P), ID)
        F1 = np.minimum(F1, d); F2 = newF2
    edge = (F2 - F1) * size  # px distance to cell border (x2)
    cellshade = r.random(len(P))[ID]
    base = np.array(hexc('7A160C')[:3]) * (0.75 + 0.5 * cellshade[..., None])
    hot = np.array(hexc('FFD040')[:3]); mid = np.array(hexc('FF4A10')[:3])
    core = np.clip(1 - edge / 5.0, 0, 1)[..., None]
    rim = np.clip(1 - edge / 13.0, 0, 1)[..., None] ** 1.5
    col = base * (1 - rim) + mid * rim
    col = col * (1 - core) + hot * core
    emis = mid * rim * (1 - core) + hot * core + np.array(hexc('E0300A')[:3]) * 0.12 * (1 - rim)
    return col, emis

def np_to_image(name, arr):
    h, w, _ = arr.shape
    img = bpy.data.images.new(name, w, h, alpha=False, float_buffer=False)
    img.colorspace_settings.name = 'sRGB'
    srgb = np.where(arr <= 0.0031308, arr * 12.92, 1.055 * np.power(np.clip(arr, 0, None), 1 / 2.4) - 0.055)
    rgba = np.concatenate([np.clip(srgb, 0, 1), np.ones((h, w, 1))], -1)
    img.pixels.foreach_set(rgba.astype(np.float32).ravel())
    img.filepath_raw = os.path.join(OUT, name + '.png'); img.file_format = 'PNG'; img.save()
    img.pack()
    return img

col, emis = crack_texture(size=64)  # v3: não usada nas malhas (só a paleta)
IMG_C = np_to_image('LavaTitan_magma_color', col)
IMG_E = np_to_image('LavaTitan_magma_emissive', emis)
M_CORE = bpy.data.materials.new('magma_core'); M_CORE.use_nodes = True
nt = M_CORE.node_tree; b = nt.nodes['Principled BSDF']
tc = nt.nodes.new('ShaderNodeTexImage'); tc.image = IMG_C
te = nt.nodes.new('ShaderNodeTexImage'); te.image = IMG_E
nt.links.new(tc.outputs['Color'], b.inputs['Base Color'])
nt.links.new(te.outputs['Color'], b.inputs['Emission Color'])
b.inputs['Emission Strength'].default_value = 5.0
b.inputs['Roughness'].default_value = 0.7

M_GOLD = mat('gold', 'B08A45', 0.85, metal=0.2)
M_EYE_CORE = mat('eye_core', 'FFC860', 0.5)
M_MOUTH = mat('mouth_glow', 'A83C10', 0.9)
M_STONE_E = mat('stone_edge', '6A6180', 0.9)
# rodada 10: tons extras (focinho, presas, variação de tom das placas)
M_MUZZLE = mat('stone_muzzle', '7A7088', 0.9)
M_TOOTH = mat('stone_tooth', 'CFC6D6', 0.8)
M_MID_B = mat('stone_mid_b', '453E56', 0.94)
M_MID_C = mat('stone_mid_c', '302B3B', 0.95)
MATS = [M_CORE, M_STONE_L, M_STONE_M, M_STONE_D, M_OBS, M_OBS_HI, M_GLOW, M_GLOW_HOT, M_GOLD, M_EYE_CORE, M_STONE_E, M_MOUTH,
        M_MUZZLE, M_TOOTH, M_MID_B, M_MID_C]
MI = {m.name: i for i, m in enumerate(MATS)}

# ---------------------------------------------------------------- skeleton (joint positions)
J = {}
for s, side in ((1, 'R'), (-1, 'L')):   # facing +Y, character's right is +X
    J['shoulder.' + side] = Vector((s * 1.70, 0.45, 3.10))
    J['elbow.' + side] = Vector((s * 2.30, 0.75, 2.05))
    J['wrist.' + side] = Vector((s * 2.35, 1.20, 0.98))
    J['fist.' + side] = Vector((s * 2.32, 1.38, 0.60))
    J['hip.' + side] = Vector((s * 0.74, -0.45, 1.55))
    J['knee.' + side] = Vector((s * 0.92, -0.12, 0.88))
    J['ankle.' + side] = Vector((s * 0.94, -0.25, 0.32))
HEAD_C = Vector((0, 1.25, 3.88))

# ---------------------------------------------------------------- core (union of primitives -> voxel remesh)
core_bm = bmesh.new()
def add_ellipsoid(bm, c, r, rot=None):
    g = bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=16, radius=1.0)
    M = Matrix.Translation(c) @ (rot.to_matrix().to_4x4() if rot else Matrix()) @ Matrix.Diagonal((*r, 1))
    bmesh.ops.transform(bm, matrix=M, verts=g['verts'])
def add_limb(bm, a, b_, ra, rb):
    d = b_ - a; L = d.length
    g = bmesh.ops.create_cone(bm, cap_ends=True, segments=20, radius1=ra, radius2=rb, depth=L)
    q = Vector((0, 0, 1)).rotation_difference(d.normalized())
    M = Matrix.Translation((a + b_) / 2) @ q.to_matrix().to_4x4()
    bmesh.ops.transform(bm, matrix=M, verts=g['verts'])
    add_ellipsoid(bm, a, (ra, ra, ra)); add_ellipsoid(bm, b_, (rb, rb, rb))

add_ellipsoid(core_bm, Vector((0, 0.18, 3.08)), (1.40, 0.82, 0.70))   # ombros projetados à frente (tronco inclinado)   # shoulder yoke
add_ellipsoid(core_bm, Vector((0, -0.35, 3.0)), (1.10, 0.66, 0.66))
add_ellipsoid(core_bm, Vector((0, 0.85, 3.55)), (0.62, 0.62, 0.50))   # cabeça fundida no tronco   # pescoço largo: cabeça integrada ao tronco   # pescoço curto: cabeça acima dos ombros   # back hump
add_ellipsoid(core_bm, Vector((0, 0.62, 2.72)), (0.90, 0.58, 0.72))   # chest
add_ellipsoid(core_bm, Vector((0, 0.10, 2.25)), (0.70, 0.55, 0.58))   # belly
add_ellipsoid(core_bm, Vector((0, -0.40, 1.85)), (0.80, 0.50, 0.38))  # pelvis
add_ellipsoid(core_bm, HEAD_C, (0.70, 0.62, 0.58))                    # head core
for side in 'RL':
    s = 1 if side == 'R' else -1
    add_ellipsoid(core_bm, J['shoulder.' + side] + Vector((0, -0.05, 0.05)), (0.60, 0.60, 0.56))
    add_limb(core_bm, J['shoulder.' + side], J['elbow.' + side], 0.40, 0.38)
    add_limb(core_bm, J['elbow.' + side], J['wrist.' + side], 0.50, 0.56)
    add_ellipsoid(core_bm, J['elbow.' + side].lerp(J['wrist.' + side], 0.55), (0.68, 0.66, 0.70))
    add_ellipsoid(core_bm, J['fist.' + side], (0.76, 0.74, 0.56))
    add_limb(core_bm, J['hip.' + side], J['knee.' + side], 0.44, 0.42)
    add_limb(core_bm, J['knee.' + side], J['ankle.' + side], 0.42, 0.40)
    add_ellipsoid(core_bm, Vector((s * 0.96, -0.08, 0.20)), (0.46, 0.60, 0.22))

me = bpy.data.meshes.new('core_tmp'); core_bm.to_mesh(me); core_bm.free()
core_tmp = bpy.data.objects.new('core_tmp', me); bpy.context.scene.collection.objects.link(core_tmp)
rm = core_tmp.modifiers.new('rm', 'REMESH'); rm.mode = 'VOXEL'; rm.voxel_size = 0.045
sm = core_tmp.modifiers.new('sm', 'SMOOTH'); sm.factor = 0.8; sm.iterations = 12
dc = core_tmp.modifiers.new('dc', 'DECIMATE'); dc.ratio = 0.10
dg = bpy.context.evaluated_depsgraph_get()
core_me = bpy.data.meshes.new_from_object(core_tmp.evaluated_get(dg))
bpy.data.objects.remove(core_tmp)
# clip to ground
for v in core_me.vertices:
    if v.co.z < 0.0: v.co.z = 0.0
print('core faces', len(core_me.polygons))

bm_core = bmesh.new(); bm_core.from_mesh(core_me)
bm_core.verts.ensure_lookup_table(); bm_core.faces.ensure_lookup_table()
bvh = BVHTree.FromBMesh(bm_core)

def surf(origin, direction):
    hit = bvh.ray_cast(Vector(origin), Vector(direction).normalized())
    return hit[0], hit[1]

# ---------------------------------------------------------------- piece builder
class Builder:
    def __init__(self):
        self.V = []; self.F = []; self.FM = []; self.VB = []; self.smooth = []
    def add_bm(self, bm, bone, matfn, smooth=False):
        base = len(self.V)
        for v in bm.verts: self.V.append(v.co.copy()); self.VB.append(bone)
        for f in bm.faces:
            self.F.append([base + v.index for v in f.verts])
            self.FM.append(matfn(f)); self.smooth.append(smooth)
BODY = Builder(); GLOW = Builder()

def rock_mat(axis):
    def fn(f):
        d = f.normal.dot(axis)
        if d > 0.55: return MI['stone_light']
        if f.normal.z > -0.25: return MI['stone_mid']
        return MI['stone_dark']
    return fn
def plate_mat(axis, top='stone_mid'):
    # rodada 4: chanfro com borda mais clara, topo médio, laterais escuras; rodada 10: topo em 3 tons
    def fn(f):
        d = f.normal.dot(axis)
        if d > 0.93: return MI[top]
        if d > 0.45: return MI['stone_edge']
        return MI['stone_dark']
    return fn
def column_mat(f):
    if f.normal.z > 0.6: return MI['stone_light']
    return MI['stone_light'] if f.normal.dot(Vector((-0.5, 0.7, 0.2)).normalized()) > 0.35 else (MI['stone_mid'] if f.normal.dot(Vector((-0.5, 0.7, 0.2)).normalized()) > -0.45 else MI['stone_dark'])
def const(name): return lambda f: MI[name]

def hull(points):
    bm = bmesh.new()
    for p in points: bm.verts.new(p)
    bmesh.ops.convex_hull(bm, input=bm.verts[:])
    for f in list(bm.faces): pass
    loose = [v for v in bm.verts if not v.link_faces]
    bmesh.ops.delete(bm, geom=loose, context='VERTS')
    bmesh.ops.dissolve_limit(bm, angle_limit=math.radians(4), verts=bm.verts[:], edges=bm.edges[:])
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4])
    bm.verts.index_update(); bm.normal_update()
    return bm

def frame(n):
    n = n.normalized(); t = Vector((0, 0, 1)).cross(n)
    if t.length < 1e-3: t = Vector((1, 0, 0))
    t.normalize(); b_ = n.cross(t)
    return Matrix((t, b_, n)).transposed()  # columns t,b,n

def plate(center, normal, r, h=None, k=None, tilt=0.12, sink=0.10):
    k = k or rng.randint(5, 7); h = h or r * rng.uniform(0.45, 0.65)
    angs = sorted(rng.uniform(0, 2 * math.pi) for _ in range(k))
    angs = [i * 2 * math.pi / k + rng.uniform(-0.35, 0.35) for i in range(k)]
    pts = []
    for a in angs:
        rr = r * rng.uniform(0.82, 1.05)
        pts.append(Vector((math.cos(a) * rr, math.sin(a) * rr, -sink)))
        pts.append(Vector((math.cos(a) * rr * 0.97, math.sin(a) * rr * 0.97, h * 0.35)))
        pts.append(Vector((math.cos(a + 0.2) * rr * 0.72, math.sin(a + 0.2) * rr * 0.72, h * 0.85)))
    pts.append(Vector((rng.uniform(-.15, .15) * r, rng.uniform(-.15, .15) * r, h)))
    bm = hull(pts)
    n = (normal + Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-1, 1))) * tilt).normalized()
    R = frame(n) @ Matrix.Rotation(rng.uniform(0, 6.28), 3, 'Z')
    M = Matrix.Translation(center) @ R.to_4x4()
    bmesh.ops.transform(bm, matrix=M, verts=bm.verts[:]); bm.normal_update()
    return bm, n

def hexprism(base, axis, r, L, top_jitter=0.06, seg=6, rot=0.0):
    bm = bmesh.new()
    g = bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r * 0.96, depth=L)
    bmesh.ops.translate(bm, vec=Vector((0, 0, L / 2)), verts=bm.verts[:])
    d = Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), 0)) * top_jitter / max(r, 1e-3)
    for v in bm.verts:
        if v.co.z > L * 0.9: v.co.z += d.x * v.co.x + d.y * v.co.y
    q = Vector((0, 0, 1)).rotation_difference(axis.normalized())
    M = Matrix.Translation(base) @ q.to_matrix().to_4x4() @ Matrix.Rotation(rot, 4, 'Z')
    bmesh.ops.transform(bm, matrix=M, verts=bm.verts[:]); bm.normal_update()
    return bm

def crystal(base, axis, r, L):
    pts = []
    for i in range(6):
        a = i * math.pi / 3 + 0.3
        pts.append(Vector((math.cos(a) * r, math.sin(a) * r, 0)))
        pts.append(Vector((math.cos(a + 0.25) * r * 0.80, math.sin(a + 0.25) * r * 0.80, L * 0.42)))
        pts.append(Vector((math.cos(a) * r * 0.42, math.sin(a) * r * 0.42, L * 0.80)))
    pts += [Vector((0, 0, L)), Vector((0, 0, -0.35))]
    bm = hull(pts)
    q = Vector((0, 0, 1)).rotation_difference(axis.normalized())
    bmesh.ops.transform(bm, matrix=Matrix.Translation(base) @ q.to_matrix().to_4x4(), verts=bm.verts[:])
    bm.normal_update()
    return bm
def obs_mat(f):
    return MI['obsidian_highlight'] if f.normal.dot(Vector((-0.45, 0.75, 0.45)).normalized()) > 0.62 else MI['obsidian']   # brilho nas facetas

def nearest_bone(p):
    best, bn = 1e9, 'chest'
    for name, (a, b_) in BONES.items():
        ab = b_ - a; t = max(0, min(1, (p - a).dot(ab) / ab.length_squared))
        d = (a + ab * t - p).length
        if d < best: best, bn = d, name
    return bn

# ---------------------------------------------------------------- bones
BONES = {
    'hips': (Vector((0, -0.4, 1.6)), Vector((0, -0.1, 2.25))),
    'spine': (Vector((0, -0.1, 2.25)), Vector((0, 0.1, 2.9))),
    'chest': (Vector((0, 0.1, 2.9)), Vector((0, 0.5, 3.5))),
    'head': (Vector((0, 0.80, 3.40)), Vector((0, 1.35, 4.25))),
}
for side in 'RL':
    BONES['upperarm.' + side] = (J['shoulder.' + side], J['elbow.' + side])
    BONES['forearm.' + side] = (J['elbow.' + side], J['wrist.' + side])
    BONES['hand.' + side] = (J['wrist.' + side], J['fist.' + side] + Vector((0, 0.45, -0.2)))
    BONES['thigh.' + side] = (J['hip.' + side], J['knee.' + side])
    BONES['shin.' + side] = (J['knee.' + side], J['ankle.' + side])
    BONES['foot.' + side] = (J['ankle.' + side], J['ankle.' + side] + Vector((0, 0.6, -0.15)))
PARENT = {'spine': 'hips', 'chest': 'spine', 'head': 'chest'}
for side in 'RL':
    PARENT.update({'upperarm.' + side: 'chest', 'forearm.' + side: 'upperarm.' + side, 'hand.' + side: 'forearm.' + side,
                   'thigh.' + side: 'hips', 'shin.' + side: 'thigh.' + side, 'foot.' + side: 'shin.' + side})

# ---------------------------------------------------------------- key positions
star_p, star_n = surf((0, 3, 2.52), (0, -1, 0.05))
crater_p, crater_n = surf((0, -3, 4.6), (0, 1, -0.75))
fall_p, fall_n = surf(J['elbow.L'].lerp(J['wrist.L'], 0.5) + Vector((-2, 0.2, 0)), (1, 0, 0))
print('star', star_p, 'crater', crater_p, 'fall', fall_p)
COL_C = {'R': Vector((1.30, -0.25, 3.45)), 'L': Vector((-1.30, -0.25, 3.45))}

def blocked(p):
    if (p - crater_p).length < 0.56: return True
    if (p - fall_p).length < 0.38: return True
    if (p - HEAD_C).length < 0.66 and p.y > HEAD_C.y - 0.25: return True
    for c in COL_C.values():
        if (Vector((p.x, p.y, 0)) - Vector((c.x, c.y, 0))).length < 0.34 and p.z > 3.2: return True
    return False

# ---------------------------------------------------------------- crust mosaic (power-diagram cells on the surface)
_mos_state = rng.getstate()   # rodada 14: o mosaico mudou; depois o gerador volta ao ponto de antes (colunas, cristais etc. iguais)
areas = np.array([f.calc_area() for f in bm_core.faces]); areas /= areas.sum()
nprng = np.random.default_rng(11)
cand = []
for fi in nprng.choice(len(areas), 60000, p=areas):
    f = bm_core.faces[int(fi)]
    vs = [v.co for v in f.verts]; w = nprng.dirichlet(np.ones(len(vs)))
    cand.append(sum((vv * float(wi) for vv, wi in zip(vs, w)), Vector()))
def cell_size(p, n):   # rodada 14: testado placas grandes no peito/antebraço e pequenas nas juntas; ficou mais bagunçado, voltou ao mosaico aprovado
    if p.z < 0.8: return 0.44
    if (p - HEAD_C).length < 0.85: return 0.38
    if p.z > 2.55 and (n.z > 0.2 or p.y < -0.15): return 0.62
    return 0.54
seeds = []; sp = np.zeros((0, 3)); sr = np.zeros(0)
for p in cand:
    if p.z < 0.05: continue
    _, n, _, _ = bvh.find_nearest(p)
    d = cell_size(p, n) * rng.uniform(0.9, 1.1)
    if len(sp):
        dist = np.linalg.norm(sp - np.array(p), axis=1)
        if np.any(dist < (sr + d) * 0.5): continue
    seeds.append((p, n, d)); sp = np.vstack([sp, np.array(p)]); sr = np.append(sr, d)
print('seeds', len(seeds))

def clip(poly, a, c):
    # keep points with dot(x,a) <= c
    out = []
    for i in range(len(poly)):
        P, Q = poly[i], poly[(i + 1) % len(poly)]
        fp, fq = P.dot(a) - c, Q.dot(a) - c
        if fp <= 0: out.append(P)
        if (fp < 0) != (fq < 0) and abs(fp - fq) > 1e-9:
            t = fp / (fp - fq); out.append(P.lerp(Q, t))
    return out
GAP = 0.03
nplates = nsplit = 0
rv = random.Random(41)   # rodada 10: gerador só para tom e fissuras, não mexe no layout das placas
for i, (p, n, d) in enumerate(seeds):
    if blocked(p) or p.z < 0.06: continue
    Fm = frame(n); Ft = Fm.transposed()
    poly = [Vector((math.cos(a) * d * 0.85, math.sin(a) * d * 0.85)) for a in np.linspace(0, 2 * math.pi, 9)[:-1] + 0.2]
    poly = [v * (1.3 / 0.85) for v in poly]
    dist = np.linalg.norm(sp - np.array(p), axis=1)
    for j in np.nonzero((dist < (d + sr) * 1.2) & (dist > 1e-6))[0]:
        q = Ft @ (Vector(sp[j]) - p)
        if abs(q.z) > 0.6 * q.length + 0.05: continue   # other side of a limb
        u = Vector((q.x, q.y)); L = u.length
        if L < 1e-5: continue
        rj = sr[j]
        c = (L * L + (d * d - rj * rj) * 0.25) / (2 * L) - GAP / 2
        poly = clip(poly, u / L, c)
        if len(poly) < 3: break
    if len(poly) < 3: continue
    area2 = sum(poly[k].x * poly[(k + 1) % len(poly)].y - poly[(k + 1) % len(poly)].x * poly[k].y for k in range(len(poly))) / 2
    if area2 < 0.012: continue
    cen = sum(poly, Vector((0, 0))) / len(poly)
    h = rng.uniform(0.13, 0.20) * (d / 0.46) ** 0.5
    pts = []
    for v in poly:
        pts.append(Vector((v.x, v.y, -0.14)))
        pts.append(Vector((v.x, v.y, h * 0.55 + rng.uniform(-0.02, 0.02))))
        w = v.lerp(cen, 0.20); pts.append(Vector((w.x, w.y, h * rng.uniform(0.85, 1.0))))
    off = Vector((rng.uniform(-.2, .2), rng.uniform(-.2, .2))) * d * 0.5
    pts.append(Vector((cen.x + off.x, cen.y + off.y, h * 1.12)))
    tilt = Matrix.Rotation(rng.uniform(-0.08, 0.08), 3, 'X') @ Matrix.Rotation(rng.uniform(-0.08, 0.08), 3, 'Y')
    # rodada 10: variação de tom por placa e fissura fina (escura) partindo parte das placas grandes
    top = rv.choices(['stone_mid', 'stone_mid_b', 'stone_mid_c'], weights=(5, 3, 2))[0]
    if d > 0.5 and area2 > 0.16 and rv.random() < 0.45:
        a = rv.uniform(0, math.pi); u = Vector((math.cos(a), math.sin(a), 0)); c0 = Vector((cen.x, cen.y, 0)).dot(u) + rv.uniform(-0.05, 0.05)
        for sg in (1, -1):
            part = []
            for v in pts:
                k = v.dot(u) - c0
                if sg * k < 0.022: v = v + u * (0.022 * sg - k)   # encosta no corte, deixando um vão de 0,044
                part.append(v)
            bm = hull([p + Fm @ (tilt @ v) for v in part])
            BODY.add_bm(bm, nearest_bone(p), plate_mat(n, top if sg > 0 else rv.choice(['stone_mid', 'stone_mid_b', 'stone_mid_c']))); bm.free()
        nsplit += 1; nplates += 1; continue
    bm = hull([p + Fm @ (tilt @ v) for v in pts])
    BODY.add_bm(bm, nearest_bone(p), plate_mat(n, top)); bm.free(); nplates += 1
print('plates', nplates, 'split', nsplit)
rng.setstate(_mos_state)
for _ in range(61474): rng.random()   # mesmo ponto do gerador que o mosaico antigo deixava

# fallen plate on left forearm (hangs loose, shows magma)
bm, _ = plate(fall_p + fall_n * 0.12 + Vector((0, 0, -0.18)), (fall_n + Vector((0, 0.3, -0.9))).normalized(), 0.3, tilt=0.0)
BODY.add_bm(bm, 'forearm.L', rock_mat(fall_n)); bm.free()

# rodada 7: a estrela do peito virou fissura comum (veias do peito no núcleo, sem símbolo nem filete)

# ---------------------------------------------------------------- head
# rodada 10: cabeça de gorila de pedra refeita (olhos e boca eram o ponto fraco). Maior, mais alta e à frente
# dos ombros: crânio em cúpula, sobrancelha contínua em V, olhos angulares acesos sob a sobrancelha, focinho
# claro saliente com narinas, boca em crescente com lava no fundo e duas presas de pedra subindo da mandíbula.
# A cabeça usa um gerador próprio (rh) e depois o gerador do corpo avança como antes, para o corpo não mudar.
def rockcloud(c, half, n=14, jitter=1.0):
    return [c + Vector((rng.uniform(-1, 1) * half[0], rng.uniform(-1, 1) * half[1], rng.uniform(-1, 1) * half[2])) for _ in range(n)]
_rng_state = rng.getstate()
rh = random.Random(23)
H = HEAD_C + Vector((0, 0.50, 0.60)); HS = 1.65   # rodada 17: mais alta e à frente (aparece de lado)   # rodada 12: cabeça 40% maior que na rodada 10, mais alta e à frente
def hp(x, y, z): return H + HS * Vector((x, y, z))
def ell(c, r, n=26, jit=0.10):
    pts = []
    for _ in range(n):
        u = Vector((rh.gauss(0, 1), rh.gauss(0, 1), rh.gauss(0, 1))).normalized() * (1 + rh.uniform(-jit, jit))
        pts.append(hp(*c) + HS * Vector((u.x * r[0], u.y * r[1], u.z * r[2])))
    return pts
def put(pts, matfn, glow=False):
    bm = hull(pts); (GLOW if glow else BODY).add_bm(bm, 'head', matfn); bm.free()
def head_rock(pts, axis=Vector((0, 1, 0.3))): put(pts, rock_mat(axis.normalized()))
def muzzle_mat(f):   # focinho: pedra mais clara que o resto da cabeça (centro de atenção, como o focinho do kong)
    d = f.normal.dot(Vector((0, 0.8, 0.6)).normalized())
    if d > 0.35: return MI['stone_muzzle']
    if f.normal.z > -0.3: return MI['stone_light']
    return MI['stone_mid']
# crânio em cúpula + nuca que desce para a corcunda
# rodada 15: crânio partido em 4 placas com fendas de lava finas, como o corpo (a cabeça não parece colada)
_cr = ell((0, -0.10, 0.30), (0.78, 0.62, 0.50), 56, 0.05); _cc = hp(0, -0.10, 0.30)
put(ell((0, -0.10, 0.30), (0.71, 0.56, 0.45), 30, 0.02), const('glow_magma'), glow=True)   # lava por baixo das placas
_U = [(Vector((1, 0.08, 0.10)).normalized(), 0.10 * HS), (Vector((0.05, 0.75, -0.55)).normalized(), 0.02 * HS)]
for s1 in (1, -1):
    for s2 in (1, -1):
        part = []
        for v in _cr:
            q = v - _cc
            for (u, c0), sg in zip(_U, (s1, s2)):
                k = q.dot(u) - c0
                if sg * k < 0.028 * HS: q = q + u * (0.028 * HS * sg - k)
            part.append(_cc + q)
        head_rock(part, Vector((0, 0.3, 1)))
head_rock(ell((0, -0.55, 0.05), (0.70, 0.45, 0.42), 24), Vector((0, -0.3, 1)))
for s in (1, -1):   # laterais e "orelhas" de pedra que fecham a cabeça e a ligam aos ombros
    head_rock(ell((s * 0.62, -0.05, 0.04), (0.20, 0.42, 0.38), 20), Vector((s, 0.2, 0.3)))   # rodada 16: mais para dentro (perfil contínuo)
    head_rock(ell((s * 0.60, 0.42, -0.12), (0.22, 0.20, 0.20), 16), Vector((s * 0.6, 0.8, 0.1)))   # maçã do rosto
# cavidade escura dos olhos (fundo do rosto, atrás dos olhos)
for s_ in (1, -1):   # rodada 13: órbita arredondada (de lado não aparece mais uma caixa)
    put(ell((s_ * 0.37, 0.40, 0.26), (0.34, 0.13, 0.20), 22, 0.03), const('stone_dark'))
# sobrancelha contínua em V: mais baixa no meio (bravo calmo), avança sobre os olhos e faz sombra
for s in (1, -1):
    ridge = [hp(s * x, y, z) for x, y, z in ((-0.04, 0.74, 0.27), (-0.04, 0.70, 0.43), (-0.04, 0.42, 0.45), (-0.04, 0.46, 0.25),
                                            (0.66, 0.58, 0.45), (0.66, 0.54, 0.63), (0.66, 0.30, 0.61), (0.66, 0.34, 0.41),
                                            (0.80, 0.48, 0.53), (0.80, 0.34, 0.53), (0.78, 0.44, 0.44))]   # rodada 13: ponta chanfrada
    put(ridge, rock_mat(Vector((s * 0.15, 0.6, 0.8)).normalized()))
# olhos: lâmina angular acesa, canto de dentro mais baixo, borda de cima paralela à sobrancelha;
# halo laranja fino em volta, íris FFB030 e núcleo FFE6A0 (o ponto mais claro do pet)
# rodada 13: olho em amêndoa arredondada e levemente abaulada (não é mais painel chapado): pálpebra de cima
# reta e inclinada (bravo calmo), borda de baixo redonda; brilho claro deslocado para cima e para fora
def eye_pts(sd, t0, t1, hu, hd, yf, yb, bulge=0.035):
    i0, o0 = Vector((0.10, 0.20)), Vector((0.64, 0.40))
    pts = []
    for k in range(9):
        t = t0 + (t1 - t0) * k / 8; w = math.sin(math.pi * (k / 8))
        c = i0.lerp(o0, t); x = c.x
        yy = 0.50 + 0.10 * (1 - x / 0.62) + bulge * w   # acompanha a curva do rosto e abaula no meio
        for z in (c.y + hu * w ** 0.6, c.y - hd * w ** 0.85):
            pts += [hp(sd * x, yy + yf, z), hp(sd * x, yy - yb, z)]
    return pts
for s in (1, -1):
    put(eye_pts(s, -0.06, 1.06, 0.075, 0.20, 0.000, 0.10), const('glow_magma'), glow=True)   # borda laranja
    put(eye_pts(s, 0.00, 1.00, 0.045, 0.165, 0.016, 0.08), const('glow_hot'), glow=True)     # íris
    put(eye_pts(s, 0.44, 0.82, 0.025, 0.065, 0.032, 0.03), const('eye_core'), glow=True)     # brilho
# focinho saliente de gorila, em pedra mais clara, com ponte do nariz e narinas escuras; desce até o lábio
put(ell((0, 0.70, -0.20), (0.58, 0.40, 0.29), 30, 0.05), muzzle_mat)   # rodada 17: focinho mais saliente
put(ell((0, 0.64, 0.06), (0.20, 0.22, 0.14), 14, 0.06), muzzle_mat)                   # ponte do nariz
for s_ in (1, -1):
    put(ell((s_ * 0.12, 0.965, -0.06), (0.05, 0.03, 0.03), 12, 0.02), const('stone_dark'))   # narina (rodada 16: menor e afundada)
# boca aberta em "U" (rodada 12): borda de cima reta sob o focinho, fundo curvo; interior aceso em lava,
# lábio de pedra contornando o "U", queixo abaixo e presas cor de osso presas na gengiva
def mz_top(x): return -0.46
def mz_bot(x): return -0.52 - 0.27 * (1 - (x / 0.42) ** 2)   # rodada 14: U mais fundo
def mz_y(x): return 0.72 - 0.20 * (x / 0.42) ** 2
XS = [-0.42 + k * 0.105 for k in range(9)]
put([hp(x, y, z) for x in XS for y in (0.44, mz_y(x)) for z in (mz_top(x), mz_bot(x) + 0.01)], const('glow_magma'), glow=True)
for a_, b_ in zip(XS[:-1], XS[1:]):   # lábio de baixo: faixa de pedra clara seguindo o fundo do "U"
    put([hp(x, y, z) for x in (a_ - 0.01, b_ + 0.01) for y in (mz_y(x) + 0.03, mz_y(x) - 0.14) for z in (mz_bot(x), mz_bot(x) - 0.10)], muzzle_mat)
for s_ in (1, -1):   # bochechas que fecham os cantos da boca
    put(ell((s_ * 0.49, 0.50, -0.56), (0.15, 0.28, 0.21), 16, 0.05), muzzle_mat)   # rodada 13: no tom do focinho
# queixo pesado e garganta que encosta no peito
put(ell((0, 0.40, -0.94), (0.52, 0.38, 0.26), 26, 0.05), muzzle_mat)   # rodada 15: queixo mais fundo, encaixa no pescoço   # rodada 13: queixo no tom do focinho (rosto numa peça só)
for x0 in (-0.15, 0.0, 0.15):   # fileira de dentes de baixo, curtos, presos no lábio
    b0 = Vector((x0, mz_y(x0) - 0.03, mz_bot(x0) + 0.005)); tip = Vector((x0, mz_y(x0) - 0.01, mz_bot(x0) + 0.16))
    put([hp(*(b0 + Vector((dx, dy, 0)))) for dx in (-0.045, 0.045) for dy in (-0.035, 0.035)] + [hp(*tip)], const('stone_tooth'))
put(ell((0, 0.12, -0.94), (0.50, 0.36, 0.38), 22, 0.08), rock_mat(Vector((0, 1, -0.4)).normalized()))
for s_ in (1, -1):
    # presa de baixo, grossa, saindo do lábio e subindo por fora do focinho
    b0 = Vector((s_ * 0.27, mz_y(0.27) - 0.02, mz_bot(0.27) - 0.02)); tip = Vector((s_ * 0.27, mz_y(0.27) + 0.08, -0.46))   # rodada 16: presa em pé, presa na mandíbula
    pts = [hp(*(b0 + Vector((dx, dy, 0)))) for dx in (-0.08, 0.08) for dy in (-0.06, 0.06)] + [hp(*tip)]
    pts += [hp(*(b0.lerp(tip, 0.45) + Vector((dx, 0.03, 0)))) for dx in (-0.055, 0.055)]
    put(pts, const('stone_tooth'))
    # presa de cima descendo da gengiva e dente pequeno ao lado
    for x0, w, L in ((0.14, 0.06, 0.18), (0.045, 0.045, 0.12)):
        b0 = Vector((s_ * x0, mz_y(x0) - 0.01, -0.45)); tip = Vector((s_ * x0, mz_y(x0) + 0.01, -0.45 - L))
        pts = [hp(*(b0 + Vector((dx, dy, 0)))) for dx in (-w, w) for dy in (-0.045, 0.03)] + [hp(*tip)]
        put(pts, const('stone_tooth'))
# o corpo continua com o mesmo gerador de antes (a cabeça antiga gastava 337 números)
rng.setstate(_rng_state)
for _ in range(337): rng.random()
# ---------------------------------------------------------------- shoulder columns + obsidian crystals
def cluster(side):
    s = 1 if side == 'R' else -1
    C = COL_C[side]
    out = Vector((s * 0.35, -0.25, 1)).normalized()
    cols = []
    for i in range(10):
        a = rng.uniform(0, 6.28); d = math.sqrt(rng.random()) * 0.42
        p = C + Vector((math.cos(a) * d, math.sin(a) * d * 0.9, 0))
        r = rng.uniform(0.11, 0.17)
        if any((p - q).length < (r + rq) * 0.95 for q, rq in cols): continue
        cols.append((p, r))
    for p, r in cols:
        dist = (Vector((p.x, p.y, 0)) - Vector((C.x, C.y, 0))).length
        L = rng.uniform(0.75, 1.35) * (1.2 - dist)
        bm = hexprism(p + Vector((0, 0, -0.35)), out + Vector((rng.uniform(-.12, .12), rng.uniform(-.12, .12), 0)), r * 1.15, L + 0.35, rot=rng.uniform(0, 1))
        BODY.add_bm(bm, 'chest', column_mat); bm.free()
    return cols
cluster('R'); cluster('L')
# broken column on the right shoulder: jagged stump + fallen chunk
C = COL_C['R'] + Vector((0.38, 0.22, 0))
bm = hexprism(C + Vector((0, 0, -0.3)), Vector((0.3, 0.1, 1)), 0.19, 0.75, top_jitter=0.0)
for v in bm.verts:
    if v.co.z > 3.7: v.co.z += rng.uniform(-0.18, 0.12)
bm.normal_update(); BODY.add_bm(bm, 'chest', column_mat); bm.free()
bm = hexprism(C + Vector((0.12, 0.30, 0.22)), Vector((0.9, 0.5, -0.25)), 0.16, 0.42, top_jitter=0.1)
BODY.add_bm(bm, 'chest', column_mat); bm.free()
# crystals (signature): left 2 tall + 1 small, right 3
CRY = [('L', Vector((-0.10, -0.12, 0)), 2.05, 0.21, Vector((-0.30, -0.18, 1))),
       ('L', Vector((0.22, 0.10, 0)), 1.70, 0.19, Vector((-0.10, -0.05, 1))),
       ('L', Vector((-0.30, 0.18, 0)), 0.85, 0.14, Vector((-0.6, 0.1, 1))),
       ('R', Vector((0.12, -0.15, 0)), 2.00, 0.21, Vector((0.28, -0.2, 1))),
       ('R', Vector((-0.20, -0.02, 0)), 1.55, 0.18, Vector((0.05, -0.1, 1))),
       ('R', Vector((0.05, 0.22, 0)), 1.15, 0.16, Vector((0.25, 0.15, 1)))]
for side, off, L, r, ax in CRY:
    # rodada 10: base 40% mais grossa (deixam de ler como palitos) e ponta sem brasa (brilho só nas fendas e no rosto)
    bm = crystal(COL_C[side] + off + Vector((0, 0, 0.05)), ax, r * 1.40, L)
    BODY.add_bm(bm, 'chest', obs_mat); bm.free()

# ---------------------------------------------------------------- back crater
F = frame(crater_n)
def to_cr(v): return crater_p + F @ v
bm = bmesh.new()
outer_b, outer_t, inner_r, depth = 0.55, 0.36, 0.24, 0.30
ringpts = []
for k in range(9):
    a = k * 2 * math.pi / 9 + rng.uniform(-0.12, 0.12)
    ringpts.append(a)
# build as stacked rings: bottom outer, top outer, top inner, bottom inner
rings = []
for rad, z in ((outer_b, -0.15), (outer_t * rng.uniform(0.95, 1.05), 0.38), (inner_r, 0.40), (inner_r * 0.8, 0.40 - depth)):
    rings.append([bm.verts.new(to_cr(Vector((math.cos(a) * rad * rng.uniform(0.92, 1.08), math.sin(a) * rad * rng.uniform(0.92, 1.08), z + rng.uniform(-0.04, 0.04))))) for a in ringpts])
mats_cr = []
for ri in range(3):
    for k in range(9):
        a0, a1 = rings[ri][k], rings[ri][(k + 1) % 9]; b0, b1 = rings[ri + 1][k], rings[ri + 1][(k + 1) % 9]
        f = bm.faces.new((a0, a1, b1, b0))
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
bm.verts.index_update(); bm.normal_update()
def crater_mat(f):
    c = f.calc_center_median()
    lc = F.transposed() @ (c - crater_p)
    if lc.z > 0.36: return MI['stone_light']
    if math.hypot(lc.x, lc.y) < inner_r * 1.05: return MI['stone_dark']
    return MI['stone_mid'] if f.normal.z > 0 else MI['stone_dark']
BODY.add_bm(bm, 'chest', crater_mat); bm.free()
hb = bmesh.new(); bmesh.ops.create_circle(hb, cap_ends=True, segments=9, radius=inner_r * 0.85)
for v in hb.verts: v.co = to_cr(Vector((v.co.x, v.co.y, 0.40 - depth + 0.04)))
hb.normal_update(); GLOW.add_bm(hb, 'chest', const('glow_magma')); hb.free()
hb = bmesh.new(); bmesh.ops.create_icosphere(hb, subdivisions=1, radius=0.13)
bmesh.ops.transform(hb, matrix=Matrix.Translation(to_cr(Vector((0, 0, 0.18)))), verts=hb.verts[:])
GLOW.add_bm(hb, 'chest', const('glow_magma')); hb.free()

# ---------------------------------------------------------------- hands (4 thick knuckle columns) and feet (3 toes)
for side in 'RL':
    s = 1 if side == 'R' else -1
    fc = J['fist.' + side]
    for i, xo in enumerate((-0.27, -0.09, 0.09, 0.27)):
        # rodada 15: nós dos dedos maiores e mais à frente, com a face da frente clara (o punho lê como punho)
        base = fc + Vector((xo * 1.55, 0.26, -0.24 + abs(xo) * 0.15))
        bm = hexprism(base, Vector((s * 0.05 * (i - 1.5), 1, -0.08)), 0.235, 0.62 - abs(xo) * 0.2, top_jitter=0.03, rot=0.52)
        BODY.add_bm(bm, 'hand.' + side, lambda f: MI['stone_muzzle'] if f.normal.y > 0.75 else column_mat(f)); bm.free()
    # thumb
    bm = hexprism(fc + Vector((-s * 0.38, 0.05, -0.1)), Vector((-s * 0.4, 1, -0.3)), 0.11, 0.3, rot=0.3)
    BODY.add_bm(bm, 'hand.' + side, column_mat); bm.free()
    ac = Vector((s * 0.96, -0.08, 0.16))
    for i, xo in enumerate((-0.24, 0.0, 0.24)):
        tp = ac + Vector((xo, 0.50 - abs(xo) * 0.3, 0.0))
        bm = hull(rockcloud(tp, (0.12, 0.13, 0.11), 10)); BODY.add_bm(bm, 'foot.' + side, rock_mat(Vector((0, 0.5, 0.8)).normalized())); bm.free()
        cl = [tp + Vector((0, 0.10, -0.06)) + Vector((dx, 0, dz)) for dx in (-0.06, 0.06) for dz in (-0.05, 0.04)] + [tp + Vector((0, 0.30, -0.12))]
        bm = hull(cl); BODY.add_bm(bm, 'foot.' + side, obs_mat); bm.free()

# ---------------------------------------------------------------- core into BODY (smooth, weighted)
core_base = len(BODY.V)
bm_core.verts.index_update()
uv_core = []
for v in bm_core.verts: BODY.V.append(v.co.copy()); BODY.VB.append(None)
# v3: o magma só aparece nas fendas finas entre placas (veias). Face do núcleo exposta numa área aberta,
# sem placas dos lados, vira basalto escuro, para o brilho ficar perto de 20% da superfície.
shell = BVHTree.FromPolygons([tuple(v) for v in BODY.V[:core_base]], BODY.F)
def covered(o, n): return shell.ray_cast(o, n, 0.6)[0] is not None
nvein = ndark = 0
for f in bm_core.faces:
    c = f.calc_center_median(); n = f.normal; o = c + n * 0.01
    mi = MI['magma_core']
    if (c - HEAD_C).length < 0.95 or (c - H).length < 1.55:   # rodada 4: rosto sem magma; rodada 11: nem em volta da cabeça
        mi = MI['stone_dark']; ndark += 1
    elif not covered(o, n):
        t = frame(n)
        hits = sum(covered(o + t @ Vector((math.cos(a) * 0.11, math.sin(a) * 0.11, 0)), n) for a in np.linspace(0, 2 * math.pi, 8)[:-1])
        seam = (c - star_p).length < 1.25 or any((c - J[j + '.' + sd]).length < 0.55 for j in ('shoulder', 'elbow', 'wrist', 'knee') for sd in 'RL')
        if hits >= 5 and (c - HEAD_C).length > 0.95: nvein += 1   # rodada 17: frestas estreitas (menos lascas soltas nos vãos)   # rodada 15: veias em toda fresta estreita (rede contínua), não só nas juntas
        else: mi = MI['stone_dark']; ndark += 1
    BODY.F.append([core_base + v.index for v in f.verts]); BODY.FM.append(mi); BODY.smooth.append(mi == MI['magma_core'])
print('core vein faces', nvein, 'dark', ndark)

# ---------------------------------------------------------------- palette texture (1 image, 8 swatches of 32 px)
# rodada 13: pedra puxada para o grafite do lote (sem lilás); cristais em obsidiana grafite
PAL = ['3F3C46', '2F2D35', '1E1C22', '18171C', '403D47', 'FF7A1A', 'FFB030', 'FF7A1A', 'B08A45', 'FFE6A0', '57535F', 'A83C10',
       '524E59', 'D6CFC4', '37353E', '28262D']   # rodada 16: focinho quase no tom do corpo; rodada 15: grafite mais escuro, no tom da Phoenix e do Dragon
SW = {'stone_light': 0, 'stone_mid': 1, 'stone_dark': 2, 'obsidian': 3, 'obsidian_highlight': 4,
      'glow_magma': 5, 'glow_hot': 6, 'magma_core': 7, 'gold': 8, 'eye_core': 9, 'stone_edge': 10, 'mouth_glow': 11,
      'stone_muzzle': 12, 'stone_tooth': 13, 'stone_mid_b': 14, 'stone_mid_c': 15}
pal = np.zeros((32, 512, 3))   # 16 faixas de 32 px
for k, h in enumerate(PAL): pal[:, k * 32:(k + 1) * 32] = hexc(h)[:3]
IMG_PAL = np_to_image('LavaTitan_paleta', pal)
for im in (IMG_C, IMG_E): bpy.data.images.remove(im)   # v3 usa só a paleta

def pal_mat(name, rough, emit=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes['Principled BSDF']
    t = nt.nodes.new('ShaderNodeTexImage'); t.image = IMG_PAL; t.interpolation = 'Closest'
    nt.links.new(t.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = rough
    if emit:
        nt.links.new(t.outputs['Color'], b.inputs['Emission Color'])
        b.inputs['Emission Strength'].default_value = emit
    return m
PART_MAT = {'Rock': pal_mat('LavaTitan_Rock', 0.93), 'Crystal': pal_mat('LavaTitan_Crystal', 0.5),
            'Magma': pal_mat('LavaTitan_Magma', 0.6, 2.5), 'Eyes': pal_mat('LavaTitan_Eyes', 0.5, 9.0)}
NAME_OF = {i: m.name for i, m in enumerate(MATS)}
def part_of(mname):
    if mname.startswith('stone'): return 'Rock'
    if mname in ('glow_hot', 'eye_core'): return 'Eyes'   # olhos: MeshPart Neon própria
    if mname.startswith('obsidian') or mname == 'gold': return 'Crystal'   # malha de acento: obsidiana + filete dourado
    return 'Magma'

def split(B):
    out = {k: Builder() for k in PART_MAT}
    remap = {k: {} for k in PART_MAT}
    for f, fm, sm in zip(B.F, B.FM, B.smooth):
        mname = NAME_OF[fm]; k = part_of(mname); P = out[k]; rmp = remap[k]
        idx = []
        for vi in f:
            if vi not in rmp:
                rmp[vi] = len(P.V); P.V.append(B.V[vi]); P.VB.append(B.VB[vi])
            idx.append(rmp[vi])
        P.F.append(idx); P.FM.append(SW[mname]); P.smooth.append(sm)
    return out
PARTS = {k: Builder() for k in PART_MAT}
for B in (BODY, GLOW):
    for k, P in split(B).items():
        base = len(PARTS[k].V)
        PARTS[k].V += P.V; PARTS[k].VB += P.VB; PARTS[k].smooth += P.smooth; PARTS[k].FM += P.FM
        PARTS[k].F += [[base + i for i in f] for f in P.F]

def build(name, B):
    me = bpy.data.meshes.new(name)
    me.from_pydata([(v.x, v.y, max(v.z, 0.0)) for v in B.V], [], B.F)   # pivô no chão: nada abaixo de z = 0
    me.validate()
    me.materials.append(PART_MAT[name.split('_')[1]])
    me.polygons.foreach_set('use_smooth', B.smooth)
    uv = me.uv_layers.new(name='UVMap')
    for p, sw in zip(me.polygons, B.FM):
        for li in p.loop_indices: uv.data[li].uv = ((sw + 0.5) / 16, 0.5)
    ob = bpy.data.objects.new(name, me); bpy.context.scene.collection.objects.link(ob)
    return ob
MESHES = {k: build('LavaTitan_' + k, PARTS[k]) for k in PART_MAT}

# ---------------------------------------------------------------- armature + weights
arm_d = bpy.data.armatures.new('LavaTitan_Rig')
rig = bpy.data.objects.new('LavaTitan_Rig', arm_d); bpy.context.scene.collection.objects.link(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='EDIT')
eb = {}
rb = arm_d.edit_bones.new('root'); rb.head = (0, 0, 0); rb.tail = (0, 0.5, 0); eb['root'] = rb
for name, (a, b_) in BONES.items():
    e = arm_d.edit_bones.new(name); e.head = a; e.tail = b_; eb[name] = e
for name in BONES:
    eb[name].parent = eb[PARENT.get(name, 'root')]
    eb[name].use_connect = False
bpy.ops.object.mode_set(mode='OBJECT')

def skin(ob, B):
    for name in BONES: ob.vertex_groups.new(name=name)
    names = list(BONES)
    segs = [(BONES[n][0], BONES[n][1]) for n in names]
    for i, v in enumerate(B.V):
        if B.VB[i] is not None:
            ob.vertex_groups[B.VB[i]].add([i], 1.0, 'REPLACE'); continue
        ds = []
        for (a, b_) in segs:
            ab = b_ - a; t = max(0, min(1, (v - a).dot(ab) / ab.length_squared)); ds.append((a + ab * t - v).length)
        order = sorted(range(len(ds)), key=lambda k: ds[k])[:3]
        w = [1 / (ds[k] ** 4 + 1e-4) for k in order]; sw = sum(w)
        for k, wk in zip(order, w):
            if wk / sw > 0.02: ob.vertex_groups[names[k]].add([i], wk / sw, 'REPLACE')
    ob.parent = rig
    mod = ob.modifiers.new('Armature', 'ARMATURE'); mod.object = rig
for k, ob in MESHES.items(): skin(ob, PARTS[k])

# crater light (exported as KHR_lights_punctual)
ld = bpy.data.lights.new('LavaTitan_CraterLight', 'POINT'); ld.color = hexc('FF7A1E')[:3]; ld.energy = 60; ld.shadow_soft_size = 0.2
lo = bpy.data.objects.new('LavaTitan_CraterLight', ld); bpy.context.scene.collection.objects.link(lo)
lo.location = to_cr(Vector((0, 0, 0.6))); lo.parent = rig; lo.parent_type = 'BONE'; lo.parent_bone = 'chest'
lo.matrix_world = Matrix.Translation(to_cr(Vector((0, 0, 0.6))))

# ---------------------------------------------------------------- clips (in place, 30 fps, loop: first key == last key)
FPS = 30
sc = bpy.context.scene; sc.render.fps = FPS
for pb in rig.pose.bones: pb.rotation_mode = 'QUATERNION'
REST = {b.name: b.matrix_local.to_quaternion() for b in arm_d.bones}

def wq(rx=0.0, ry=0.0, rz=0.0):
    # rotation in the rig's rest axes (X = right of the pet, Y = front, Z = up), X applied first
    return Quaternion((0, 0, 1), rz) @ Quaternion((0, 1, 0), ry) @ Quaternion((1, 0, 0), rx)
def pose(frame, rots, lift=0.0):
    for pb in rig.pose.bones:
        r = rots.get(pb.name, (0, 0, 0))
        q = REST[pb.name].inverted() @ wq(*r) @ REST[pb.name]
        pb.rotation_quaternion = q; pb.keyframe_insert('rotation_quaternion', frame=frame)
    root = rig.pose.bones['root']
    root.location = REST['root'].inverted() @ Vector((0, 0, lift)); root.keyframe_insert('location', frame=frame)

def mirror(d):
    out = {}
    for k, (x, y, z) in d.items():
        if k.endswith('.R'): out[k[:-2] + '.L'] = (x, -y, -z)
        elif k.endswith('.L'): out[k[:-2] + '.R'] = (x, -y, -z)
        else: out[k] = (x, -y, -z)
    return out

def clip(name, keys):
    rig.animation_data_create(); rig.animation_data.action = None
    for f, rots, lift in keys: pose(f, rots, lift)
    act = rig.animation_data.action; act.name = name; act.use_fake_user = True
    end = keys[-1][0]; act.frame_range = (0, end); act.use_frame_range = True
    tr = rig.animation_data.nla_tracks.new(); tr.name = name
    tr.strips.new(name, 0, act); rig.animation_data.action = None
    return act

# Idle 3,5 s: respiração pesada, ombros sobem
inhale = {'chest': (0.05, 0, 0), 'head': (-0.06, 0, 0), 'upperarm.R': (-0.04, 0.03, 0), 'upperarm.L': (-0.04, -0.03, 0)}
clip('Idle', [(0, {}, 0), (52, inhale, 0.05), (105, {}, 0)])

# Walk 2,0 s: knuckle-walk, braço de um lado com a perna do outro
stepA = {'upperarm.R': (0.38, 0, 0), 'upperarm.L': (-0.32, 0, 0), 'thigh.L': (0.40, 0, 0), 'thigh.R': (-0.35, 0, 0),
         'shin.R': (0.15, 0, 0), 'hips': (0, 0, 0.07), 'chest': (0, 0, -0.10), 'head': (0, 0, 0.05)}
passA = {'shin.L': (-0.45, 0, 0), 'forearm.L': (0.35, 0, 0), 'chest': (0.03, 0, 0)}
clip('Walk', [(0, stepA, 0), (15, passA, 0.07), (30, mirror(stepA), 0), (45, mirror(passA), 0.07), (60, stepA, 0)])

# Happy 2,5 s: bate no peito 3x e ergue os punhos
beatR = {'upperarm.R': (0.70, 0, 0.70), 'forearm.R': (1.35, 0, 0.45), 'upperarm.L': (0.45, -0.25, 0),
         'chest': (0.18, 0, 0), 'head': (0.20, 0, 0)}
beatL = mirror(beatR)
cheer = {'upperarm.R': (2.30, -0.35, 0), 'upperarm.L': (2.30, 0.35, 0), 'forearm.R': (0.30, 0, 0), 'forearm.L': (0.30, 0, 0),
         'chest': (0.22, 0, 0), 'head': (0.30, 0, 0)}
clip('Happy', [(0, {}, 0), (11, beatR, 0.08), (23, beatL, 0.08), (35, beatR, 0.08), (50, cheer, 0.30), (62, {}, 0.02), (75, {}, 0)])

# Slam 2,2 s: ergue os punhos, bate no chão em 0,5 s (fx), volta
raise_ = {'upperarm.R': (2.40, -0.25, 0), 'upperarm.L': (2.40, 0.25, 0), 'forearm.R': (0.40, 0, 0), 'forearm.L': (0.40, 0, 0),
          'chest': (0.25, 0, 0), 'head': (0.15, 0, 0), 'thigh.R': (0.15, 0, 0), 'thigh.L': (0.15, 0, 0)}
hit = {'upperarm.R': (0.15, 0.10, 0), 'upperarm.L': (0.15, -0.10, 0), 'chest': (-0.28, 0, 0), 'head': (-0.10, 0, 0),
       'thigh.R': (0.35, 0, 0), 'thigh.L': (0.35, 0, 0), 'shin.R': (-0.35, 0, 0), 'shin.L': (-0.35, 0, 0)}
clip('Slam', [(0, {}, 0), (10, raise_, 0.25), (15, hit, -0.18), (36, hit, -0.18), (54, {}, 0.02), (66, {}, 0)])

if '--pose-test' in sys.argv:
    import json
    res = {}
    for tr in rig.animation_data.nla_tracks:
        for f in range(0, int(tr.strips[0].action.frame_range[1]) + 1, 5):
            tr.is_solo = True; sc.frame_set(f)
            res[f'{tr.name}_{f}'] = [round(x, 2) for x in rig.matrix_world @ rig.pose.bones['hand.R'].tail]
            tr.is_solo = False
    print('POSE', json.dumps(res))

def tris(ob):
    return sum(len(p.vertices) - 2 for p in ob.data.polygons)
for k, ob in MESHES.items(): print('TRIS', k, tris(ob))
print('BONES', len(arm_d.bones), 'CLIPS', [a.name for a in bpy.data.actions])
allz = [ (ob.matrix_world @ v.co) for ob in MESHES.values() for v in ob.data.vertices]
print('DIMS', round(max(v.x for v in allz) - min(v.x for v in allz), 2), round(max(v.y for v in allz) - min(v.y for v in allz), 2),
      round(max(v.z for v in allz), 2), 'zmin', round(min(v.z for v in allz), 3))

sc.frame_set(0)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, 'lava_titan_v3.blend'))
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, 'LavaTitan.glb'), export_format='GLB', export_lights=False,
                          export_apply=False, export_skins=True, export_animations=True,
                          export_animation_mode='NLA_TRACKS', export_force_sampling=True, export_frame_range=False)
print('DONE')
