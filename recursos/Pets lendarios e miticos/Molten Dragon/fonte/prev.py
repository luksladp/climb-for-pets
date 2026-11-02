import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
from render import setup_scene, shoot
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=os.path.abspath('out/molten-dragon-v4.glb'))
arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
print('actions', [a.name for a in bpy.data.actions])
cam = setup_scene(int(os.environ.get('RES', 1000)), int(os.environ.get('SPP', 48)))
pose = os.environ.get('POSE')
if pose:
    arm.animation_data_create(); arm.animation_data.action = bpy.data.actions[pose]
    try: arm.animation_data.action_slot = bpy.data.actions[pose].slots[0]
    except Exception as e: print(e)
    bpy.context.scene.frame_set(int(os.environ.get('FRAME', 20)))
V = {'a': ((11, -15, 6.5), (-0.3, 0, 2.9)), 'b': ((-12, -12, 7.5), (-0.3, 0, 2.9)), 'f': ((14, 7, 5), (0, 0, 3.0)),
     'side': ((0, -20, 3.2), (-0.4, 0, 3.0)), 'head': ((7.5, -4.5, 6.2), (3.3, 0, 5.0))}
for v in os.environ.get('VIEWS', 'a').split(','):
    loc, tgt = V[v]; loc = tuple(0.82 * c for c in loc); tgt = tuple(0.82 * c for c in tgt)
    shoot(cam, loc, tgt, os.path.abspath(f"out/prev_{v}{'_' + pose if pose else ''}.png"), 35 if v == 'head' else 50)
