# ---- detail parts; exec'd inside build.py (uses M, rng, R, core, bvh0, ANCH, MB, to_object, prism_chain, basis)
from mathutils import Vector as Vec, Matrix as Mat, Quaternion as Quat
from mathutils.bvhtree import BVHTree as _BVH
import math

def ray(o, d):
    hit = bvh0.ray_cast(Vec(o), Vec(d).normalized())
    if not hit[0]: return None, None
    n = hit[1] if hit[1].dot(Vec(d)) < 0 else -hit[1]
    return hit[0], n

def add_cone_blade(mb, base, up, fwd, h, w, t, mname, edge=None):
    """flattened faceted blade (spike): diamond cross-section, tapering to tip"""
    up = Vec(up).normalized(); fwd = (Vec(fwd) - up * Vec(fwd).dot(up)).normalized(); side = up.cross(fwd)
    b = Vec(base)
    ring = [b + fwd * w, b + side * t, b - fwd * w * 0.7, b - side * t]
    mid = [b + up * h * 0.45 + fwd * w * 0.55 - fwd * w * 0.25, b + up * h * 0.45 + side * t * 0.6 - fwd * w * 0.25,
           b + up * h * 0.45 - fwd * w * 0.6, b + up * h * 0.45 - side * t * 0.6 - fwd * w * 0.25]
    tip = b + up * h - fwd * w * 0.9
    r0 = [mb.add_v(p) for p in ring]; r1 = [mb.add_v(p) for p in mid]; tp = mb.add_v(tip)
    for i in range(4):
        j = (i + 1) % 4
        mb.face([r0[i], r0[j], r1[j], r1[i]], mname)
        mb.face([r1[i], r1[j], tp], edge if (edge and i in (0, 3)) else mname)
    mb.face(list(reversed(r0)), mname)

def torus(mb, center, normal, R, r, mname, seg=20, sides=6, sx=1.0):
    t, b, n = basis(Vec(normal))
    rings = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        c = Vec(center) + (t * math.cos(a) * sx + b * math.sin(a)) * R
        radial = (t * math.cos(a) + b * math.sin(a))
        ring = [mb.add_v(c + (radial * math.cos(2 * math.pi * k / sides) + n * math.sin(2 * math.pi * k / sides)) * r) for k in range(sides)]
        rings.append(ring)
    for i in range(seg):
        i2 = (i + 1) % seg
        for k in range(sides):
            k2 = (k + 1) % sides
            mb.face([rings[i][k], rings[i2][k], rings[i2][k2], rings[i][k2]], mname)

def ico(mb, center, rad, mname, scale=(1, 1, 1), rot=None, flat=1):
    # octahedron-ish faceted gem / rock
    c = Vec(center); s = Vec(scale)
    pts = [Vec((1, 0, 0)), Vec((-1, 0, 0)), Vec((0, 1, 0)), Vec((0, -1, 0)), Vec((0, 0, 1)), Vec((0, 0, -1))]
    pts = [Vec((p.x * s.x, p.y * s.y, p.z * s.z)) * rad for p in pts]
    if rot: pts = [rot @ p for p in pts]
    ids = [mb.add_v(c + p) for p in pts]
    for a, b_, cc in ((0, 2, 4), (2, 1, 4), (1, 3, 4), (3, 0, 4), (2, 0, 5), (1, 2, 5), (3, 1, 5), (0, 3, 5)):
        mb.face([ids[a], ids[b_], ids[cc]], mname)

