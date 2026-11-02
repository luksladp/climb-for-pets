"""Folha de conferência dos clipes: 4 quadros por clipe, vista 3/4 (render do Blender, não é o jogo).
Uso: python anim_check.py <pasta com VolcanicPhoenix.blend>"""
import math
import os
import sys

import bpy
from mathutils import Vector

OUT = os.path.abspath(sys.argv[-1])
bpy.ops.wm.open_mainfile(filepath=os.path.join(OUT, "VolcanicPhoenix.blend"))
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.samples = 8
sc.render.film_transparent = True
sc.render.resolution_x = sc.render.resolution_y = 320
w = bpy.data.worlds.new("w")
sc.world = w
w.use_nodes = True
w.node_tree.nodes["Background"].inputs[1].default_value = 1.2
cd = bpy.data.cameras.new("c")
cd.type = "ORTHO"
cd.ortho_scale = 8.5
cam = bpy.data.objects.new("c", cd)
sc.collection.objects.link(cam)
sc.camera = cam
tgt = Vector((0, -0.2, 3.0))
a = math.radians(35)
cam.location = tgt + Vector((math.sin(a) * 14, math.cos(a) * 14, 2))
cam.rotation_euler = (tgt - cam.location).to_track_quat("-Z", "Y").to_euler()
rig = bpy.data.objects["VolcanicPhoenix_Rig"]
for tr in rig.animation_data.nla_tracks:
    tr.mute = True
os.makedirs(os.path.join(OUT, "anim"), exist_ok=True)
for act in bpy.data.actions:
    rig.animation_data.action = act
    n = int(act.frame_range[1])
    for k in range(4):
        sc.frame_set(round(n * k / 4))
        sc.render.filepath = os.path.join(OUT, "anim", f"{act.name}_{k}.png")
        bpy.ops.render.render(write_still=True)
