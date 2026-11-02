import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy, bmesh, numpy as np, math, random
from mathutils import Vector
from common import *
import plates as PL

OUT = os.environ.get('OUT', 'out'); os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
M = materials()
rng = np.random.default_rng(7); R = random.Random(7)

d = np.load('core.npz'); V = d['v']; F = d['f']; P = d['p']
me = bpy.data.meshes.new('core'); me.from_pydata(V.tolist(), [], F.tolist()); me.update()
core = bpy.data.objects.new('core', me); bpy.context.scene.collection.objects.link(core)
bm = bmesh.new(); bm.from_mesh(me); bmesh.ops.recalc_face_normals(bm, faces=bm.faces); bm.to_mesh(me); bm.free()
me.update()
N = np.array([v.normal for v in me.vertices])

from mathutils.bvhtree import BVHTree
bvh0 = BVHTree.FromPolygons([tuple(v) for v in V], F.tolist())
def _ray(o, d):
    h = bvh0.ray_cast(Vector(o), Vector(d).normalized())
    n = h[1]
    if n is not None and n.dot(Vector(d)) > 0: n = -n
    return h[0], n
ANCH = {}
ANCH['furnace'] = _ray((6, 0, 3.15), (-1, 0, 0))

# tail end: last core point along tail
tv = V[P == 'tail']; ti = np.argmin(tv[:, 0]); te = tv[ti]
ANCH['tail_end'] = (-4.9, 0, 3.0); ANCH['tail_dir'] = (-0.3, 0, 1.0)
GOLD_NECK = [False]
def classify(c, n, part):
    if np.linalg.norm(c - np.array(ANCH['furnace'][0])) < 0.5: return None
    base = part.rstrip('LR')
    if base in ('ffoot', 'hfoot') and c[2] < 0.25:
        return dict(top='skin', edge='skin', side='skin')
    if base == 'torso' and n[2] < -0.55:
        return dict(top='basalt', edge='obsidian_dark', side='obsidian_dark')
    if base == 'neck' and not GOLD_NECK[0] and c[2] > 4.3 and n[2] > 0.2 and c[1] > 0.1:
        GOLD_NECK[0] = True; return dict(top='gold', edge='gold_edge', side='gold')
    if base == 'torso' and n[2] > 0.72 and abs(c[1]) < 0.85:
        return dict(top='obsidian', edge='gold', side='obsidian_dark')
    return dict(top='obsidian', edge='obsidian_edge', side='obsidian_dark')

sub = np.arange(len(V))
mbp, info = PL.build_plates(core, V, N, P, rng, classify)
plates = to_object(mbp, 'plates', M, smooth=True)
es = plates.modifiers.new('es', 'EDGE_SPLIT'); es.split_angle = math.radians(32)
bpy.context.view_layer.objects.active = plates; bpy.ops.object.modifier_apply(modifier='es')
print('plates', len(info), 'faces', len(mbp.f))

# decimate core + magma material
core.data.materials.append(M['magma_body'])  # r11: fendas do corpo mais fracas que os olhos
for p in core.data.polygons: p.use_smooth = True
dm = core.modifiers.new('d', 'DECIMATE'); dm.ratio = 0.07
bpy.context.view_layer.objects.active = core
bpy.ops.object.modifier_apply(modifier='d')
# v5: magma só nos veios principais (peito, garganta, barriga); o resto da fresta fica pedra escura
core.data.materials.append(M['obsidian_dark'])
for p in core.data.polygons:
    c = p.center; n = p.normal
    chest = c.x > 1.3 and 2.0 < c.z < 4.9 and abs(c.y) < 1.1 and n.x > 0.1
    belly = c.z < 2.35 and abs(c.y) < 0.95 and -1.9 < c.x < 2.0 and n.z < -0.2
    neck = c.z > 3.6 and c.x > 1.6
    # r11: rede acesa na frente (peito, pescoço, barriga) e em ~45% das frestas do resto; costas apagam mais
    h = (math.sin(c.x * 12.9898 + c.y * 78.233 + c.z * 37.719) * 43758.5453) % 1.0
    lit = chest or belly or neck or (h < (0.12 if n.z > 0.5 else 0.3))  # r14: brilho concentrado em peito, garganta e barriga
    p.material_index = 0 if lit else 1
print('core faces', len(core.data.polygons))

if os.environ.get('PARTS', '1') == '1':
    exec(open('parts.py').read())

bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(f'{OUT}/dragon.blend'))