def sphere(mb, center, rad, mname, scale=(1, 1, 1), rot=None, seg=10, rings=6):
    c = Vec(center); s = Vec(scale); ids = []
    top = mb.add_v(c + (rot @ Vec((0, 0, rad * s.z)) if rot else Vec((0, 0, rad * s.z))))
    for i in range(1, rings):
        th = math.pi * i / rings; row = []
        for k in range(seg):
            ph = 2 * math.pi * k / seg
            p = Vec((math.sin(th) * math.cos(ph) * s.x, math.sin(th) * math.sin(ph) * s.y, math.cos(th) * s.z)) * rad
            row.append(mb.add_v(c + (rot @ p if rot else p)))
        ids.append(row)
    bot = mb.add_v(c + (rot @ Vec((0, 0, -rad * s.z)) if rot else Vec((0, 0, -rad * s.z))))
    for k in range(seg):
        k2 = (k + 1) % seg
        mb.face([top, ids[0][k], ids[0][k2]], mname)
        mb.face([bot, ids[-1][k2], ids[-1][k]], mname)
    for i in range(len(ids) - 1):
        for k in range(seg):
            k2 = (k + 1) % seg
            mb.face([ids[i][k], ids[i + 1][k], ids[i + 1][k2], ids[i][k2]], mname)

def bez(pts, n):
    # catmull-rom through control points
    out = []
    P = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(P) - 2):
        for k in range(n):
            t = k / n
            p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(pts[-1])
    return out

GROUPS = {}   # name -> MB  (each becomes one object, later skinned to a bone)
def G(name):
    if name not in GROUPS: GROUPS[name] = MB()
    return GROUPS[name]

# ================= WINGS =================
def point_in_poly(pts2, poly):
    x, y = pts2[:, 0], pts2[:, 1]; inside = np.zeros(len(pts2), bool); n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        cond = ((y1 > y) != (y2 > y)) & (x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1)
        inside ^= cond
    return inside

