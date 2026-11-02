# angular faceted head (loft), jaw slightly open with glowing mouth; exec'd from parts.py
mb = G('head')
PIV = Vec((2.8, 0, 5.2)); PITCH = math.radians(8)
rotH = Mat.Rotation(PITCH, 3, 'Y')   # +Y rotation tips snout down
def T(p, piv=PIV, rot=None):
    return piv + (rot or rotH) @ (Vec(p) - piv)
# sections: x, [(y,z) left half from top-center to mouth corner], palate z
UP = [
    (2.55, [(0, 5.95), (0.5, 5.9), (0.66, 5.4), (0.52, 4.98)], 4.95),
    (3.15, [(0, 6.05), (0.6, 5.95), (0.7, 5.35), (0.52, 4.96)], 4.96),
    (3.7, [(0, 5.88), (0.66, 5.85), (0.6, 5.3), (0.46, 4.97)], 4.97),
    (4.15, [(0, 5.58), (0.56, 5.52), (0.62, 5.2), (0.52, 4.98)], 4.98),
    (4.65, [(0, 5.45), (0.46, 5.4), (0.5, 5.14), (0.44, 4.99)], 4.99),
    (5.05, [(0, 5.32), (0.34, 5.28), (0.36, 5.08), (0.32, 4.99)], 4.99),
]
# r13: canto de cima chanfrado (o focinho deixa de ser caixa)
UP = [(x, [h[0], (h[1][0] * 0.82, h[1][1] + 0.01), ((h[1][0] + h[2][0]) / 2 + 0.05, (h[1][1] + h[2][1]) / 2 + 0.1), h[2], h[3]], bz) for x, h, bz in UP]

# r12: cabeça com o material do corpo: cada faceta vira 4 placas chanfradas com fresta de lava
_PR = random.Random(12)
def plated_quad(mb, ids, mat, inner):
    P = [Vec(mb.v[i]) for i in ids]
    c = sum(P, Vec()) / 4
    nrm = (P[1] - P[0]).cross(P[3] - P[0]).normalized()
    if nrm.dot(c - inner) < 0: nrm = -nrm
    mb.face(ids, 'magma_body' if _PR.random() < 0.6 else 'obsidian_dark')  # fundo (vira a fresta); ~60% aceso, como o corpo
    def bl(u, v): return P[0].lerp(P[1], u).lerp(P[3].lerp(P[2], u), v)
    # divisão irregular (1, 2 ou 3 placas por lado, cortes tortos) para não virar azulejo
    nu, nv = _PR.choice((1, 2, 2, 3)), _PR.choice((1, 2, 2))
    us = [0] + sorted(_PR.uniform(0.25, 0.75) if nu == 2 else (k + _PR.uniform(-0.12, 0.12)) / nu for k in range(1, nu)) + [1]
    vs = [0] + sorted(_PR.uniform(0.25, 0.75) if nv == 2 else (k + _PR.uniform(-0.12, 0.12)) / nv for k in range(1, nv)) + [1]
    sk = _PR.uniform(-0.15, 0.15)
    for a in range(nu):
        for b in range(nv):
            def g(ia, ib):
                u = us[ia] + (sk * (vs[ib] - 0.5) if 0 < ia < nu else 0)
                return bl(min(max(u, 0), 1), vs[ib])
            q = [g(a, b), g(a + 1, b), g(a + 1, b + 1), g(a, b + 1)]
            qc = sum(q, Vec()) / 4
            h = 0.035 + _PR.uniform(0, 0.02)
            bot = [mb.add_v(x + (qc - x) * 0.06 + nrm * 0.004) for x in q]
            top = [mb.add_v(x + (qc - x) * 0.14 + nrm * h) for x in q]
            mid = mb.add_v(qc + nrm * (h + 0.012))
            for k in range(4):
                k2 = (k + 1) % 4
                mb.face([bot[k], bot[k2], top[k2], top[k]], 'obsidian_edge')
                mb.face([top[k], top[k2], mid], mat)

