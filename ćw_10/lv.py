import numpy as np
import matplotlib.pyplot as plt
a = 1.
b = 0.1
c = 0.1
d = 1
x0 = 10
y0 = 5
tmax = 20
dt = 0.01

def lotka_volterra(a, b, c, d, x0, y0, tmax, dt):

    t = np.arange(0, tmax, dt)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    x[0] = x0
    y[0] = y0

    for i in range(1, len(t)):
        x_prev = x[i-1]
        y_prev = y[i-1]

        k1_x = a * x_prev - b * x_prev * y_prev
        k1_y = c * x_prev * y_prev - d * y_prev

        k2_x = a * (x_prev + dt/2 * k1_x) - b * (x_prev + dt/2 * k1_x) * (y_prev + dt/2 * k1_y)
        k2_y = c * (x_prev + dt/2 * k1_x) * (y_prev + dt/2 * k1_y) - d * (y_prev + dt/2 * k1_y)

        k3_x = a * (x_prev + dt/2 * k2_x) - b * (x_prev + dt/2 * k2_x) * (y_prev + dt/2 * k2_y)
        k3_y = c * (x_prev + dt/2 * k2_x) * (y_prev + dt/2 * k2_y) - d * (y_prev + dt/2 * k2_y)

        k4_x = a * (x_prev + dt * k3_x) - b * (x_prev + dt * k3_x) * (y_prev + dt * k3_y)
        k4_y = c * (x_prev + dt * k3_x) * (y_prev + dt * k3_y) - d * (y_prev + dt * k3_y)

        x[i] = x_prev + (dt / 6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        y[i] = y_prev + (dt / 6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)

    return t, x, y


t, x, y = lotka_volterra(a, b, c, d, x0, y0, tmax, dt)

plt.plot(t, x, label="x")
plt.plot(t, y, label="y")
plt.xlabel("t")
plt.ylabel("Liczebność populacji")
plt.legend()
plt.show()