def wing(s):
    mb = G('wing_' + ('L' if s > 0 else 'R'))
    S = lambda x, y, z: Vec((x, y * s, z))
    Rt = S(0.75, 0.95, 3.95); E = S(0.35, 2.2, 5.4); W = S(-0.3, 2.75, 6.35)
    TH = S(0.15, 2.85, 6.75)
    F = [S(-3.2, 3.6, 6.85), S(-3.85, 3.7, 5.3), S(-3.55, 3.3, 3.9), S(-2.4, 2.4, 3.3)]
    B = S(-1.25, 1.0, 3.55)
    # finger knuckle points (slightly bent)
    Fk = [W.lerp(f, 0.5) + S(0, 0.15, 0.12) for f in F]
    # membrane outline
    outline = [Rt, E, W, F[0]]
    for i in range(3):
        mid = F[i].lerp(F[i + 1], 0.5); outline += [mid.lerp(W, 0.28), F[i + 1]]
    mid = F[3].lerp(B, 0.5); outline += [mid.lerp(W, 0.2), B]
    # plane fit
    O = np.array([list(p) for p in outline]); c0 = O.mean(0)
    u_, s_, vt = np.linalg.svd(O - c0); ax = vt[0]; ay = vt[1]; nz = vt[2]
    if nz[1] * s < 0: nz = -nz
    poly = np.stack([(O - c0) @ ax, (O - c0) @ ay], 1)
    # dense samples inside outline
    lo = poly.min(0); hi = poly.max(0); st = 0.05
    gx, gy = np.meshgrid(np.arange(lo[0], hi[0], st), np.arange(lo[1], hi[1], st))
    G2 = np.stack([gx.ravel(), gy.ravel()], 1); G2 = G2[point_in_poly(G2, poly)]
    # camber: membrane bows outward between fingers
    def lift(p2, off):
        p = c0 + ax * p2[0] + ay * p2[1]
        # distance to nearest finger line -> bulge
        P3 = Vec(p)
        dmin = 9
        for f in F + [E]:
            a, b = W, f
            ab = b - a; t = max(0, min(1, (P3 - a).dot(ab) / ab.length_squared)); dmin = min(dmin, (a + ab * t - P3).length)
        return P3 + Vec(nz) * (off - 0.18 * min(dmin, 0.7))
    # yellow vein sheet (both faces)
    from scipy.spatial import Delaunay
    G3 = np.vstack([G2[::14], poly])
    def sheet(off, mname, flip):
        tri = Delaunay(G3)
        cen = G3[tri.simplices].mean(1); keep = point_in_poly(cen, poly)
        ids = [mb.add_v(lift(p, off)) for p in G3]
        for t_ in tri.simplices[keep]:
            mb.face([ids[t_[0]], ids[t_[2]], ids[t_[1]]] if flip else [ids[t_[0]], ids[t_[1]], ids[t_[2]]], mname)
    sheet(0.0, 'lava_wing', False); sheet(-0.002, 'lava_wing', True)  # r11: veias da asa mais fracas  # v9: veias laranja na membrana  # v5: laranja só na borda
    # voronoi cells (stained glass)
    seeds = []
    for i in rng.permutation(len(G2)):
        r = 0.55 * rng.uniform(0.7, 1.3)
        if not seeds or min(np.linalg.norm(G2[j] - G2[i]) for j in seeds) > r: seeds.append(i)
    SP = G2[seeds]
    own = np.argmin(np.linalg.norm(G2[:, None] - SP[None], axis=2), 1)
    from scipy.spatial import ConvexHull
    wrist2 = np.array([(np.array(W) - c0) @ ax, (np.array(W) - c0) @ ay])
    for ci in range(len(SP)):
        Q = G2[own == ci]
        if len(Q) < 4: continue
        try: h = ConvexHull(Q)
        except Exception: continue
        H = Q[h.vertices]; cc = Q.mean(0)
        kp = [0]
        for i in range(1, len(H)):
            if np.linalg.norm(H[i] - H[kp[-1]]) > 0.11: kp.append(i)
        if len(kp) > 3 and np.linalg.norm(H[kp[-1]] - H[0]) < 0.06: kp.pop()
        if len(kp) < 3: continue
        H = H[kp]
        H = np.array([p + (cc - p) / (np.linalg.norm(cc - p) + 1e-9) * min(0.028, np.linalg.norm(cc - p) * 0.4) for p in H])
        far = np.linalg.norm(cc - wrist2)
        mname = 'wing_dark' if far > 1.6 or rng.random() < 0.5 else 'wing_dark2'  # v4: membrana escura, laranja só nas veias e borda
        for side_off, flip in ((0.035, False), (-0.035, True)):
            ring = [mb.add_v(lift(p, side_off)) for p in H]
            ctr = mb.add_v(lift(cc, side_off * 1.4))
            k = len(ring)
            for i in range(k):
                f = [ring[i], ring[(i + 1) % k], ctr]
                mb.face(f[::-1] if flip else f, mname)
            if not flip: top = ring
            else: bot = ring
        for i in range(len(top)):
            j = (i + 1) % len(top)
            mb.face([top[i], bot[i], bot[j], top[j]], mname)
    # v6: nervuras acesas finas ao longo dos dedos, por dentro da membrana
    for f in F:
        prism_chain(mb, [lift(np.array([(np.array(W.lerp(f, u)) - c0) @ ax, (np.array(W.lerp(f, u)) - c0) @ ay]), 0.04) for u in (0.12, 0.45, 0.85)], [0.03, 0.025, 0.012], 4, 'lava_vein')
    # v4: borda laranja da membrana
    # r15: ouro só na borda da frente (braço e dedo de cima), mais grosso; a borda de trás fica em pedra escura
    prism_chain(mb, outline[1:4], [0.08] * 3, 6, 'gold')
    prism_chain(mb, outline[3:] + [outline[1]], [0.04] * (len(outline) - 2), 5, 'obsidian_dark')
    # arm + fingers (faceted obsidian)
    arm = bez([Rt, E, W], 4)
    prism_chain(mb, arm, [0.3 - 0.15 * i / (len(arm) - 1) for i in range(len(arm))], 6, 'obsidian', jitter=0.08, rng=R)
    for i, f in enumerate(F + [TH]):
        pts = bez([W, Fk[i], f], 4) if i < 4 else [W, W.lerp(TH, 0.5), TH]
        n_ = len(pts)
        prism_chain(mb, pts, [0.11 * (1 - k / (n_ - 1)) + 0.025 for k in range(n_)], 5, 'obsidian', jitter=0.06, rng=R)
        if i < 4:
            add_cone_blade(mb, f, (f - Fk[i]).normalized(), Vec(nz), 0.48, 0.1, 0.06, 'gold', 'gold_edge')  # v9: pontas douradas
    # thumb claw (gold) + wrist & elbow spikes
    add_cone_blade(mb, TH, (TH - W).normalized() + Vec((0, 0, 0.6)), Vec((1, 0, 0)), 0.62, 0.16, 0.11, 'gold', 'gold_edge')  # r14: garra da asa grande em ouro
    for p, d, h in ((W, S(-0.2, 0.3, 1), 0.55), (E, S(0.2, 0.5, 0.6), 0.4), (E.lerp(W, 0.5), S(0, 0.4, 1), 0.28)):
        add_cone_blade(mb, p, d, Vec((1, 0, 0)), h, 0.12, 0.07, 'gold' if p is W else 'obsidian', 'gold_edge' if p is W else 'obsidian_edge')  # r14: espinho do pulso em ouro
    # armour chunks on the arm
    for t in (0.2, 0.45, 0.7, 0.9):
        p = arm[int(t * (len(arm) - 1))]
        ico(mb, p, 0.24 - 0.08 * t, 'obsidian', scale=(1.0, 0.8, 0.7), rot=Euler((R.random(), R.random(), R.random())).to_matrix())

