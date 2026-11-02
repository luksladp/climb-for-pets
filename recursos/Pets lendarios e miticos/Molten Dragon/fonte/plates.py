import numpy as np, math, random
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from scipy.spatial import ConvexHull
from common import MB, basis

# plate size (Poisson radius), crack gap, thickness by part
PARAMS = {
    'torso': (1.1, 0.05, 0.22), 'neck': (0.68, 0.045, 0.16), 'head': (0.62, 0.035, 0.12),
    'jaw': (0.58, 0.035, 0.1), 'tail': (0.6, 0.045, 0.13),
    'fleg': (0.62, 0.045, 0.15), 'hleg': (0.7, 0.045, 0.16), 'ffoot': (0.42, 0.035, 0.09), 'hfoot': (0.42, 0.035, 0.09),
}

def poisson(P, N, radius_fn, rng):
    order = rng.permutation(len(P)); seeds = []
    S = np.zeros((0, 3))
    for i in order:
        r = radius_fn(P[i]) * rng.uniform(0.75, 1.3)
        if len(S) == 0 or np.min(np.linalg.norm(S - P[i], axis=1)) > r:
            seeds.append(i); S = np.vstack([S, P[i]])
    return np.array(seeds)

def build_plates(core_ob, verts, normals, parts, rng, classify):
    """classify(centroid, normal, part) -> dict(top=, edge=, side=) material names or None to skip"""
    bm_tree = BVHTree.FromObject(core_ob, __import__('bpy').context.evaluated_depsgraph_get())
    mb = MB(); info = []
    base = np.array([p.rstrip('LR') for p in parts])
    for part in np.unique(parts):
        key = part.rstrip('LR')
        size, gap, thick = PARAMS[key]
        idx = np.where(parts == part)[0]
        P = verts[idx]; N = normals[idx]
        def rf(p):
            s = size
            if key == 'tail': s = size * max(0.62, min(1.0, (p[0] + 5.2) / 3.0))
            if key == 'neck' and p[2] > 4.4: s *= 0.8
            return s
        seeds = poisson(P, N, rf, rng)
        S = P[seeds]; SN = N[seeds]
        # metric: distance + normal disagreement
        D = np.linalg.norm(P[:, None, :] - S[None], axis=2) + 0.5 * (1 - N @ SN.T)
        own = np.argmin(D, axis=1)
        for c in range(len(seeds)):
            m = own == c
            if m.sum() < 5: continue
            Q = P[m]; QN = N[m]
            cen = Q.mean(0); nrm = QN.mean(0); nrm /= np.linalg.norm(nrm) + 1e-9
            t, b, n = basis(nrm); t = np.array(t); b = np.array(b)
            uv = np.stack([(Q - cen) @ t, (Q - cen) @ b], 1)
            try: hull = ConvexHull(uv)
            except Exception: continue
            H = Q[hull.vertices]; Huv = uv[hull.vertices]
            # simplify: drop points closer than min_len to the previous kept one
            min_len = rf(cen) * 0.16
            keep = [0]
            for i in range(1, len(H)):
                if np.linalg.norm(Huv[i] - Huv[keep[-1]]) > min_len: keep.append(i)
            if len(keep) > 2 and np.linalg.norm(Huv[keep[-1]] - Huv[keep[0]]) < min_len * 0.6: keep.pop()
            if len(keep) < 3: continue
            H = H[keep]
            g = gap * (0.45 + 0.6 * rng.random() ** 2)  # v4: fissuras finas (veias)
            # inset toward centroid in tangent plane
            Hi = []
            for h in H:
                d = (cen - h); d -= nrm * (d @ nrm); L = np.linalg.norm(d)
                Hi.append(h + d / (L + 1e-9) * min(g, L * 0.45))
            Hi = np.array(Hi)
            hit = bm_tree.find_nearest(Vector(cen))
            sc = np.array(hit[0]) if hit[0] else cen
            bulge = (sc - Hi.mean(0)) @ nrm
            mats = classify(cen, nrm, part)
            if mats is None: continue
            th = thick * (0.8 + 0.5 * rng.random())
            k = len(Hi)
            ring_b = [mb.add_v(h - nrm * 0.10) for h in Hi]
            ring_t = [mb.add_v(h + (h - cen) * 0.06 + nrm * th * 0.45) for h in Hi]
            # v3: chunky bevelled block (flat domed top) instead of a faceted pyramid
            ring_c = []
            for h in Hi:
                q = h + (cen - h) * 0.16
                ring_c.append(mb.add_v(q + nrm * (th * 0.9 + 0.6 * max(bulge, 0))))
            apex = mb.add_v(Hi.mean(0) + nrm * (th * 0.98 + 0.75 * max(bulge, 0)))
            for i in range(k):
                j = (i + 1) % k
                mb.face([ring_b[i], ring_b[j], ring_t[j], ring_t[i]], mats['side'])
                mb.face([ring_t[i], ring_t[j], ring_c[j], ring_c[i]], mats['edge'])
                mb.face([ring_c[i], ring_c[j], apex], mats['top'])
            mb.face(list(reversed(ring_b)), mats['side'])
            info.append((part, cen, nrm, Hi))
    return mb, info
