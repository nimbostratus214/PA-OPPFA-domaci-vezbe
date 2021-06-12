from vortex import *
from funs import *

if __name__ == "__main__":
    v = Vortex(n="v")
    r = Vortex(n="r")
    s = Vortex(n="s")
    w = Vortex(n="w")
    t = Vortex(n="t")
    x = Vortex(n="x")
    u = Vortex(n="u")
    y = Vortex(n="y")

    v.connection = [r]
    r.connection = [s, r]
    s.connection = [r, w]
    w.connection = [s, t, x]
    t.connection = [w, x, u]
    x.connection = [w, t, u, x]
    u.connection = [t, x, y]
    y.connection = [u, x]

    G = [v, r, s, w, t, x, u, y]

    bfs_script(G, s, x)