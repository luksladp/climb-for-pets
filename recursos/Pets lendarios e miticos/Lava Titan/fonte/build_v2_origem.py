# Lava Titan v2 — procedural build in Blender (bpy). Units = studs, Z up, front = +Y.
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

M_STONE_L = mat('stone_light', '8A8381', 0.78)
M_STONE_M = mat('stone_mid', '5A4F4B', 0.82)
M_STONE_D = mat('stone_dark', '2E2829', 0.85)
M_OBS = mat('obsidian', '121016', 0.32)
M_OBS_HI = mat('obsidian_highlight', '4A3A5A', 0.25)
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

col, emis = crack_texture()
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

MATS = [M_CORE, M_STONE_L, M_STONE_M, M_STONE_D, M_OBS, M_OBS_HI, M_GLOW, M_GLOW_HOT]
MI = {m.name: i for i, m in enumerate(MATS)}

# ---------------------------------------------------------------- skeleton (joint positions)
J = {}
for s, side in ((1, 'R'), (-1, 'L')):   # facing +Y, character's right is +X
    J['shoulder.' + side] = Vector((s * 1.25, 0.25, 3.10))
    J['elbow.' + side] = Vector((s * 1.50, 0.55, 2.00))
    J['wrist.' + side] = Vector((s * 1.48, 0.92, 0.80))
    J['fist.' + side] = Vector((s * 1.45, 1.05, 0.42))
    J['hip.' + side] = Vector((s * 0.55, -0.45, 1.55))
    J['knee.' + side] = Vector((s * 0.72, -0.12, 0.88))
    J['ankle.' + side] = Vector((s * 0.74, -0.25, 0.32))
HEAD_C = Vector((0, 1.12, 3.62))

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

add_ellipsoid(core_bm, Vector((0, 0.0, 3.05)), (1.30, 0.80, 0.68))   # shoulder yoke
add_ellipsoid(core_bm, Vector((0, -0.35, 3.0)), (1.05, 0.62, 0.62))   # back hump
add_ellipsoid(core_bm, Vector((0, 0.50, 2.72)), (0.80, 0.55, 0.70))   # chest
add_ellipsoid(core_bm, Vector((0, 0.10, 2.15)), (0.62, 0.55, 0.60))   # belly
add_ellipsoid(core_bm, Vector((0, -0.40, 1.72)), (0.66, 0.50, 0.45))  # pelvis
add_ellipsoid(core_bm, HEAD_C, (0.46, 0.46, 0.44))                    # head core
for side in 'RL':
    s = 1 if side == 'R' else -1
    add_ellipsoid(core_bm, J['shoulder.' + side] + Vector((0, -0.05, 0.05)), (0.52, 0.52, 0.50))
    add_limb(core_bm, J['shoulder.' + side], J['elbow.' + side], 0.36, 0.34)
    add_limb(core_bm, J['elbow.' + side], J['wrist.' + side], 0.42, 0.46)
    add_ellipsoid(core_bm, J['elbow.' + side].lerp(J['wrist.' + side], 0.55), (0.52, 0.52, 0.55))
    add_ellipsoid(core_bm, J['fist.' + side], (0.50, 0.52, 0.40))
    add_limb(core_bm, J['hip.' + side], J['knee.' + side], 0.42, 0.40)
    add_limb(core_bm, J['knee.' + side], J['ankle.' + side], 0.40, 0.36)
    add_ellipsoid(core_bm, Vector((s * 0.76, -0.08, 0.20)), (0.42, 0.55, 0.20))

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
        pts.append(Vector((math.cos(a) * r * 0.86, math.sin(a) * r * 0.86, L * 0.72)))
    pts += [Vector((0, 0, L)), Vector((0, 0, -0.35))]
    bm = hull(pts)
    q = Vector((0, 0, 1)).rotation_difference(axis.normalized())
    bmesh.ops.transform(bm, matrix=Matrix.Translation(base) @ q.to_matrix().to_4x4(), verts=bm.verts[:])
    bm.normal_update()
    return bm
def obs_mat(f):
    return MI['obsidian_highlight'] if f.normal.dot(Vector((-0.45, 0.75, 0.45)).normalized()) > 0.9 else MI['obsidian']

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
    'chest': (Vector((0, 0.1, 2.9)), Vector((0, 0.3, 3.5))),
    'head': (Vector((0, 0.72, 3.15)), Vector((0, 0.95, 3.75))),
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
COL_C = {'R': Vector((1.02, -0.20, 3.45)), 'L': Vector((-1.02, -0.20, 3.45))}

