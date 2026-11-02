"""Renders do Blender (não é o jogo): frente, 3/4, lado e ícone 128 px, com fundo transparente.

Uso: python render.py <pasta com VolcanicPhoenix.blend> [--fx] [--pose Idle:30]
Saída: <pasta>/renders/{frente,tres_quartos,lado}[_fx].png e icone_512.png (o ícone de 128 px é o 512 recortado e reduzido)
"""
import math
import os
import sys

import bpy
from mathutils import Vector

args = sys.argv[1:]
OUT = os.path.abspath(args[0])
FX = "--fx" in args
POSE = None
if "--pose" in args:
    POSE = args[args.index("--pose") + 1]
NAME = "VolcanicPhoenix"
bpy.ops.wm.open_mainfile(filepath=os.path.join(OUT, NAME + ".blend"))
scene = bpy.context.scene
os.makedirs(os.path.join(OUT, "renders"), exist_ok=True)

rig = bpy.data.objects[NAME + "_Rig"]
if POSE:
    act, fr = POSE.split(":")
    for tr in rig.animation_data.nla_tracks:
        tr.mute = True
    rig.animation_data.action = bpy.data.actions[act]
    scene.frame_set(int(fr))

scene.render.engine = "CYCLES"
scene.cycles.samples = 64
scene.cycles.use_denoising = True
scene.render.film_transparent = True
scene.render.resolution_x = scene.render.resolution_y = 1024
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"

world = bpy.data.worlds.new("w")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.55, 0.57, 0.62, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.55


def light(name, kind, rot, energy, color=(1, 1, 1)):
    ld = bpy.data.lights.new(name, kind)
    ld.energy = energy
    ld.color = color
    if kind == "SUN":
        ld.angle = math.radians(8)
    ob = bpy.data.objects.new(name, ld)
    scene.collection.objects.link(ob)
    ob.rotation_euler = [math.radians(a) for a in rot]
    return ob


light("key", "SUN", (50, 0, 35), 3.2, (1.0, 0.97, 0.92))
light("fill", "SUN", (65, 0, -140), 0.9, (0.85, 0.9, 1.0))
light("rim", "SUN", (-60, 0, 180), 2.2, (1.0, 0.62, 0.38))  # borda quente: separa do fundo escuro

if FX:
    # prévia dos efeitos: os mesmos flipbooks entregues, em planos emissivos voltados à câmera
    import fx_preview
    fx_preview.add(scene, OUT)

cam_d = bpy.data.cameras.new("cam")
cam_d.type = "ORTHO"
cam_d.ortho_scale = 9.0  # rodada 10: cabeça maior, crista inteira no quadro
cam = bpy.data.objects.new("cam", cam_d)
scene.collection.objects.link(cam)
scene.camera = cam
target = Vector((0, -0.1, 3.85))

VIEWS = {"frente": 0, "tres_quartos": 40, "lado": 90}
suffix = "_fx" if FX else ""
for vname, ang in VIEWS.items():
    a = math.radians(ang)
    d = 15.5
    cam.location = target + Vector((math.sin(a) * d, math.cos(a) * d, 1.2))
    cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
    for ob in scene.objects:
        if ob.get("billboard"):
            ob.rotation_euler = (cam.location - ob.location).to_track_quat("Z", "Y").to_euler()
    scene.render.filepath = os.path.join(OUT, "renders", f"{vname}{suffix}.png")
    bpy.ops.render.render(write_still=True)

if not FX:
    # rodada 10: pet inteiro a 3/4 de frente com margem; a cabeça de ~1/3 da altura já deixa os olhos grandes
    a = math.radians(32)
    icon_t = Vector((0, 0.2, 4.0))
    cam.location = icon_t + Vector((math.sin(a) * 13, math.cos(a) * 13, 1.0))
    cam_d.ortho_scale = 8.6
    # rim light extra só no ícone: contorno quente dos dois lados para destacar no fundo escuro do inventário
    light("rim_icon_r", "SUN", (-70, 0, 150), 9.0, (0.85, 0.9, 1.0))  # rodada 16: borda fria dos dois lados (contorno no fundo escuro)  # rodada 9: contorno aceso do tronco
    light("rim_icon_l", "SUN", (-70, 0, -150), 9.0, (0.85, 0.9, 1.0))  # rodada 14: borda fria separa do fundo escuro
    target = icon_t
    cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
    scene.render.resolution_x = scene.render.resolution_y = 512
    scene.render.filepath = os.path.join(OUT, "renders", "icone_512.png")
    bpy.ops.render.render(write_still=True)
    # ícone 128: recorta a borda transparente, deixa 8% de margem e reduz
    from PIL import Image
    im = Image.open(scene.render.filepath).convert("RGBA")
    im = im.crop(im.getbbox())
    side = int(max(im.size) / 0.9)  # rodada 14: margem de 5%
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    sq.resize((128, 128), Image.LANCZOS).save(os.path.join(OUT, "renders", "icone_128.png"))
print("OK renders")
