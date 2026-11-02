import bpy, math
from mathutils import Vector

def setup_scene(res=900, samples=48):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'; sc.cycles.samples = samples; sc.cycles.use_denoising = True
    sc.cycles.device = 'CPU'
    sc.render.resolution_x = res; sc.render.resolution_y = res
    sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'Medium High Contrast'
    w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
    w.node_tree.nodes['Background'].inputs[0].default_value = (0.035, 0.04, 0.08, 1)
    w.node_tree.nodes['Background'].inputs[1].default_value = 1.0
    # floor
    bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 0, 0))
    fl = bpy.context.active_object; fl.name = 'floor_render'
    m = bpy.data.materials.new('floor'); m.use_nodes = True
    m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.09, 0.095, 0.14, 1)
    m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.6
    fl.data.materials.append(m)
    def light(name, loc, energy, size, col=(1, 1, 1)):
        ld = bpy.data.lights.new(name, 'AREA'); ld.energy = energy; ld.size = size; ld.color = col
        o = bpy.data.objects.new(name, ld); sc.collection.objects.link(o); o.location = loc
        d = Vector((0, 0, 2.5)) - Vector(loc); o.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    light('key', (6, -8, 10), 1900, 6, (1, 0.95, 0.9))
    light('rim', (-8, 6, 7), 1600, 6, (0.75, 0.7, 1.0))
    light('fill', (8, -2, 3), 700, 8, (0.8, 0.85, 1.0))
    cam = bpy.data.cameras.new('cam'); cam.lens = 50
    co = bpy.data.objects.new('cam', cam); sc.collection.objects.link(co); sc.camera = co
    # glow in compositor
    sc.use_nodes = True if hasattr(sc, 'use_nodes') else None
    try:
        tree = bpy.data.node_groups.new('comp', 'CompositorNodeTree'); sc.compositing_node_group = tree
        rl = tree.nodes.new('CompositorNodeRLayers'); gl = tree.nodes.new('CompositorNodeGlare')
        out = tree.nodes.new('NodeGroupOutput'); tree.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
        try:
            gl.inputs['Type'].default_value = 'Fog Glow'; gl.inputs['Threshold'].default_value = 1.0
            gl.inputs['Strength'].default_value = 0.6; gl.inputs['Size'].default_value = 0.5
        except Exception as e: print('glare opts', e)
        tree.links.new(rl.outputs['Image'], gl.inputs['Image']); tree.links.new(gl.outputs['Image'], out.inputs[0])
    except Exception as e:
        print('compositor skipped', e)
    return co

def shoot(cam, loc, target, path, lens=50):
    cam.data.lens = lens; cam.location = loc
    d = Vector(target) - Vector(loc); cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
