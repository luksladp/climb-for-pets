# Screenshots de verificação (render do Blender, não é o jogo): frente, 3/4, lado, sem e com efeitos, + ícone 128.
# Uso: python3 shots.py <glb> <pasta_vfx> <saida>
import sys, os, math, bpy
from mathutils import Vector
from PIL import Image
GLB, VFX, OUT = [os.path.abspath(a) for a in sys.argv[1:4]]
os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
if arm.animation_data: arm.animation_data.action = None
# v5: prints no 1º quadro do Idle (a pose que o jogador vê)
arm.animation_data_create(); arm.animation_data.action = bpy.data.actions['Idle']
try: arm.animation_data.action_slot = bpy.data.actions['Idle'].slots[0]
except Exception as e: print(e)
bpy.context.scene.frame_set(1)
for t in list(arm.animation_data.nla_tracks): t.mute = True
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.samples = int(os.environ.get('SPP', 64)); sc.cycles.use_denoising = True
sc.render.film_transparent = True; sc.view_settings.view_transform = 'Standard'
sc.render.resolution_x = sc.render.resolution_y = int(os.environ.get('RES', 1024))
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs[0].default_value = (0.42, 0.44, 0.48, 1)  # luz ambiente neutra
def light(kind, loc, energy, size=5, col=(1, 1, 1)):
    ld = bpy.data.lights.new(kind, kind); ld.energy = energy; ld.color = col
    if kind == 'AREA': ld.size = size
    o = bpy.data.objects.new(kind, ld); sc.collection.objects.link(o); o.location = loc
    o.rotation_euler = (Vector((0, 0, 2.5)) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
light('SUN', (6, -5, 10), 3.2, col=(1, 0.97, 0.92))
light('AREA', (-7, 6, 6), 900, 6, (0.85, 0.85, 1.0))
# v4: luz de borda quente (rim) para o pet não sumir no fundo escuro
light('AREA', (-9, -3, 7), 2600, 4, (1.0, 0.62, 0.32))
light('AREA', (-6, 8, 3), 1400, 4, (1.0, 0.55, 0.3))
light('AREA', (-4, 0, 9), 1800, 5, (0.9, 0.92, 1.0))  # v9: rim claro para o fundo escuro
cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); sc.collection.objects.link(cam); sc.camera = cam
cam.data.type = 'ORTHO'

def bone_pos(n):
    return arm.matrix_world @ arm.pose.bones[n].head

def frame(path):
    im = Image.open(path).convert('RGBA'); return im

def fx_plane(name, img, frame_idx, loc, size, facing=True, alpha=1.0, strength=2.0, opacity=1.0):
    sheet = Image.open(os.path.join(VFX, img)); q = sheet.width // 4
    fx, fy = frame_idx % 4, frame_idx // 4
    tile = sheet.crop((fx * q, fy * q, fx * q + q, fy * q + q))
    p = f'/tmp/md/shots/{name}.png'; tile.save(p)
    bpy.ops.mesh.primitive_plane_add(size=size, location=loc); pl = bpy.context.active_object; pl.name = 'fx_' + name
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear()
    tx = nt.nodes.new('ShaderNodeTexImage'); tx.image = bpy.data.images.load(p)
    em = nt.nodes.new('ShaderNodeEmission'); em.inputs['Strength'].default_value = strength * alpha
    tr = nt.nodes.new('ShaderNodeBsdfTransparent'); mix = nt.nodes.new('ShaderNodeMixShader')
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    nt.links.new(tx.outputs['Color'], em.inputs['Color'])
    mul = nt.nodes.new('ShaderNodeMath'); mul.operation = 'MULTIPLY'; mul.inputs[1].default_value = opacity
    nt.links.new(tx.outputs['Alpha'], mul.inputs[0]); nt.links.new(mul.outputs[0], mix.inputs[0])
    nt.links.new(tr.outputs[0], mix.inputs[1]); nt.links.new(em.outputs[0], mix.inputs[2]); nt.links.new(mix.outputs[0], out.inputs[0])
    pl.data.materials.append(m); pl.visible_shadow = False
    if facing:
        c = pl.constraints.new('TRACK_TO'); c.target = cam; c.track_axis = 'TRACK_Z'; c.up_axis = 'UP_Y'
    return pl