def blocked(p):
    if (p - star_p).length < 0.80: return True
    if (p - crater_p).length < 0.56: return True
    if (p - fall_p).length < 0.38: return True
    if (p - HEAD_C).length < 0.66 and p.y > HEAD_C.y - 0.25: return True
    for c in COL_C.values():
        if (Vector((p.x, p.y, 0)) - Vector((c.x, c.y, 0))).length < 0.34 and p.z > 3.2: return True
    return False

# ---------------------------------------------------------------- crust mosaic (power-diagram cells on the surface)
areas = np.array([f.calc_area() for f in bm_core.faces]); areas /= areas.sum()
nprng = np.random.default_rng(11)
cand = []
for fi in nprng.choice(len(areas), 30000, p=areas):
    f = bm_core.faces[int(fi)]
    vs = [v.co for v in f.verts]; w = nprng.dirichlet(np.ones(len(vs)))
    cand.append(sum((vv * float(wi) for vv, wi in zip(vs, w)), Vector()))
def cell_size(p, n):
    if p.z < 0.8: return 0.32
    if (p - HEAD_C).length < 0.75: return 0.32
    if p.z > 2.55 and (n.z > 0.2 or p.y < -0.15): return 0.52
    return 0.41
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
GAP = 0.045
nplates = 0
for i, (p, n, d) in enumerate(seeds):
    if blocked(p) or p.z < 0.06: continue
    Fm = frame(n); Ft = Fm.transposed()
    poly = [Vector((math.cos(a) * d * 0.85, math.sin(a) * d * 0.85)) for a in np.linspace(0, 2 * math.pi, 9)[:-1] + 0.2]
    poly = [v * (1.0 / 0.85) for v in poly]
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
        w = v.lerp(cen, 0.22); pts.append(Vector((w.x, w.y, h * rng.uniform(0.85, 1.0))))
    off = Vector((rng.uniform(-.2, .2), rng.uniform(-.2, .2))) * d * 0.5
    pts.append(Vector((cen.x + off.x, cen.y + off.y, h * 1.12)))
    tilt = Matrix.Rotation(rng.uniform(-0.08, 0.08), 3, 'X') @ Matrix.Rotation(rng.uniform(-0.08, 0.08), 3, 'Y')
    bm = hull([p + Fm @ (tilt @ v) for v in pts])
    BODY.add_bm(bm, nearest_bone(p), rock_mat(n)); bm.free(); nplates += 1
print('plates', nplates)

# fallen plate on left forearm (hangs loose, shows magma)
bm, _ = plate(fall_p + fall_n * 0.12 + Vector((0, 0, -0.18)), (fall_n + Vector((0, 0.3, -0.9))).normalized(), 0.3, tilt=0.0)
BODY.add_bm(bm, 'forearm.L', rock_mat(fall_n)); bm.free()

# ---------------------------------------------------------------- chest star (5 sector plates + furnace)
SR = 0.64
F = frame(star_n)
def to_star(v): return star_p + F @ v
corners = [Vector((math.cos(math.pi / 2 + i * 2 * math.pi / 5) * SR, math.sin(math.pi / 2 + i * 2 * math.pi / 5) * SR, 0)) for i in range(5)]
# frame(): local x = t (world X-ish), local y = b (world up-ish)
gap = 0.055
for i in range(5):
    a, b_ = corners[i], corners[(i + 1) % 5]
    c = (a + b_) / 3
    tri = []
    for v in (Vector((0, 0, 0)), a, b_):
        # shrink toward centroid by gap
        d = (c - v); tri.append(v + d.normalized() * gap * 1.6 if d.length > 1e-6 else v)
    pts = []
    for v in tri:
        pts.append(v + Vector((0, 0, -0.12)))
        pts.append(v + Vector((0, 0, 0.12)))
        pts.append(v.lerp(c, 0.25) + Vector((0, 0, 0.24)))
    pts.append(c + Vector((0.02, -0.02, 0.30)))
    bm = hull([to_star(p) for p in pts]); bm.normal_update()
    BODY.add_bm(bm, 'chest', rock_mat(star_n)); bm.free()
# outer double ring of plates around star
for i in range(5):
    a = math.pi / 2 + (i + 0.5) * 2 * math.pi / 5
    pp = to_star(Vector((math.cos(a) * 0.80, math.sin(a) * 0.80, 0)))
    _, nrm, _, _ = bvh.find_nearest(pp)
    bm, _ = plate(pp, nrm, 0.26, tilt=0.05)
    BODY.add_bm(bm, 'chest', rock_mat(nrm)); bm.free()
