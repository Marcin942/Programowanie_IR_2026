from vector import Vector2D
import matplotlib.pyplot as plt

class PointMass:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.trajectory = []

    def update(self, F, dt):
        self.trajectory.append(self.position)
        self.velocity = self.velocity + (F * (1 / self.mass) * dt)
        self.position = self.position + (self.velocity * dt)


# #Rzut ukośny   
p = PointMass(1, Vector2D(0,0), Vector2D(1,1))
g = Vector2D(0, -9.81)
dt = 0.01
while p.position.y >= 0:
    p.update(g * p.mass, dt)
plt.plot([r.x for  r in p.trajectory], [r.y for r in p.trajectory])
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Oscylator harmoniczny
p = PointMass(1, Vector2D(0, 1), Vector2D(1, 0))
k = 10.0
dt = 0.01
for _ in range(1000):
    force = p.position * (- k)
    p.update(force, dt)
plt.plot([r.x for  r in p.trajectory])
plt.plot([r.y for  r in p.trajectory])
plt.show()