from mathutils import Euler
wing(1); wing(-1)
# v9: asas 25% maiores
for sd_ in ('L', 'R'):
    g = GROUPS['wing_' + sd_]; sg_ = 1 if sd_ == 'L' else -1; rt = Vec((0.75, 0.95 * sg_, 3.95))
    g.v = [tuple(rt + (Vec(v) - rt) * 1.25) for v in g.v]

# ================= DORSAL SPIKES =================
mb = G('spikes')
xs = np.linspace(2.75, -4.3, 13)
for i, x in enumerate(xs):
    o, n = ray((x, 0, 9), (0, 0, -1))
    if o is None: continue
    h = 0.35 + 0.45 * math.exp(-((x - 0.2) / 2.3) ** 2)
    if x > 2.2: h *= 0.75
    add_cone_blade(mb, o - Vec((0, 0, 0.05)), Vec((0.0, 0, 1)) + Vec((-0.35, 0, 0)), Vec((1, 0, 0)), h + 0.12, 0.2 + 0.1 * h, 0.07, 'obsidian', 'obsidian_edge')

# ================= HEAD =================
exec(open('head.py').read())
# crown: 3 gold blades + magma jewel
o, n = hray(T(Vec((2.72, 0, 9))), (0, 0, -1))  # r14: coroa mais para trás, faixa de pedra entre ela e os olhos
cb = o - Vec((0, 0, 0.05))
add_cone_blade(mb, cb, Vec((0.1, 0, 1)), Vec((1, 0, 0)), 1.7, 0.4, 0.13, 'gold', 'gold_edge')
for s in (1, -1):
    add_cone_blade(mb, cb + Vec((-0.05, 0.3 * s, -0.03)), Vec((0, 0.5 * s, 1)), Vec((1, 0, 0)), 1.25, 0.32, 0.11, 'gold', 'gold_edge')
    add_cone_blade(mb, cb + Vec((-0.25, 0.32 * s, -0.04)), Vec((-0.5, 0.6 * s, 1)), Vec((1, 0, 0)), 1.0, 0.27, 0.09, 'gold', 'gold_edge')
    add_cone_blade(mb, cb + Vec((0.2, 0.34 * s, -0.04)), Vec((0.3, 0.6 * s, 1)), Vec((1, 0, 0)), 0.8, 0.24, 0.09, 'gold', 'gold_edge')
torus(mb, cb + Vec((0, 0, 0.08)), Vec((0.15, 0, 1)), 0.5, 0.12, 'gold', seg=18, sides=6)
ico(mb, cb + Vec((0.5, 0, 0.3)), 0.24, 'jewel', scale=(0.7, 1, 1.3))

