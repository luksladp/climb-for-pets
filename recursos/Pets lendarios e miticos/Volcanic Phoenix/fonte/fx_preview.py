"""Prévia dos efeitos no render do Blender (não é o jogo): cada emissor da camada ambiente vira alguns
planos voltados à câmera com um quadro do flipbook entregue em ../vfx. Usado por render.py --fx."""
import math
import os

import bpy
from mathutils import Vector

VFX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "vfx")


def frame_mat(name, sheet, grid, idx, strength=2.5, tint=None):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    uv = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    col, row = idx % grid, idx // grid
    mp.inputs["Scale"].default_value = (1 / grid, 1 / grid, 1)
    mp.inputs["Location"].default_value = (col / grid, 1 - (row + 1) / grid, 0)
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(os.path.join(VFX, sheet), check_existing=True)
    tex.extension = "CLIP"
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Strength"].default_value = strength
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(uv.outputs["UV"], mp.inputs["Vector"])
    nt.links.new(mp.outputs[0], tex.inputs["Vector"])
    if tint:  # cor do Beam (Color) aplicada sobre a textura
        mul = nt.nodes.new("ShaderNodeMix")
        mul.data_type = "RGBA"
        mul.blend_type = "MULTIPLY"
        mul.inputs["Factor"].default_value = 1.0
        mul.inputs["B"].default_value = tint
        nt.links.new(tex.outputs["Color"], mul.inputs["A"])
        nt.links.new(mul.outputs["Result"], em.inputs["Color"])
    else:
        nt.links.new(tex.outputs["Color"], em.inputs["Color"])
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    return m


def card(scene, name, loc, size, mat):
    bpy.ops.mesh.primitive_plane_add(size=size, location=loc)
    ob = bpy.context.active_object
    ob.name = name
    ob.data.materials.append(mat)
    ob["billboard"] = True
    ob.visible_shadow = False
    return ob


def add(scene, out):
    # posições = âncoras FX_* do rig (rest pose)
    a = {o.name: o.matrix_world.translation.copy() for o in scene.objects if o.name.startswith("FX_")}
    # rodada 3: chamas de verdade nas pontas das asas, na crista e na cauda (flipbook flame_4x4)
    for k, (n, size, f, off) in enumerate([("FX_WingTip.R", 3.4, 2, (-0.3, 0, -0.4)),
                                           ("FX_WingTip.L", 3.4, 9, (0.3, 0, -0.4)),
                                           ("FX_Crest", 2.2, 5, (0, -0.1, -0.6)), ("FX_TailTip", 3.4, 12, (0, 0.5, 0.0))]):
        card(scene, f"fx_flame{k}", a[n] + Vector(off) + Vector((0, 0, 0.4 * size)), size,
             frame_mat(f"m_flame{k}", "flame_4x4.png", 4, f, 3.0))
    for k, (dx, dz, f) in enumerate([(0.3, -0.2, 2), (-0.5, -0.9, 6)]):  # ember_fall: ~2 vivas
        card(scene, f"fx_ember{k}", a["FX_TailEmber"] + Vector((dx, 0, dz)), 0.9,
             frame_mat(f"m_ember{k}", "ember_feather_4x4.png", 4, f))
    # rodada 4: anel de brasas no chão (Beam deitado com ground_ring.png), centrado sob o corpo
    bpy.ops.mesh.primitive_plane_add(size=6.4, location=(0, -0.1, 0.03))
    ring = bpy.context.active_object
    ring.name = "fx_ground_ring"
    ring.data.materials.append(frame_mat("m_ring", "ground_ring.png", 1, 0, 4.0, (1.0, 0.2, 0.012, 1)))
    ring.visible_shadow = False
    # luz real: 1 PointLight no peito (orçamento: ≤ 1 luz)
    ld = bpy.data.lights.new("core_light", "POINT")
    ld.energy = 16  # rodada 17: sem ponto claro no peito
    ld.color = (1.0, 0.5, 0.14)
    ob = bpy.data.objects.new("core_light", ld)
    ob.location = a["FX_Core"] + Vector((0, 0.6, 0))
    scene.collection.objects.link(ob)