def loft(mb, secs, mats_fn, close_mat, xform, inner=None):
    rings = []
    for x, half, bz in secs:
        pts = [(y, z) for y, z in reversed(half)] + [(-y, z) for y, z in half[1:]]
        pts = [(y * (1 + R.uniform(-0.04, 0.04)), z + R.uniform(-0.02, 0.02)) if y != 0 else (y, z) for y, z in pts]
        rings.append([mb.add_v(xform(Vec((x + R.uniform(-0.03, 0.03), y, z)))) for y, z in pts])
    n = len(rings[0])
    for i in range(len(rings) - 1):
        for k in range(n - 1):
            q = [rings[i][k], rings[i][k + 1], rings[i + 1][k + 1], rings[i + 1][k]]
            m_ = mats_fn(i, k, n)
            mb.face(q, 'SKIN' if m_ in ('obsidian', 'obsidian_edge') else m_)
        # bottom (palate / jaw top) between the two mouth corners
        mb.face([rings[i][n - 1], rings[i][0] if False else rings[i][n - 1], rings[i + 1][n - 1]][:0] or
                [rings[i][n - 1], rings[i + 1][n - 1], rings[i + 1][0], rings[i][0]], close_mat)
    mb.face(rings[0][::-1], 'obsidian_dark'); mb.face(rings[-1], 'obsidian')
    return rings

def up_mat(i, k, n):
    return 'obsidian'  # r12: tudo em placas, mesmo tom do corpo
uring = loft(mb, UP, up_mat, 'mouth_in', T, inner=T(Vec((3.6, 0, 5.35))))  # v12: céu da boca em lava escura  # v10: interior escuro  # v7: interior da boca aceso  # v6: céu da boca escuro

# jaw: open ~12 deg around hinge (own group so it can animate)
mb_head = mb; mb = G('jaw')
JPIV = Vec((2.85, 0, 4.95)); rotJ = rotH @ Mat.Rotation(math.radians(17), 3, 'Y')  # v12: boca mais aberta
LO = [  # v12: mandíbula mais funda, com queixo
    (2.75, [(0.52, 4.93), (0.48, 4.58), (0, 4.4)]),
    (3.4, [(0.5, 4.93), (0.44, 4.55), (0, 4.42)]),
    (4.0, [(0.44, 4.93), (0.39, 4.58), (0, 4.48)]),
    (4.55, [(0.44, 4.93), (0.38, 4.62), (0, 4.52)]),
    (4.95, [(0.32, 4.93), (0.28, 4.7), (0, 4.64)]),
]
LO = [(x, [h[0], h[1], (h[1][0] * 0.55, h[1][1] - (h[1][1] - h[2][1]) * 0.75), h[2]]) for x, h in LO]  # r13: queixo chanfrado
def xj(p): return T(p, JPIV, rotJ)
jr = []
for x, half in LO:
    pts = half + [(-y, z) for y, z in reversed(half[:-1])]
    jr.append([mb.add_v(xj(Vec((x, y, z)))) for y, z in pts])
n = len(jr[0])
for i in range(len(jr) - 1):
    for k in range(n - 1):
        mb.face([jr[i][k + 1], jr[i][k], jr[i + 1][k], jr[i + 1][k + 1]], 'SKIN')  # r13: placas orgânicas por cima
    mb.face([jr[i][0], jr[i][n - 1], jr[i + 1][n - 1], jr[i + 1][0]], 'mouth_in')
mb.face(jr[0], 'obsidian_dark'); mb.face(jr[-1][::-1], 'obsidian')
# v12: língua em lava escura dentro da mandíbula
sphere(mb, xj(Vec((3.6, 0, 4.88))), 0.66, 'tongue', scale=(1.0, 0.5, 0.26), seg=12, rings=6)  # r13: língua com volume
jb = mb; mb = mb_head
# mouth interior glow block (throat)
sphere(mb, T(Vec((2.85, 0, 4.86))), 0.5, 'magma', scale=(1.0, 0.95, 0.66))  # r15: garganta acesa, a boca escurece para a frente
sphere(mb, T(Vec((3.05, 0, 4.86))), 0.5, 'lava_dark', scale=(0.6, 0.98, 0.62))  # r13: brasa que escurece para a frente  # v10: brilho vem da garganta  # v8: brasa baixa e recuada  # v6: brasa só no fundo da garganta


