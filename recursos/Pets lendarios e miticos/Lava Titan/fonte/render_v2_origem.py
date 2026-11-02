import bpy, sys, math, os
from mathutils import Vector
args = sys.argv[sys.argv.index('--') + 1:]
blend, outdir, res, samples = args[0], args[1], int(args[2]), int(args[3])
views = args[4].split(',') if len(args) > 4 else ['hero']
bpy.ops.wm.open_mainfile(filepath=blend)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = samples
sc.cycles.use_denoising = True
sc.render.resolution_x = res; sc.render.resolution_y = res
sc.render.film_transparent = False
sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Punchy'
sc.view_settings.exposure = 0.0

w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.012, 0.014, 0.022, 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0

# floor
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
fl = bpy.context.active_object
fm = bpy.data.materials.new('floor'); fm.use_nodes = True
fb = fm.node_tree.nodes['Principled BSDF']; fb.inputs['Base Color'].default_value = (0.05, 0.05, 0.065, 1); fb.inputs['Roughness'].default_value = 0.6
fl.data.materials.append(fm)

def area(name, loc, energy, size, color, target=(0, 0.3, 2.6)):
    l = bpy.data.lights.new(name, 'AREA'); l.energy = energy; l.size = size; l.color = color
    o = bpy.data.objects.new(name, l); sc.collection.objects.link(o); o.location = loc
    d = Vector(target) - Vector(loc); o.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
area('key', (-5, 7, 8), 2200, 5, (1.0, 0.95, 0.9))
area('fill', (7, 5, 3), 800, 6, (0.75, 0.82, 1.0))
area('rim', (2, -7, 7), 1100, 4, (0.8, 0.85, 1.0))

cam_d = bpy.data.cameras.new('cam'); cam = bpy.data.objects.new('cam', cam_d); sc.collection.objects.link(cam); sc.camera = cam
cam_d.lens = 60
VIEWS = {
    'hero': ((-5.2, 10.0, 4.6), (0.05, 0.2, 2.55)),
    'front': ((0, 11.5, 3.2), (0, 0.2, 2.6)),
    'back': ((6.0, -9.0, 6.0), (0, -0.2, 2.8)),
    'side': ((11.0, 1.0, 3.0), (0, 0.2, 2.6)),
}
for v in views:
    loc, tgt = VIEWS[v]
    cam.location = loc; cam.rotation_euler = (Vector(tgt) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    sc.render.filepath = os.path.join(outdir, f'render_{v}.png')
    bpy.ops.render.render(write_still=True)
    print('rendered', v)
