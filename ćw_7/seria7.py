class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, vector2d):
            return NotImplemented
        return vector2d(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, vector2d):
            return NotImplemented
        return vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, vector2d):
            return vector2d(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float, complex)):
            return vector2d(self.x * other, self.y * other)
        else:
            return NotImplemented
    
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float, complex)):
            return vector2d(self.x / scalar, self.y / scalar)
        else:
            return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"vector2d({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, vector2d):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
class pointmass:
    __g__ = vector2d(0, -9.81) #w [m/s^2]

    def __init__(self, mass, position, velocity, ground_level=-float('inf')):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.trajectory = []
        self.ground_level = ground_level

        if not isinstance(position, vector2d) or not isinstance(velocity, vector2d):
            raise TypeError("position and velocity must be of type vector2d")

    def __repr__(self):
        return (
            f"pointmass(mass={self.mass}, position={repr(self.position)}, "
            f"velocity={repr(self.velocity)})"
        )
    
    def step(self, dt: float, force = vector2d(0, 0)):

        if (self.trajectory.count(self.position) == 0):
            self.trajectory.append(self.position)

        acceleration = force / self.mass
        self.velocity += (self.__g__ + acceleration) * dt

        self.position += self.velocity * dt

        if self.position.y < self.ground_level:
            self.position.y = self.ground_level
            self.velocity.y = 0
            

        self.trajectory.append(self.position)


def plot(trajectory, axis, dt):
    import matplotlib.pyplot as plt
    
    if axis is None:
        axis = "x"
    axis = axis.lower()
    if axis not in ("x", "y"):
        axis = "x"

    x_values = [i * dt for i, pos in enumerate(trajectory)]
    
    y_values = None
    for pos in trajectory:
        if axis == "x":
            if y_values is None:
                y_values = []
            y_values.append(pos.x)
        elif axis == "y":
            if y_values is None:
                y_values = []
            y_values.append(pos.y)


    plt.plot(x_values, y_values)
    plt.title("Trajektoria")
    plt.xlabel("Czas (s)")
    plt.ylabel("Położenie w osi " + axis.capitalize() + " (m)")
    plt.grid()
    plt.show()


def plot_trajectory(trajectory):
    import matplotlib.pyplot as plt

    x_values = [pos.x for pos in trajectory]
    y_values = [pos.y for pos in trajectory]

    plt.plot(x_values, y_values)
    plt.title("Trajektoria")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.grid()
    plt.show()


def plot_trajectory_realtime(trajectory, interval=0.01, scale_interval=5.0):
    import matplotlib.pyplot as plt
    import math

    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot([], [], "b-")
    current_point, = ax.plot([], [], "ro")

    ax.set_title("Trajektoria (realtime)")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.grid(True)
    time_text = ax.text(0.02, 0.95, "t = 0.00 s", transform=ax.transAxes, va="top")
    velocity_text = ax.text(0.02, 0.90, "v = 0.00 m/s", transform=ax.transAxes, va="top")

    x_values = []
    y_values = []

    points_per_scale = max(1, int(scale_interval / interval))

    def _set_scale(start_idx):
        end_idx = min(len(trajectory), start_idx + points_per_scale)
        future = trajectory[start_idx:end_idx]
        if not future:
            return

        future_x = [p.x for p in future]
        future_y = [p.y for p in future]

        x_min, x_max = min(future_x), max(future_x)
        y_min, y_max = min(future_y), max(future_y)

        x_pad = max(1e-6, (x_max - x_min) * 0.1)
        y_pad = max(1e-6, (y_max - y_min) * 0.1)

        ax.set_xlim(x_min - x_pad, x_max + x_pad)
        ax.set_ylim(y_min - y_pad, y_max + y_pad)

    for i, pos in enumerate(trajectory):
        if i % points_per_scale == 0:
            _set_scale(i)

        x_values.append(pos.x)
        y_values.append(pos.y)

        line.set_data(x_values, y_values)
        current_point.set_data([pos.x], [pos.y])
        time_text.set_text(f"t = {i * interval:.2f} s")
        if i == 0:
            velocity = 0.0
        else:
            dx = trajectory[i].x - trajectory[i - 1].x
            dy = trajectory[i].y - trajectory[i - 1].y
            velocity = math.sqrt(dx * dx + dy * dy) / interval
        velocity_text.set_text(f"v = {velocity:.2f} m/s")
        plt.pause(interval)

    plt.ioff()
    plt.show()
    
if __name__ == "__main__":
    #Rzut_ukośny
    mass = 1.0
    dt = 0.01
    initial_position = vector2d(0, 0)
    pocisk_initial_velocity = vector2d(10, 10)
    pocisk = pointmass(mass, initial_position, pocisk_initial_velocity, ground_level=0)

    
    for _ in range(1000):
        pocisk.step(dt)

    plot(pocisk.trajectory, dt=dt, axis="y")
    #plot_trajectory_realtime(pocisk.trajectory)

    #Drgania harmoniczne
    drgania__initial_velocity = vector2d(10, 0)
    drgania = pointmass(mass, initial_position, drgania__initial_velocity, ground_level=0)
    for i in range(1000):
        force = vector2d(-drgania.position.x, 0) * 20
        drgania.step(dt, force)

    plot(drgania.trajectory, dt=dt, axis="x")

    #

    

