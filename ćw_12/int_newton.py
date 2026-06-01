import numpy as np
import matplotlib.pyplot as plt

def IntRectangular(f, a, b, N):

    h = (b - a) / N  # szerokość każdego przdziału
    integral_sum = 0

    for i in range(0, N):
        midpoint = a + (i + 0.5) * h  # środek przedziału
        integral_sum += h * f(midpoint)

    return integral_sum

def IntTrapezoidal(f, a, b, N):

    h = (b - a) / N  # szerokość każdego przdziału
    integral_sum = 0

    for i in range(0, N):
        x_left = a + i * h #lewy koniec przedziału
        x_right = a + (i+1) * h # prawy koniec przedziału  

        integral_sum += h * (f(x_left) + f(x_right)) / 2

    return integral_sum


def f(t):
    return 1/t

N = 1000 # liczba przedziałów

int_rect = np.array([])
int_trapz = np.array([])
x_range = np.linspace(1,10)

for x in x_range:
    int_rect = np.append(int_rect, IntRectangular(f, 1, x, N))
    int_trapz = np.append(int_trapz, IntTrapezoidal(f, 1, x, N))

plt.scatter(x_range, int_rect)
plt.scatter(x_range, int_trapz)
plt.xlabel('x')
plt.ylabel(f'$\int_1^x f(t)dt$')
plt.show()