# furnace: glowing pentagram ridge + hot core
bm = bmesh.new()
for i in range(5):
    a = corners[i]
    dirv = a.normalized(); side = Vector((-dirv.y, dirv.x, 0))
    w = 0.05
    pts = [Vector((0, 0, -0.05)) + side * w, Vector((0, 0, -0.05)) - side * w, a * 1.02 + side * 0.01, a * 1.02 - side * 0.01,
           Vector((0, 0, 0.14)) + side * w, Vector((0, 0, 0.14)) - side * w, a * 1.02 + Vector((0, 0, 0.06)), ]
    hb = hull([to_star(p) for p in pts]); GLOW.add_bm(hb, 'chest', const('glow_hot')); hb.free()
hb = bmesh.new(); bmesh.ops.create_icosphere(hb, subdivisions=2, radius=0.12)
bmesh.ops.transform(hb, matrix=Matrix.Translation(to_star(Vector((0, 0, 0.18)))), verts=hb.verts[:])
GLOW.add_bm(hb, 'chest', const('glow_hot')); hb.free()
# pentagon furnace plate under the sectors
hb = bmesh.new(); g = bmesh.ops.create_circle(hb, cap_ends=True, segments=5, radius=SR * 0.98)
bmesh.ops.rotate(hb, cent=Vector(), matrix=Matrix.Rotation(math.pi / 2 - math.pi / 2, 3, 'Z'), verts=hb.verts[:])
for v in hb.verts: v.co = to_star(Vector((v.co.x, v.co.y, 0.0)))
hb.normal_update(); GLOW.add_bm(hb, 'chest', const('glow_magma')); hb.free()

# ---------------------------------------------------------------- head
H = HEAD_C
HS = 1.15
def rockcloud(c, half, n=14, jitter=1.0):
    return [c + Vector((rng.uniform(-1, 1) * half[0], rng.uniform(-1, 1) * half[1], rng.uniform(-1, 1) * half[2])) for _ in range(n)]
def hc(c, half, n=14): return rockcloud(c, tuple(x * HS for x in half), n)
def head_rock(pts, axis=Vector((0, 1, 0.3))):
    bm = hull(pts); BODY.add_bm(bm, 'head', rock_mat(axis.normalized())); bm.free()
# cranium / brow ledge (overhangs the eyes)
head_rock(hc(H + HS * Vector((0, 0.05, 0.28)), (0.40, 0.36, 0.14)), Vector((0, 0.2, 1)))
brow = [H + HS * Vector((x, 0.42 + rng.uniform(-.03, .05), 0.16 + rng.uniform(-.02, .05))) for x in (-0.44, -0.3, -0.15, 0, 0.15, 0.3, 0.44)]
brow += [p + Vector((0, -0.28, 0.08)) for p in brow] + [p + Vector((0, -0.02, 0.13)) for p in brow]
brow += [H + HS * Vector((x, 0.46, 0.20)) for x in (-0.25, 0.25)]
head_rock(brow, Vector((0, 0.6, 0.8)))
# heavy jaw (juts forward)
jaw = hc(H + HS * Vector((0, 0.40, -0.22)), (0.36, 0.22, 0.16), 16)
jaw += [H + HS * Vector((x, 0.62, -0.20 + z)) for x in (-0.24, 0.24) for z in (-0.1, 0.06)]
head_rock(jaw, Vector((0, 1, 0.2)))
# muzzle / nose bridge
head_rock(hc(H + HS * Vector((0, 0.52, 0.0)), (0.17, 0.10, 0.07), 10), Vector((0, 1, 0.3)))
# cheeks
for s in (1, -1):
    head_rock(hc(H + HS * Vector((s * 0.36, 0.25, -0.02)), (0.12, 0.16, 0.16), 10), Vector((s * 0.7, 0.6, 0.2)))
# eyes: V slits, slanting down toward the middle, sunk under the brow
for s in (1, -1):
    inner = H + HS * Vector((s * 0.07, 0.50, 0.075)); outer = H + HS * Vector((s * 0.30, 0.43, 0.14))
    d = (outer - inner); up = Vector((0, 0, 1)); fwd = Vector((0, 1, 0))
    pts = []
    for t, hh in ((0, 0.02), (0.45, 0.045), (1, 0.012)):
        c = inner + d * t
        pts += [c + up * hh + fwd * 0.03, c - up * hh + fwd * 0.03, c + up * hh * 0.6 - fwd * 0.08, c - up * hh * 0.6 - fwd * 0.08]
    bm = hull(pts); GLOW.add_bm(bm, 'head', const('glow_hot')); bm.free()
# eye sockets (dark, behind the slits)
for s in (1, -1):
    bm = hull(hc(H + HS * Vector((s * 0.19, 0.40, 0.10)), (0.15, 0.06, 0.07), 12))
    BODY.add_bm(bm, 'head', const('stone_dark')); bm.free()
