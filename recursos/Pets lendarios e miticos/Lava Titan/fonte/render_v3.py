# Render do Lava Titan v3 no Blender (não é o jogo): fundo neutro, pet ocupando o quadro.
# uso: python render_v3.py <blend> <saida_dir> <res> <amostras> <vistas> [--fx] [--clip Nome --frame N]
import bpy, sys, os
from mathutils import Vector
a = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:]
blend, outdir, res, samples, views = a[0], a[1], int(a[2]), int(a[3]), a[4].split(',')
fx = '--fx' in a
bpy.ops.wm.open_mainfile(filepath=blend)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = samples; sc.cycles.use_denoising = True
sc.render.resolution_x = sc.render.resolution_y = res
sc.view_settings.view_transform = 'Standard'
rig = bpy.data.objects['LavaTitan_Rig']
if '--clip' in a:
    name, f = a[a.index('--clip') + 1], int(a[a.index('--frame') + 1])
    for tr in rig.animation_data.nla_tracks: tr.mute = tr.name != name
    sc.frame_set(f)
else:
    for tr in rig.animation_data.nla_tracks: tr.mute = True
    sc.frame_set(0)
# sem efeitos: magma só com a cor; com efeitos: um pouco mais de brilho, sem estourar para amarelo
m = bpy.data.materials['LavaTitan_Magma']; m.node_tree.nodes['Principled BSDF'].inputs['Emission Strength'].default_value = 1.6 if fx else 1.0
bpy.data.materials['LavaTitan_Eyes'].node_tree.nodes['Principled BSDF'].inputs['Emission Strength'].default_value = 3.0   # olhos: o ponto mais forte
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.42, 0.44, 0.47, 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.9
bpy.ops.mesh.primitive_plane_add(size=60)
fl = bpy.context.active_object; fm = bpy.data.materials.new('floor'); fm.use_nodes = True
fm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.36, 0.37, 0.39, 1)
fl.data.materials.append(fm)
sun = bpy.data.lights.new('sun', 'SUN'); sun.energy = 3.2; sun.angle = 0.2
so = bpy.data.objects.new('sun', sun); sc.collection.objects.link(so); so.rotation_euler = (0.75, 0.15, 2.6)
FXDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'vfx')
# efeitos ligados: 1 quadro de cada flipbook num plano voltado para a câmera, no ponto do emissor
FX = [('LavaTitan_crater_embers_4x4.png', 4, 6, (0, -1.25, 4.05), 1.4, False),
      ('LavaTitan_magma_drip_4x4.png', 4, 5, (2.36, 1.30, 0.45), 0.55, False),
      ('LavaTitan_magma_drip_4x4.png', 4, 9, (-2.36, 1.30, 0.40), 0.55, False),
      ('LavaTitan_ground_aura_4x4.png', 4, 3, (0, 0.2, 0.02), 8.0, True)]   # True: deitado no chão
fx_planes = []
if fx:
    from PIL import Image
    for k, (sheet, g, fr, pos, size, flat) in enumerate(FX):
        im = Image.open(os.path.join(FXDIR, sheet)); L = im.width // g
        crop = im.crop(((fr % g) * L, (fr // g) * L, (fr % g + 1) * L, (fr // g + 1) * L))
        fp = f'/tmp/lt_fx_{k}.png'; crop.save(fp)
        bpy.ops.mesh.primitive_plane_add(size=size, location=pos); pl = bpy.context.active_object
        m = bpy.data.materials.new(f'fx{k}'); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear()
        t = nt.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(fp)
        e = nt.nodes.new('ShaderNodeEmission'); e.inputs['Strength'].default_value = 1.6 if flat else 1.3
        tr = nt.nodes.new('ShaderNodeBsdfTransparent'); mx = nt.nodes.new('ShaderNodeMixShader')
        o = nt.nodes.new('ShaderNodeOutputMaterial')
        nt.links.new(t.outputs['Color'], e.inputs['Color']); nt.links.new(t.outputs['Alpha'], mx.inputs[0])
        nt.links.new(tr.outputs[0], mx.inputs[1]); nt.links.new(e.outputs[0], mx.inputs[2]); nt.links.new(mx.outputs[0], o.inputs['Surface'])
        pl.data.materials.append(m); pl.visible_shadow = False
        if not flat: fx_planes.append(pl)
    pt = bpy.data.lights.new('crater', 'POINT'); pt.energy = 120; pt.color = (1.0, 0.48, 0.12)
    po = bpy.data.objects.new('crater', pt); sc.collection.objects.link(po); po.location = (0, -1.2, 3.7)
rim = bpy.data.lights.new('rim', 'SUN'); rim.energy = 2.2; rim.color = (1.0, 0.62, 0.35); rim.angle = 0.3
ro = bpy.data.objects.new('rim', rim); sc.collection.objects.link(ro); ro.rotation_euler = (-1.0, 0.0, 0.5)   # luz de borda quente, por trás
cam_d = bpy.data.cameras.new('cam'); cam_d.type = 'ORTHO'; cam_d.ortho_scale = 6.6
cam = bpy.data.objects.new('cam', cam_d); sc.collection.objects.link(cam); sc.camera = cam
T = Vector((0, 0.1, 2.75))
V = {'frente': Vector((0, 1, 0.22)), 'tres_quartos': Vector((0.7, 0.72, 0.2)), 'lado': Vector((1, 0, 0.08)),
     'costas': Vector((-0.4, -1, 0.35)), 'icone': Vector((0.50, 0.86, 0.18))}
for v in views:
    d = V[v].normalized(); cam.location = (T + Vector((0, 0, 0.0)) if v == 'icone' else T) + d * 20   # ícone: corpo inteiro com folga (o recorte e a margem ficam no icone.py)
    cam.rotation_euler = (-d).to_track_quat('-Z', 'Y').to_euler()
    for pl in fx_planes: pl.rotation_euler = cam.rotation_euler
    cam_d.ortho_scale = 9.0 if v == 'icone' else 6.9
    sc.render.film_transparent = True; fl.hide_render = True   # fundo transparente (a folha do comparar.py põe o fundo)
    tag = ('_fx' if fx else '') + (f"_{a[a.index('--clip') + 1]}{a[a.index('--frame') + 1]}" if '--clip' in a else '')
    sc.render.filepath = os.path.join(outdir, f'{v}{tag}.png'); bpy.ops.render.render(write_still=True)
