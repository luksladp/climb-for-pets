import bpy, os, math, numpy as np
from mathutils import Vector as V, Matrix, Quaternion, Euler
OUT = os.environ.get('OUT', 'out')
bpy.ops.wm.open_mainfile(filepath=os.path.abspath(f'{OUT}/dragon.blend'))
sc = bpy.context.scene; sc.render.fps = 24
BONES = [  # name, head, tail, parent
    ('root', (0, 0, 0), (0, 0, 0.6), None),
    ('body', (-0.4, 0, 2.75), (1.3, 0, 2.95), 'root'),
    ('hips', (-0.4, 0, 2.75), (-1.9, 0, 2.6), 'body'),
    ('neck_1', (1.6, 0, 3.4), (2.5, 0, 4.35), 'body'),
    ('neck_2', (2.5, 0, 4.35), (2.85, 0, 4.95), 'neck_1'),
    ('head', (2.85, 0, 4.95), (3.9, 0, 5.4), 'neck_2'),
    ('jaw', (2.85, 0, 4.9), (4.6, 0, 4.55), 'head'),
    ('tail_1', (-1.9, 0, 2.6), (-3.0, 0, 2.05), 'hips'),
    ('tail_2', (-3.0, 0, 2.05), (-3.7, 0, 1.72), 'tail_1'),
    ('tail_3', (-3.7, 0, 1.72), (-4.3, 0, 1.85), 'tail_2'),
    ('tail_4', (-4.3, 0, 1.85), (-4.85, 0, 2.8), 'tail_3'),
]
for s, sd in ((1, 'L'), (-1, 'R')):
    BONES += [(f'wing_{sd}_1', (0.75, 0.9 * s, 3.95), (0.35, 2.2 * s, 5.4), 'body'),
              (f'wing_{sd}_2', (0.35, 2.2 * s, 5.4), (-0.3, 2.75 * s, 6.35), f'wing_{sd}_1'),
              (f'fleg_{sd}', (1.4, 1.0 * s, 2.7), (1.6, 1.1 * s, 1.2), 'body'),
              (f'ffoot_{sd}', (1.6, 1.1 * s, 1.2), (1.75, 1.15 * s, 0.15), f'fleg_{sd}'),
              (f'hleg_{sd}', (-1.4, 1.0 * s, 2.3), (-1.1, 1.1 * s, 1.0), 'hips'),
              (f'hfoot_{sd}', (-1.1, 1.1 * s, 1.0), (-1.1, 1.15 * s, 0.15), f'hleg_{sd}')]
# FX_* anchor bones (no skin weights): emitters/lights attach here in Roblox (Bone is an Attachment)
BONES += [('orbit', (-0.3, 0, 3.3), (-0.3, 0, 3.8), 'root')]
from common import head_x
BONES += [('FX_Crown', head_x((2.72, 0, 6.5)), head_x((2.72, 0, 6.8)), 'head'),
          ('FX_Nostril', head_x((4.85, 0, 5.2)), head_x((5.1, 0, 5.2)), 'head'),
          ('FX_Mouth', head_x((4.4, 0, 4.85)), head_x((4.8, 0, 4.85)), 'jaw'),
          ('FX_Furnace', (2.45, 0, 3.15), (2.75, 0, 3.15), 'body'),
          ('FX_Back', (-0.2, 0, 3.95), (-0.2, 0, 4.25), 'body'),
          ('FX_Ground', (0, 0, 0.05), (0, 0, 0.35), 'root')]
K = 0.82 * 9.0 / 10.42  # v10: cabe em 9 studs com a cabeça maior
for o in bpy.data.objects:
    if o.type == 'MESH' and o.name != 'floor_render': o.data.transform(Matrix.Scale(K, 4))
BONES = [(n, tuple(K * c for c in h), tuple(K * c for c in t), p) for n, h, t, p in BONES]
arm = bpy.data.armatures.new('molten_dragon'); ao = bpy.data.objects.new('molten_dragon', arm)
sc.collection.objects.link(ao); bpy.context.view_layer.objects.active = ao
bpy.ops.object.mode_set(mode='EDIT')
for n, h, t, p in BONES:
    b = arm.edit_bones.new(n); b.head = h; b.tail = t; b.roll = 0
    if p: b.parent = arm.edit_bones[p]; b.use_connect = False
bpy.ops.object.mode_set(mode='OBJECT')
seg = {n: (np.array(h, float), np.array(t, float)) for n, h, t, p in BONES}