# ================= CHEST FURNACE =================
mb = G('chest')
fo, fn = ANCH['furnace']
sphere(mb, fo - fn * 0.3, 0.3, 'magma', seg=12, rings=8)
torus(mb, fo + fn * 0.12, fn, 0.5, 0.13, 'gold', seg=22, sides=6)
# v4: peitoral de ouro em leque em volta da fornalha
for k in range(7):
    a = math.radians(-150 + k * 50)
    d = (t_ * math.cos(a) + b_ * math.sin(a)) if False else None
t_, b_, n_ = basis(fn)
for k in range(5):
    a = k / 5 * 2 * math.pi + 0.3
    rad = (t_ * math.cos(a) + b_ * math.sin(a))
    add_cone_blade(mb, fo + fn * 0.1 + rad * 0.62, rad, fn, 0.55, 0.26, 0.07, 'obsidian_edge', 'obsidian')
# gold spiral filigree
t_, b_, n_ = basis(fn)
sp = []
for k in range(60):
    a = k / 59 * 2.2 * math.pi; r = 0.55 + 0.38 * k / 59
    sp.append(fo + fn * (0.16 - 0.05 * k / 59) + (t_ * math.cos(a) + b_ * math.sin(a)) * r)
pass
for k in range(6):
    a = k / 6 * 2 * math.pi
    ico(mb, fo + fn * 0.15 + (t_ * math.cos(a) + b_ * math.sin(a)) * 0.46, 0.06, 'gold_edge')

# ================= GOLD RINGS (shoulders / thighs) =================
for nm, (x, z, rr) in (('hleg', (-1.3, 1.9, 0.55)), ('fleg', (1.5, 2.0, 0.45))):
    for s in (1, -1):
        mb = G(nm + ('L' if s > 0 else 'R'))
        o, n = ray((x, 4 * s, z), (0, -s, 0))
        if o:
            # v3: gold band wrapped around the limb (not a hoop on the skin)
            c = Vec((x, 0, z)); c.y = o.y - s * (rr + 0.05)
            torus(mb, c, Vec((0.15 * (1 if nm == 'fleg' else -1), 0, 1)), rr + 0.08, 0.2, 'gold', seg=28, sides=6, sx=1.15)  # r15: faixa grossa encostada na perna
            pass

# v4: ombreiras e placas de quadril de ouro
for nm, (x, z) in (('fleg', (1.45, 2.75)), ('hleg', (-1.35, 2.45))):
    for s in (1, -1):
        mb = G(nm + ('L' if s > 0 else 'R'))
        o, n = ray((x, 4 * s, z), (0, -s, 0))
        if o:
            for k in range(3):
                add_cone_blade(mb, o + n * 0.15 + Vec((0.35 * (k - 1), 0, 0.35)), Vec((0, 0.6 * s, 1)), Vec((1, 0, 0)), 0.5, 0.16, 0.06, 'obsidian_edge', 'obsidian')

# v4: rochas de lava orbitando (peça em volta do corpo do Mythic, no modelo base)
mb = G('orbit')
for k in range(5):
    a = k / 5 * 2 * math.pi
    c = Vec((-0.3 + 3.7 * math.cos(a), 3.7 * math.sin(a), 3.3 + 0.6 * math.sin(3 * a)))
    rr = 0.58 + 0.12 * (k % 2)  # r14: pedras de lava maiores, legíveis no ícone
    rm_ = Euler((k, 2 * k, 0.5 * k)).to_matrix()
    # r16: rocha escura com fissuras finas (a lava só aparece nas frestas), sem cara de abóbora
    sphere(mb, c, rr * 0.7, 'magma', seg=8, rings=5)
    for j in range(5):
        dj = rm_ @ Vec((math.cos(j * 1.256), math.sin(j * 1.256), 0.35 * ((j % 2) * 2 - 1)))
        ico(mb, c + dj * rr * 0.3, rr * 0.76, 'obsidian' if j % 2 else 'obsidian_edge', scale=(1.0, 0.85, 0.8), rot=rm_ @ Mat.Rotation(j * 1.1, 3, 'X') @ Mat.Rotation(j * 0.7, 3, 'Z'))

