import numpy as np
import matplotlib.pyplot as plt

def BallVolume(n, N):

    # Generujemy N punktów, z których każdy ma n współrzędnych z przedziału [-1,1]
    coordinates = np.random.uniform(-1, 1, size=(N, n))
    
    # Obliczamy kwadraty odległości od środka dla każdego punkty
    distances_squared = np.sum(coordinates**2, axis=1)
    
    # Liczymy ile punktów znajduje się wewnątrz kuli jednostkowej
    n_inside = np.sum(distances_squared <= 1)
    
    # Objętość n-wymiarowego sześcianu
    cube_volume = 2 ** n
    
    # Oszacowanie objętości kuli
    estimated_volume =  cube_volume * (n_inside / N)
    return estimated_volume


N = 100000
n_values = np.arange(1, 10) # n = 1, ..., 10

volumes = np.array([BallVolume(n, N) for n in n_values])

plt.scatter(n_values, volumes)
plt.xlabel('n')
plt.ylabel('objętość kuli n-wymiarowej')
plt.show()