def organic_plates(g, part, inner, avoid=()):
    import bmesh as _bm
    sk = MB(); idx = [i for i, m_ in enumerate(g.m) if m_ == 'SKIN']
    for i in idx: sk.face([sk.add_v(g.v[j]) for j in g.f[i]], 'obsidian')
    me_ = bpy.data.meshes.new('skin_' + part); me_.from_pydata(sk.v, [], sk.f); me_.update()
    bm_ = _bm.new(); bm_.from_mesh(me_)
    _bm.ops.remove_doubles(bm_, verts=bm_.verts, dist=1e-5)
    _bm.ops.subdivide_edges(bm_, edges=bm_.edges, cuts=8, use_grid_fill=True)
    _bm.ops.triangulate(bm_, faces=bm_.faces)
    bm_.to_mesh(me_); bm_.free(); me_.update()
    ob_ = bpy.data.objects.new('skin_' + part, me_); bpy.context.scene.collection.objects.link(ob_)
    Vs = np.array([v.co[:] for v in me_.vertices]); Ns = np.array([v.normal[:] for v in me_.vertices])
    flip = ((Vs - np.array(inner[:])) * Ns).sum(1) < 0; Ns[flip] *= -1
    pm, _ = PL.build_plates(ob_, Vs, Ns, np.array([part] * len(Vs)), np.random.default_rng(13 + len(part)),
                            lambda c, n_, pt: None if any((Vec(c[:]) - a).length < 0.3 for a in avoid) else dict(top='obsidian', edge='obsidian_edge', side='obsidian_dark'))
    bpy.data.objects.remove(ob_); bpy.data.meshes.remove(me_)
    R13 = random.Random(len(part) * 7)
    g.m = ['magma_head' if m_ == 'SKIN' else m_ for m_ in g.m]  # r15: fresta no laranja do corpo, mais fraca que os olhos
    g.extend(pm)
organic_plates(mb, 'head', T(Vec((3.7, 0, 5.4))), avoid=[T(Vec((3.84 + 0.25, 0.44 * s_ + 0.15 * s_, 5.56))) for s_ in (1, -1)])  # r13: sem placa por cima dos olhos
organic_plates(jb, 'jaw', xj(Vec((3.8, 0, 4.72))))
hb = MB(); hb.extend(mb); hb.extend(jb)
hbvh = _BVH.FromPolygons([Vec(v) for v in hb.v], hb.f)
def hray(o, d):
    h = hbvh.ray_cast(Vec(o), Vec(d).normalized())
    if not h[0]: return None, None
    return h[0], (h[1] if h[1].dot(Vec(d)) < 0 else -h[1])