# v6: joelhos marcados com placa-espinho de obsidiana
for nm, kp, d in (('fleg', (1.62, 1.2), (1, 0, 0.35)), ('hleg', (-1.12, 1.05), (-1, 0, 0.45))):
    for s in (1, -1):
        mb = G(nm + ('L' if s > 0 else 'R'))
        o, n = ray((kp[0] + 2.0 * d[0], 1.12 * s, kp[1]), (-d[0], 0, 0))
        if o: add_cone_blade(mb, o - n * 0.05, Vec(d), Vec((0, 1, 0)), 0.42, 0.26, 0.12, 'obsidian_edge', 'obsidian')

# ================= CLAWS =================
for nm, fx in (('ffoot', 1.95), ('hfoot', -1.0)):
    for s in (1, -1):
        mb = G(nm.replace('foot', 'leg') + ('L' if s > 0 else 'R'))
        for k, a in enumerate((-0.55, -0.18, 0.18, 0.55)):
            d = Vec((math.cos(a), math.sin(a), 0))
            base = Vec((fx, 1.15 * s, 0.16)) + d * 0.5
            torus(mb, base, d, 0.075, 0.025, 'gold', seg=8, sides=4)
            pts = [base, base + d * 0.22, base + d * 0.42 - Vec((0, 0, 0.14))]
            prism_chain(mb, pts, [0.11, 0.08, 0.01], 5, 'tooth')  # v8: garras de osso maiores

# ================= TAIL AXE =================
mb = G('tail_tip')
o = Vec(ANCH['tail_end']); tdir = Vec(ANCH['tail_dir']).normalized()
perp = tdir.cross(Vec((0, 1, 0))).normalized()  # in XZ plane, perpendicular to tail
sphere(mb, o, 0.3, 'gold', seg=10, rings=6)
for sgn in (1, -1):
    pv = perp * sgn
    root_a = o + tdir * 0.28 + pv * 0.12; root_b = o - tdir * 0.22 + pv * 0.12
    edge_a = o + tdir * 0.8 + pv * 0.8; edge_b = o - tdir * 0.6 + pv * 0.8
    edge_m = o + tdir * 0.1 + pv * 1.0
    out = [root_a, edge_a, edge_m, edge_b, root_b]
    th = [0.12, 0.05, 0.05, 0.05, 0.12]
    Y = Vec((0, 1, 0))
    top = [mb.add_v(p + Y * t) for p, t in zip(out, th)]
    bot = [mb.add_v(p - Y * t) for p, t in zip(out, th)]
    mid = [mb.add_v(p.lerp(o + pv * 0.5, 0.25) + Y * 0.13) for p in out]
    midb = [mb.add_v(p.lerp(o + pv * 0.5, 0.25) - Y * 0.13) for p in out]
    for i in range(4):
        e = 'gold_edge' if i in (1, 2) else 'obsidian_edge'
        mb.face([top[i], top[i + 1], mid[i + 1], mid[i]], e)
        mb.face([bot[i + 1], bot[i], midb[i], midb[i + 1]], e)
    mb.face(mid[::-1], 'obsidian'); mb.face(midb, 'obsidian')
    for i in range(4):
        mb.face([top[i + 1], top[i], bot[i], bot[i + 1]], 'gold')
    mb.face([top[0], top[4], bot[4], bot[0]], 'obsidian_dark')
    # magma line on the blade
    prism_chain(mb, [o + pv * 0.3 + tdir * 0.15, o + pv * 0.55 + tdir * 0.05, o + pv * 0.68 - tdir * 0.1], [0.03, 0.035, 0.02], 4, 'lava_vein')

# v5+: cabeça maior, um pouco à frente (HS em common.py)
for name in ('head', 'jaw'):
    g = GROUPS[name]; piv = Vec((2.6, 0, 4.9))
    g.v = [tuple(piv + (Vec(v) - piv) * HS + Vec((0.3, 0, 0.18))) for v in g.v]
for name, g in GROUPS.items():
    ob = to_object(g, 'part_' + name, M)
