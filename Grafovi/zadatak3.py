from vortex import *
from funs import *

if __name__ == "__main__":
    u = Vortex(n = "u")
    v = Vortex(n = "v")
    x = Vortex(n = "x")
    y = Vortex(n = "y")
    w = Vortex(n = "w")
    z = Vortex(n = "z")

    u.connection = [v, x]
    v.connection = [y]
    x.connection = [v]
    y.connection = [x]
    w.connection = [y, z]
    z.connection = [z]

    G = [u, v, x, y, w, z]

    dfs_script(G, u, y)