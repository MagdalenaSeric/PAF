import numpy as np
import matplotlib.pyplot as plt

m = 9.11e-31
q_e = -1.602e-19
q_p = +1.602e-19

B = np.array([0.0, 0.0, 5e-3])

r0 = np.array([0.0, 0.0, 0.0])
v0 = np.array([1e5, 2e5, 5e4])

dt = 1e-12
N = 20000

def akceleracija(q, v, E):
    F = E + np.cross(v, B)
    return (q/m) * F

def run_kut(q, r, v, dt, E):
    k1v = akceleracija(q, v, E)
    k1r = v

    k2v = akceleracija(q, v + 0.5*dt*k1v, E)
    k2r = v + 0.5*dt*k1v

    k3v = akceleracija(q, v + 0.5*dt*k2v, E)
    k3r = v + 0.5*dt*k2v

    k4v = akceleracija(q, v + dt*k3v, E)
    k4r = v + dt*k3v

    nova_v = v + (dt/6)*(k1v + 2*k2v + 2*k3v + k4v)
    novi_r = r + (dt/6)*(k1r + 2*k2r + 2*k3r + k4r)

    return nova_v, novi_r

def simulacija(q, E):
    r = []
    v = []

    r.append(r0.copy())
    v.append(v0.copy())

    for i in range(N - 1):
        nova_v, novi_r = run_kut(q, r[i], v[i], dt, E)
        r.append(novi_r)
        v.append(nova_v)

    return np.array(r)

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

pts = simulacija(q_e, np.array([0,0,0]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E = 0", linewidth = 1)

pts = simulacija(q_e, np.array([0,0,100]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E || B", linewidth = 1)

pts = simulacija(q_e, np.array([100,0,0]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E ⊥ B", linewidth = 1)

ax.legend()
ax.set_xlabel("x", labelpad=15, fontsize=12)
ax.set_ylabel("y", labelpad=15, fontsize=12)
ax.set_zlabel("z", labelpad=15, fontsize=12)
plt.title("Elektron")
ax.set_box_aspect([1,1,1])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

pts = simulacija(q_p, np.array([0,0,0]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E = 0", linewidth = 1)

pts = simulacija(q_p, np.array([0,0,100]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E || B", linewidth = 1)

pts = simulacija(q_p, np.array([100,0,0]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E ⊥ B", linewidth = 1)

ax.legend()
ax.set_xlabel("x", labelpad=15, fontsize=12)
ax.set_ylabel("y", labelpad=15, fontsize=12)
ax.set_zlabel("z", labelpad=15, fontsize=12)
plt.title("Pozitron")
ax.set_box_aspect([1,1,1])
plt.show()