def segdist(P, a, b):
    ab = b - a; t = np.clip(((P - a) @ ab) / (ab @ ab), 0, 1)
    return np.linalg.norm(P - (a + t[:, None] * ab), axis=1)

BODY = ['body', 'hips', 'neck_1', 'neck_2', 'head', 'tail_1', 'tail_2', 'tail_3', 'tail_4'] + \
       [f'{k}_{s}' for k in ('fleg', 'ffoot', 'hleg', 'hfoot') for s in 'LR']
def cand(name):
    if name.startswith('part_wing_'): s = name[-1]; return [f'wing_{s}_1', f'wing_{s}_2']
    if name == 'part_head': return ['head']
    if name == 'part_jaw': return ['jaw']
    if name == 'part_tail_tip': return ['tail_4']
    if name == 'part_chest': return ['body']
    if name == 'part_orbit': return ['orbit']
    return BODY

for ob in [o for o in bpy.data.objects if o.type == 'MESH' and o.name != 'floor_render']:
    P = np.array([ob.matrix_world @ v.co for v in ob.data.vertices])
    names = cand(ob.name)
    if len(names) == 1:
        g = ob.vertex_groups.new(name=names[0]); g.add(list(range(len(P))), 1.0, 'REPLACE')
    else:
        D = np.stack([segdist(P, *seg[n]) for n in names], 1)
        # legs must not grab torso verts: penalise by side
        for j, n in enumerate(names):
            if n[-1] in 'LR' and not n.startswith('wing'):
                sgn = 1 if n[-1] == 'L' else -1
                D[:, j] += np.where(P[:, 1] * sgn < 0.3 * K, 1.0, 0) + np.where(P[:, 2] > 2.4 * K, 0.6, 0)
        sig = (0.35 if names is BODY else 0.8) * K
        W = np.exp(-(D - D.min(1, keepdims=True)) ** 2 / sig ** 2)
        W[W < 0.08] = 0; W /= W.sum(1, keepdims=True)
        for j, n in enumerate(names):
            idx = np.where(W[:, j] > 0)[0]
            if len(idx) == 0: continue
            g = ob.vertex_groups.new(name=n)
            for i in idx: g.add([int(i)], float(W[i, j]), 'REPLACE')
    m = ob.modifiers.new('Armature', 'ARMATURE'); m.object = ao
    ob.parent = ao

# ---------- animations ----------
pb = ao.pose.bones
for b in pb: b.rotation_mode = 'QUATERNION'
def wrot(bname, axis, deg):
    """rotation about a world axis, expressed in the bone's local rest frame"""
    Rw = Matrix.Rotation(math.radians(deg), 3, V(axis))
    B = arm.bones[bname].matrix_local.to_3x3()
    return (B.inverted() @ Rw @ B).to_quaternion()

def make_action(name, frames, fn):
    ao.animation_data_create()
    act = bpy.data.actions.new(name); ao.animation_data.action = act
    for f in range(frames + 1):
        t = f / frames
        for b in pb: b.rotation_quaternion = (1, 0, 0, 0); b.location = (0, 0, 0); b.scale = (1, 1, 1)
        fn(t)
        for b in pb:
            b.keyframe_insert('rotation_quaternion', frame=f + 1)
            if b.name in ('root', 'body'):
                b.keyframe_insert('location', frame=f + 1); b.keyframe_insert('scale', frame=f + 1)
    act.use_fake_user = True
    trk = ao.animation_data.nla_tracks.new(); trk.name = name
    trk.strips.new(name, 1, act); ao.animation_data.action = None
    return act

TAU = 2 * math.pi
def rot(b, axis, deg):
    pb[b].rotation_quaternion = pb[b].rotation_quaternion @ wrot(b, axis, deg)

def spin(t):
    rot('orbit', (0, 0, 1), 360 * t)

def stance():
    # v5: pose de herói — pescoço erguido, peito à frente, pata dianteira esquerda avançada, asas menos abertas
    rot('neck_1', (0, 1, 0), -12); rot('head', (0, 1, 0), 6); rot('body', (0, 1, 0), -4)
    rot('fleg_L', (0, 1, 0), -28); rot('ffoot_L', (0, 1, 0), 38); rot('fleg_R', (0, 1, 0), 8); rot('ffoot_R', (0, 1, 0), -10)
    for s, sg in (('L', 1), ('R', -1)): rot(f'wing_{s}_1', (1, 0, 0), sg * 8)  # v9: asas mais abertas

