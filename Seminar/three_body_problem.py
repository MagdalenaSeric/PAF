import numpy as np
import matplotlib.pyplot as plt

#gravitacijska konstanta
G = 6.6743e-11

#vremenski korak i broj koraka simulacije
dt = 0.005
koraci_simulacije = 400000


def udaljenost(rA, rB):
    #udaljenost dviju točaka u prostoru
    return np.sqrt((rA[0] - rB[0])**2 + (rA[1] - rB[1])**2 + (rA[2] - rB[2])**2)

def akceleracija(r1, r2, r3, masa_1, masa_2, masa_3):
    a1 = -G * masa_2 * (r1 - r2) / udaljenost(r1, r2)**3 - G * masa_3 * (r1 - r3) / udaljenost(r1, r3)**3
    a2 = -G * masa_1 * (r2 - r1) / udaljenost(r1, r2)**3 - G * masa_3 * (r2 - r3) / udaljenost(r2, r3)**3
    a3 = -G * masa_1 * (r3 - r1) / udaljenost(r1, r3)**3 - G * masa_2 * (r3 - r2) / udaljenost(r2, r3)**3

    return a1, a2, a3

def runge_kutta(r1, v1, r2, v2, r3, v3, masa_1, masa_2, masa_3, dt):
    # k1
    a1_1, a2_1, a3_1 = akceleracija(r1, r2, r3, masa_1, masa_2, masa_3)
    k1r1, k1v1 = v1, a1_1
    k1r2, k1v2 = v2, a2_1
    k1r3, k1v3 = v3, a3_1
    
    # k2
    a1_2, a2_2, a3_2 = akceleracija(r1 + 0.5 * dt * k1r1, r2 + 0.5 * dt * k1r2, r3 + 0.5 * dt * k1r3, masa_1, masa_2, masa_3)
    k2r1, k2v1 = v1 + 0.5 * dt * k1v1, a1_2
    k2r2, k2v2 = v2 + 0.5 * dt * k1v2, a2_2
    k2r3, k2v3 = v3 + 0.5 * dt * k1v3, a3_2

    # k3
    a1_3, a2_3, a3_3 = akceleracija(r1 + 0.5 * dt * k2r1, r2 + 0.5 * dt * k2r2, r3 + 0.5 * dt * k2r3, masa_1, masa_2, masa_3)
    k3r1, k3v1 = v1 + 0.5 * dt * k2v1, a1_3
    k3r2, k3v2 = v2 + 0.5 * dt * k2v2, a2_3
    k3r3, k3v3 = v3 + 0.5 * dt * k2v3, a3_3

    # k4
    a1_4, a2_4, a3_4 = akceleracija(r1 + dt * k3r1, r2 + dt * k3r2, r3 + dt * k3r3, masa_1, masa_2, masa_3)
    k4r1, k4v1 = v1 + dt * k3v1, a1_4
    k4r2, k4v2 = v2 + dt * k3v2, a2_4
    k4r3, k4v3 = v3 + dt * k3v3, a3_4

    novi_r1 = r1 + (dt/6) * (k1r1 + 2*k2r1 + 2*k3r1 + k4r1)
    novi_v1 = v1 + (dt/6) * (k1v1 + 2*k2v1 + 2*k3v1 + k4v1)

    novi_r2 = r2 + (dt/6) * (k1r2 + 2*k2r2 + 2*k3r2 + k4r2)
    novi_v2 = v2 + (dt/6) * (k1v2 + 2*k2v2 + 2*k3v2 + k4v2)

    novi_r3 = r3 + (dt/6) * (k1r3 + 2*k2r3 + 2*k3r3 + k4r3)
    novi_v3 = v3 + (dt/6) * (k1v3 + 2*k2v3 + 2*k3v3 + k4v3)

    return novi_r1, novi_v1, novi_r2, novi_v2, novi_r3, novi_v3

def simulacija(r0_1, v0_1, r0_2, v0_2, r0_3, v0_3, masa_1, masa_2, masa_3, naslov):
    r1 = np.zeros((koraci_simulacije, 3))
    v1 = np.zeros((koraci_simulacije, 3))

    r2 = np.zeros((koraci_simulacije, 3))
    v2 = np.zeros((koraci_simulacije, 3))

    r3 = np.zeros((koraci_simulacije, 3))
    v3 = np.zeros((koraci_simulacije, 3))

    #početni uvjeti
    r1[0] = r0_1
    v1[0] = v0_1
    
    r2[0] = r0_2
    v2[0] = v0_2

    r3[0] = r0_3
    v3[0] = v0_3

    #ažuriranje stanja
    for i in range(koraci_simulacije - 1):
        r1[i+1], v1[i+1], r2[i+1], v2[i+1], r3[i+1], v3[i+1] = runge_kutta(r1[i], v1[i], r2[i], v2[i], r3[i], v3[i], masa_1, masa_2, masa_3, dt)

    #graf
    fig = plt.figure()
    ax = fig.add_subplot(projection = "3d")

    ax.plot(r1[:,0], r1[:,1], r1[:,2], color="red", linewidth = 1, label="Tijelo 1")
    ax.plot(r2[:,0], r2[:,1], r2[:,2], color="blue", linewidth = 1, label="Tijelo 2")
    ax.plot(r3[:,0], r3[:,1], r3[:,2], color="green", linewidth = 1, label="Tijelo 3")

    ax.set_title(naslov)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_box_aspect([1, 1, 1])
    ax.legend()

# 1.slučaj
simulacija(
    np.array([-1000, 0, -500]), np.array([0, -5, 1]),
    np.array([0, 1000, 0]), np.array([5, 0, -1]),
    np.array([1000, 0, 500]), np.array([0, 5, 1]),
    1e15, 1e15, 1e15, "Sustav tijela jednakih masa"
)

# 2.slučaj
simulacija(
    np.array([-1000, 500, -400]), np.array([1, -4, 1]),
    np.array([500, 1000, 300]), np.array([4, -1, -1]),
    np.array([1200, -800, 200]), np.array([-3, 2, 1]),
    1e15, 1.5e15, 2e15, "Kaotični sustav"
)

# 3.slučaj
simulacija(
    np.array([0, 0, 0]), np.array([0, 0, 0]),
    np.array([2000, 0, 200]), np.array([0, 58, 0]),
    np.array([-3000, 0, -400]), np.array([0, -47, 0]),
    1e17, 1e15, 1e15, "Hijerarhijski sustav"
)

plt.show()