FX = []
def add_fx():
    g = bone_pos('FX_Ground'); FX.append(fx_plane('ring', 'anel-brasas-chao_4x4.png', 3, g + Vector((0, 0, 0.03)), 7.0, facing=False))
    b = bone_pos('FX_Back')
    for i, (dx, dy) in enumerate(((1.0, 0), (0.1, 0), (-0.8, 0), (-1.6, 0))):
        FX.append(fx_plane(f'flame{i}', 'chama-aura_4x4.png', (i * 5) % 16, b + Vector((dx, dy, 0.95)), 2.3, strength=1.0))  # r14: chama laranja, presa ao dorso
    FX.append(fx_plane('crown', 'brilho-coroa_4x4.png', 7, bone_pos('FX_Crown') + Vector((0, 0, 0.15)), 1.3))
    FX.append(fx_plane('furnace', 'pulso-fornalha_4x4.png', 3, bone_pos('FX_Furnace') + Vector((0.25, 0, 0)), 1.3))
    FX.append(fx_plane('smoke', 'fumaca-narina_4x4.png', 6, bone_pos('FX_Nostril') + Vector((1.1, 0, 0.9)), 1.3, alpha=1.0, strength=1.0, opacity=0.35))  # r16: fumaça translúcida, acima e à frente do focinho, longe dos olhos
    for i in range(6):
        a = i / 6 * 2 * math.pi
        FX.append(fx_plane(f'ember{i}', 'brasa_4x4.png', i * 2, Vector((math.cos(a) * 3.0, math.sin(a) * 3.0, 0.6 + 1.6 * (i % 3) / 2)), 0.45))

VIEWS = {'frente': (math.radians(0), 16), 'tres_quartos': (math.radians(-40), 14), 'lado': (math.radians(-90), 4)}
def shoot(tag):
    for v, (yaw, pitch) in VIEWS.items():
        d = Vector((math.cos(yaw), math.sin(yaw), math.tan(math.radians(pitch))))
        tgt = Vector((-0.1, 0, 2.6)); cam.location = tgt + d.normalized() * 30
        cam.rotation_euler = (tgt - cam.location).to_track_quat('-Z', 'Y').to_euler()
        cam.data.ortho_scale = 7.2 if v == 'frente' else 10.2
        sc.render.filepath = f'{OUT}/{v}{tag}.png'; bpy.ops.render.render(write_still=True)
# v12 (rodada 10): ícone com o pet inteiro a 3/4 de frente, recortado pelo próprio contorno com
# margem de 9%; sem contorno claro nem luz de recorte branca (o revisor viu halo no fundo escuro);
# luz de recorte quente por trás e as fendas acesas separam o corpo do fundo escuro
def icon():
    hid = [o for o in bpy.data.objects if o.name.startswith('part_orbit')]
    for o in hid: o.hide_render = True
    rim = bpy.data.lights.new('rim_icon', 'AREA'); rim.energy = 3600; rim.size = 5; rim.color = (1.0, 0.72, 0.42)  # r15: contraluz mais forte
    ro = bpy.data.objects.new('rim_icon', rim); sc.collection.objects.link(ro); ro.location = (-7, 5, 8)
    ro.rotation_euler = (Vector((0.5, 0, 3.0)) - ro.location).to_track_quat('-Z', 'Y').to_euler()
    # r11: câmera em perspectiva perto da frente, para a cabeça (mais perto) ficar maior com o pet inteiro
    yaw, pitch = math.radians(-12), 8  # r17: quase de frente, os dois olhos separados
    d = Vector((math.cos(yaw), math.sin(yaw), math.tan(math.radians(pitch))))
    tgt = Vector((0.6, 0, 3.4))
    cam.data.type = 'PERSP'; cam.data.lens = 24
    cam.location = tgt + d.normalized() * float(os.environ.get('ICON_DIST', 11.5))
    cam.rotation_euler = (tgt - cam.location).to_track_quat('-Z', 'Y').to_euler()
    res = sc.render.resolution_x; sc.render.resolution_x = sc.render.resolution_y = 768
    sc.render.filepath = f'{OUT}/_icone_raw.png'; bpy.ops.render.render(write_still=True)
    sc.render.resolution_x = sc.render.resolution_y = res
    for o in hid: o.hide_render = False
    bpy.data.objects.remove(ro); cam.data.type = 'ORTHO'
    ic = Image.open(f'{OUT}/_icone_raw.png').convert('RGBA')
    x0, y0, x1, y1 = ic.split()[3].point(lambda v: 255 if v > 24 else 0).getbbox()
    side = max(x1 - x0, y1 - y0); pad = int(side * 0.05); side += 2 * pad  # r15: pet enche ~90% do quadro
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    sq = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    sq.paste(ic.crop((cx - side // 2, cy - side // 2, cx - side // 2 + side, cy - side // 2 + side)), (0, 0))
    sq.resize((128, 128), Image.LANCZOS).save(f'{OUT}/icone_128.png')
if os.environ.get('ICON_ONLY'):
    icon(); raise SystemExit
shoot('')
icon()
add_fx(); shoot('_fx')
