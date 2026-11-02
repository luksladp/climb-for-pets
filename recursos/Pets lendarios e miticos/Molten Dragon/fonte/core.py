# SDF core of the Molten Dragon (Blender coords: +X forward, +Y left, +Z up, ground z=0)
import numpy as np
from skimage.measure import marching_cubes

def ell(c, r):
    c = np.array(c, float); r = np.array(r, float)
    def f(P):
        q = (P - c) / r
        k0 = np.linalg.norm(q, axis=-1); k1 = np.linalg.norm(q / r, axis=-1)
        return k0 * (k0 - 1.0) / np.maximum(k1, 1e-6)
    return f

def rcone(a, b, ra, rb):
    a = np.array(a, float); b = np.array(b, float)
    def f(P):
        ba = b - a; l2 = ba @ ba; rr = ra - rb; a2 = l2 - rr * rr; il2 = 1.0 / l2
        pa = P - a; y = pa @ ba; z = y - l2
        x2v = pa * l2 - y[..., None] * ba; x2 = (x2v * x2v).sum(-1); y2 = y * y * l2; z2 = z * z * l2
        k = np.sign(rr) * rr * rr * x2
        d = np.where(np.sign(z) * a2 * z2 > k, np.sqrt(x2 + z2) * il2 - rb,
            np.where(np.sign(y) * a2 * y2 < k, np.sqrt(x2 + y2) * il2 - ra,
                     (np.sqrt(x2 * a2 * il2) + y * rr) * il2 - ra))
        return d
    return f

def chain(pts, part):
    return [(part, rcone(pts[i][0], pts[i + 1][0], pts[i][1], pts[i + 1][1])) for i in range(len(pts) - 1)]

def primitives():
    P = []
    P += [('torso', ell((0.95, 0, 2.95), (1.4, 1.3, 1.35))),
          ('torso', ell((1.6, 0, 2.95), (0.95, 1.1, 1.2))),
          ('torso', ell((-0.25, 0, 2.65), (1.4, 1.2, 1.12))),
          ('torso', ell((-1.4, 0, 2.65), (1.05, 1.1, 1.0)))]
    P += chain([((1.9, 0, 3.6), 0.95), ((2.5, 0, 4.35), 0.72), ((2.85, 0, 4.95), 0.6)], 'neck')
    P += [('neck', ell((2.95, 0, 5.15), (0.5, 0.52, 0.55)))]
    for s, side in ((1, 'L'), (-1, 'R')):
        P += [('fleg' + side, ell((1.4, 1.0 * s, 2.6), (0.78, 0.62, 1.05)))]
        P += chain([((1.45, 1.12 * s, 1.95), 0.62), ((1.6, 1.15 * s, 0.95), 0.46), ((1.65, 1.15 * s, 0.35), 0.44)], 'fleg' + side)
        P += [('ffoot' + side, ell((1.95, 1.15 * s, 0.22), (0.6, 0.48, 0.25)))]
        P += [('hleg' + side, ell((-1.4, 1.0 * s, 2.1), (1.0, 0.65, 1.0)))]
        P += chain([((-1.3, 1.12 * s, 1.5), 0.6), ((-1.05, 1.15 * s, 0.95), 0.42), ((-1.35, 1.15 * s, 0.45), 0.38)], 'hleg' + side)
        P += [('hfoot' + side, ell((-1.0, 1.15 * s, 0.22), (0.6, 0.48, 0.25)))]
    P += chain([((-2.2, 0, 2.6), 0.85), ((-3.0, 0, 2.05), 0.62), ((-3.7, 0, 1.72), 0.46), ((-4.3, 0, 1.85), 0.35),
                ((-4.7, 0, 2.25), 0.27), ((-4.85, 0, 2.75), 0.21)], 'tail')
    return P

def smin(a, b, k):
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0, 1)
    return b * (1 - h) + a * h - k * h * (1 - h)

def build(res=0.045):
    prims = primitives()
    lo = np.array([-5.7, -2.0, -0.2]); hi = np.array([5.4, 2.0, 6.3])
    n = np.ceil((hi - lo) / res).astype(int) + 1
    g = np.stack(np.meshgrid(*[lo[i] + np.arange(n[i]) * res for i in range(3)], indexing='ij'), -1)
    d = None
    for part, f in prims:
        v = f(g)
        k = 0.12 if part in ('jaw',) else 0.28
        d = v if d is None else smin(d, v, k)
    d = np.maximum(d, -g[..., 2])  # flat soles at ground
    verts, faces, _, _ = marching_cubes(d, 0.0, spacing=(res, res, res))
    verts += lo
    # label each vertex by its dominant primitive
    labels = [p for p, _ in prims]
    best = np.full(len(verts), 1e9); lab = np.zeros(len(verts), int)
    for i, (part, f) in enumerate(prims):
        v = f(verts)
        m = v < best; best[m] = v[m]; lab[m] = i
    parts = np.array(labels)[lab]
    return verts, faces[:, ::-1], parts

if __name__ == '__main__':
    import time; t = time.time()
    v, f, p = build()
    print(len(v), len(f), time.time() - t, np.unique(p, return_counts=True))
    np.savez('core.npz', v=v, f=f, p=p)
