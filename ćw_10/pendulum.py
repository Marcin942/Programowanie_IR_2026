import numpy as np
import matplotlib.pyplot as plt
g = 9.81
l = 1
theta0 = 0.01
omega0 = 0.0
tmax = 10
dt = 0.01

def pendulum_euler(l, theta0, omega0, tmax, dt):
    t = np.arange(0, tmax, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        omega[i] = omega[i-1] - (g / l) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i-1] * dt

    return t, theta, omega


def pendulum_rk4(l, theta0, omega0, tmax, dt):
    t = np.arange(0, tmax, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        k1_theta = omega[i-1]
        k1_omega = -(g / l) * np.sin(theta[i-1])

        k2_theta = omega[i-1] + k1_omega * dt / 2
        k2_omega = -(g / l) * np.sin(theta[i-1] + k1_theta * dt / 2)

        k3_theta = omega[i-1] + k2_omega * dt / 2
        k3_omega = -(g / l) * np.sin(theta[i-1] + k2_theta * dt / 2)

        k4_theta = omega[i-1] + k3_omega * dt
        k4_omega = -(g / l) * np.sin(theta[i-1] + k3_theta * dt)

        theta[i] = theta[i-1] + (dt / 6) * (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta)
        omega[i] = omega[i-1] + (dt / 6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)

    return t, theta, omega


t, theta, omega = pendulum_euler(l, theta0, omega0, tmax, dt)
#t, theta, omega = pendulum_rk4(l, theta0, omega0, tmax, dt)


plt.plot(t, theta, label="theta")
plt.plot(t, omega, label="omega")
plt.xlabel("t")
plt.legend()
plt.show()

plt.plot(theta, omega)
plt.xlabel("theta")
plt.ylabel("omega")
plt.show()