for s in (1, -1):
    # r12: olho do lote: amarelo chapado aceso, anguloso e franzido (canto de dentro mais baixo),
    # sem pupila nem reflexo, no encaixe de pedra sob uma sobrancelha; longe da aba da coroa
    e = T(Vec((3.84, 0.5 * s, 5.54)))  # r17: olhos mais afastados
    n = (rotH @ Vec((0.74, 0.66 * s, 0.1))).normalized()
    hit, _ = hray(e + n * 3, -n)
    if hit: e = hit - n * 0.03
    upv = (Vec((0, 0, 1)) - n * n.z).normalized()
    ind = n.cross(upv) * s                           # aponta para o meio da cara
    if ind.y * s > 0: ind = -ind
    ER = 0.6
    # contorno no plano do olho: (para dentro, para cima)
    OL = [(-1.0, 0.0), (-0.55, 0.42), (0.15, 0.36), (0.95, -0.02), (0.6, -0.3), (-0.4, -0.36)]
    OL = [(-x * (0.78 if -x > 0 else 1.0), y) for x, y in OL]  # x>0 = para dentro; r17: lado de dentro mais curto (ponte escura entre os olhos)
    def ept(x, y, d, sc=1.0): return e + ind * x * ER * sc + upv * y * ER * sc + n * d
    def eye_prism(sc, d0, d1, dome, mname):
        b_ = [mb.add_v(ept(x, y, d0, sc)) for x, y in OL]
        t_ = [mb.add_v(ept(x, y, d1, sc)) for x, y in OL]
        cc = mb.add_v(ept(0.05, 0.02, d1 + dome, sc))
        m = len(OL)
        for k in range(m):
            k2 = (k + 1) % m
            mb.face([b_[k], b_[k2], t_[k2], t_[k]], mname); mb.face([t_[k], t_[k2], cc], mname)
        mb.face(b_[::-1], mname)
    eye_prism(1.22, -0.12, 0.02, 0.02, 'obsidian_dark')   # encaixe
    eye_prism(1.0, -0.1, 0.07, 0.07, 'eye')               # olho aceso, quase plano
    eye_prism(0.55, -0.05, 0.12, 0.04, 'eye_core')        # r13: núcleo mais claro
    # sobrancelha de pedra sobre a borda de cima (do canto de fora, alto, ao de dentro, baixo)
    p0, p1 = ept(-1.05, 0.72, 0.08), ept(1.0, 0.42, 0.1)  # r13: acima da borda, sem cobrir
    mid = (p0 + p1) / 2; ax = (p1 - p0).normalized()
    rotB = Mat((ax, n.cross(ax).normalized() * -1 if n.cross(ax).dot(upv) < 0 else n.cross(ax).normalized(), n)).transposed()
    ico(mb, mid + n * 0.04, (p1 - p0).length * 0.6, 'obsidian_edge', scale=(1.0, 0.2, 0.3), rot=rotB)
    # maçã do rosto
    ico(mb, ept(-0.2, -0.75, -0.05), 0.32, 'obsidian_edge', scale=(1.3, 0.45, 0.6), rot=rotB)
    # r11: sem espinhos de franja na bochecha (topo da cabeça mais limpo)
    pass  # r12: sem riscos soltos na bochecha
    # v12: dentes grossos de desenho (base larga), presa grande em cima e embaixo; sem serrote
    uy = lambda x: np.interp(x, [s_[0] for s_ in UP], [s_[1][-1][0] for s_ in UP])
    ly = lambda x: np.interp(x, [l[0] for l in LO], [l[1][0][0] for l in LO])
    for x, h, w in ((3.3, 0.13, 0.08), (3.52, 0.15, 0.09), (3.76, 0.17, 0.1), (4.0, 0.19, 0.1), (4.25, 0.34, 0.14), (4.5, 0.18, 0.1), (4.72, 0.16, 0.09), (4.93, 0.13, 0.08)):
        add_cone_blade(mb, T(Vec((x, (uy(x) - 0.08) * s, 4.99))), rotH @ Vec((0, 0, -1)), Vec((1, 0, 0)), h, w, w * 0.75, 'tooth')
    if s > 0:
        for yy in (0.1, -0.1, 0.22, -0.22):
            add_cone_blade(mb, T(Vec((5.02, yy, 4.99))), rotH @ Vec((0, 0, -1)), Vec((1, 0, 0)), 0.13, 0.06, 0.05, 'tooth')
            add_cone_blade(jb, xj(Vec((4.92, yy, 4.92))), rotJ @ Vec((0, 0, 1)), Vec((1, 0, 0)), 0.11, 0.055, 0.045, 'tooth')
    for x, h, w in ((3.45, 0.12, 0.08), (3.68, 0.14, 0.09), (3.92, 0.16, 0.09), (4.16, 0.17, 0.1), (4.42, 0.28, 0.13), (4.66, 0.15, 0.09), (4.86, 0.12, 0.08)):
        add_cone_blade(jb, xj(Vec((x, (ly(x) - 0.09) * s, 4.92))), rotJ @ Vec((0, 0, 1)), Vec((1, 0, 0)), h, w, w * 0.75, 'tooth')
    # nostril
    o, n = hray(T(Vec((4.9, 0.12 * s, 7))), (0, 0, -1))
    if o: sphere(mb, o + n * 0.01, 0.07, 'pupil', scale=(1.3, 0.45, 0.3), rot=rotH @ Mat.Rotation(0.4 * s, 3, 'Z'), seg=8, rings=4)
# horns: 2 big sweeping back with gold rings (left 2, right 1), 2 small
for s in (1, -1):
    pts = bez([T(Vec(p)) for p in ((3.05, 0.42 * s, 5.85), (2.65, 0.6 * s, 6.35), (2.1, 0.74 * s, 6.7), (1.5, 0.8 * s, 6.82))], 4)
    n_ = len(pts)
    prism_chain(mb, pts[:-2], [0.25 * (1 - k / (n_ - 1)) ** 0.8 + 0.01 for k in range(n_ - 2)], 6, 'obsidian_edge', jitter=0.05, rng=R)
    prism_chain(mb, pts[-3:], [0.25 * (1 - k / (n_ - 1)) ** 0.8 + 0.01 for k in range(n_ - 3, n_)], 6, 'gold', jitter=0.03, rng=R)  # r14: ponta do chifre em ouro
    for t in ((0.25, 0.47) if s > 0 else (0.36,)):
        k = int(t * (n_ - 1)); d = (pts[k + 1] - pts[k - 1]).normalized()
        torus(mb, pts[k], d, 0.25 * (1 - t) ** 0.8 + 0.05, 0.08, 'gold_edge', seg=12, sides=5)  # r14: anel grosso
    pass  # r11: sem o par de chifres pequenos