def idle(t):
    spin(t); stance()
    br = math.sin(TAU * t)
    pb['body'].scale = (1, 1 + 0.025 * br, 1 + 0.03 * br)
    rot('neck_1', (0, 1, 0), -2 * br); rot('head', (0, 1, 0), 3 * math.sin(TAU * t + 0.6))
    puff = max(0, math.sin(TAU * (t - 0.45) * 2)) if 0.45 < t < 0.7 else 0  # smoke puff ~2.0s
    rot('jaw', (0, 1, 0), 10 * puff)
    for i in range(1, 5): rot(f'tail_{i}', (0, 0, 1), 6 * math.sin(TAU * t - i * 0.6))
    for s, sg in (('L', 1), ('R', -1)):
        rot(f'wing_{s}_1', (1, 0, 0), sg * 4 * br); rot(f'wing_{s}_2', (1, 0, 0), sg * 3 * math.sin(TAU * t - 0.5))

def walk(t):
    spin(t)
    a = math.sin(TAU * t)
    pb['root'].location = (0, 0, 0.08 * abs(math.cos(TAU * t)))
    for leg, ph in (('fleg_L', 0), ('hleg_R', 0), ('fleg_R', 0.5), ('hleg_L', 0.5)):
        s = math.sin(TAU * (t + ph)); rot(leg, (0, 1, 0), 22 * s)
        rot(leg.replace('leg', 'foot'), (0, 1, 0), -12 * max(0, -math.cos(TAU * (t + ph))))
    rot('body', (1, 0, 0), 2.5 * a); rot('neck_1', (0, 0, 1), -3 * a); rot('head', (0, 1, 0), 4 * math.sin(2 * TAU * t))
    for i in range(1, 5): rot(f'tail_{i}', (0, 0, 1), 9 * math.sin(TAU * t - i * 0.7))
    for s, sg in (('L', 1), ('R', -1)): rot(f'wing_{s}_1', (1, 0, 0), sg * 5 * math.sin(2 * TAU * t))

def happy(t):
    spin(t)
    e = math.sin(math.pi * min(1, t / 0.85)) if t < 0.85 else 0
    open_ = min(1, t / 0.25) if t < 0.7 else max(0, 1 - (t - 0.7) / 0.3)
    pb['root'].location = (0, 0, 0.35 * max(0, math.sin(TAU * t * 2)) * (1 if t < 0.5 else 0))
    rot('neck_1', (0, 1, 0), -14 * open_); rot('head', (0, 1, 0), -18 * open_)
    rot('jaw', (0, 1, 0), 24 * open_ * (0.8 + 0.2 * math.sin(TAU * t * 6)))
    for s, sg in (('L', 1), ('R', -1)):
        rot(f'wing_{s}_1', (1, 0, 0), sg * 10 * open_ + sg * 8 * math.sin(TAU * t * 3) * open_)
        rot(f'wing_{s}_2', (1, 0, 0), -sg * 22 * open_)
    for i in range(1, 5): rot(f'tail_{i}', (0, 0, 1), 14 * math.sin(TAU * t * 2 - i * 0.6))

def breath(t):
    spin(t)
    up = min(1, t / 0.25) if t < 0.25 else (max(0, 1 - (t - 0.25) / 0.1) if t < 0.35 else 0)
    fire = 1 if 0.25 <= t < 0.75 else (max(0, 1 - (t - 0.75) / 0.2) if t >= 0.75 else 0)
    rot('neck_1', (0, 1, 0), -12 * up + 10 * fire); rot('head', (0, 1, 0), -10 * up + 6 * fire)
    rot('jaw', (0, 1, 0), 28 * fire)
    pb['body'].scale = (1, 1 + 0.06 * up, 1 + 0.06 * up)
    for s, sg in (('L', 1), ('R', -1)): rot(f'wing_{s}_1', (1, 0, 0), -sg * 10 * up)

make_action('Idle', 96, idle); make_action('Walk', 43, walk); make_action('Happy', 72, happy); make_action('Breath', 58, breath)
for o in list(bpy.data.objects):
    if o.name == 'floor_render': bpy.data.objects.remove(o)
bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(f'{OUT}/dragon_rig.blend'))
bpy.ops.export_scene.gltf(filepath=os.path.abspath(f'{OUT}/molten-dragon-v4.glb'), export_format='GLB',
                          export_animations=True, export_animation_mode='ACTIONS', export_apply=False)
print('exported')