# horns: short, curved outward
for s in (1, -1):
    bm = bmesh.new(); prev = None
    pts_all = []
    base = H + HS * Vector((s * 0.30, -0.02, 0.36))
    path = [base + Vector((s * 0.13 * i, -0.04 * i, 0.07 * i - 0.012 * i * i)) for i in range(5)]
    for i, c in enumerate(path):
        rr = 0.10 * (1 - i / 4.6)
        for k in range(6):
            a = k * math.pi / 3
            pts_all.append(c + Vector((0, math.cos(a) * rr, math.sin(a) * rr)))
    # build hull of consecutive segments for a faceted curve
    for i in range(4):
        seg = pts_all[i * 6:(i + 2) * 6] if i < 3 else pts_all[i * 6:(i + 1) * 6] + [path[4] + Vector((s * 0.1, -0.02, -0.02))]
        hb = hull(seg); BODY.add_bm(hb, 'head', obs_mat); hb.free()

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
        bm = hexprism(p + Vector((0, 0, -0.35)), out + Vector((rng.uniform(-.12, .12), rng.uniform(-.12, .12), 0)), r, L + 0.35, rot=rng.uniform(0, 1))
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
    bm = crystal(COL_C[side] + off + Vector((0, 0, 0.05)), ax, r, L)
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
GLOW.add_bm(hb, 'chest', const('glow_hot')); hb.free()

# ---------------------------------------------------------------- hands (4 thick knuckle columns) and feet (3 toes)
for side in 'RL':
    s = 1 if side == 'R' else -1
    fc = J['fist.' + side]
    for i, xo in enumerate((-0.27, -0.09, 0.09, 0.27)):
        base = fc + Vector((xo * 1.05, 0.12, -0.24 + abs(xo) * 0.15))
        bm = hexprism(base, Vector((s * 0.05 * (i - 1.5), 1, -0.08)), 0.125, 0.40 - abs(xo) * 0.2, top_jitter=0.03, rot=0.52)
        BODY.add_bm(bm, 'hand.' + side, column_mat); bm.free()
    # thumb
    bm = hexprism(fc + Vector((-s * 0.38, 0.05, -0.1)), Vector((-s * 0.4, 1, -0.3)), 0.11, 0.3, rot=0.3)
    BODY.add_bm(bm, 'hand.' + side, column_mat); bm.free()
    ac = Vector((s * 0.76, -0.08, 0.16))
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
for f in bm_core.faces:
    BODY.F.append([core_base + v.index for v in f.verts]); BODY.FM.append(MI['magma_core']); BODY.smooth.append(True)

def build(name, B, uvscale=0.42):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(v) for v in B.V], [], B.F)
    me.validate()
    for m in MATS: me.materials.append(m)
    me.polygons.foreach_set('material_index', B.FM)
    me.polygons.foreach_set('use_smooth', B.smooth)
    uv = me.uv_layers.new(name='UVMap')
    for p in me.polygons:
        n = p.normal; ax = max(range(3), key=lambda i: abs(n[i]))
        for li in p.loop_indices:
            co = me.vertices[me.loops[li].vertex_index].co
            u, v = [(co.y, co.z), (co.x, co.z), (co.x, co.y)][ax]
            uv.data[li].uv = (u * uvscale, v * uvscale)
    ob = bpy.data.objects.new(name, me); bpy.context.scene.collection.objects.link(ob)
    return ob

body = build('LavaTitan_Body', BODY)
glow = build('LavaTitan_Glow', GLOW)

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
    if name in ('spine', 'chest') or name.startswith(('forearm', 'hand', 'shin', 'foot')):
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
skin(body, BODY); skin(glow, GLOW)

# crater light (exported as KHR_lights_punctual)
ld = bpy.data.lights.new('LavaTitan_CraterLight', 'POINT'); ld.color = hexc('FF7A1E')[:3]; ld.energy = 60; ld.shadow_soft_size = 0.2
lo = bpy.data.objects.new('LavaTitan_CraterLight', ld); bpy.context.scene.collection.objects.link(lo)
lo.location = to_cr(Vector((0, 0, 0.6))); lo.parent = rig; lo.parent_type = 'BONE'; lo.parent_bone = 'chest'
lo.matrix_world = Matrix.Translation(to_cr(Vector((0, 0, 0.6))))

def tris(ob):
    return sum(len(p.vertices) - 2 for p in ob.data.polygons)
print('TRIS body', tris(body), 'glow', tris(glow))
print('DIMS', tuple(round(x, 2) for x in body.dimensions), 'zmax', max(v.co.z for v in body.data.vertices))

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, 'lava_titan_v2.blend'))
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, 'lava-titan-v2.glb'), export_format='GLB', export_lights=True,
                          export_apply=False, export_skins=True, export_animations=False)
print('DONE')
