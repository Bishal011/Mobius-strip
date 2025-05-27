import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import simpson  # Updated import

class MobiusStrip:
    def __init__(self, R=1, w=0.5, n=100):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        U, V = self.U, self.V
        R = self.R
        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def compute_surface_area(self):
        # Compute partial derivatives
        dXu = np.gradient(self.X, axis=1)
        dXv = np.gradient(self.X, axis=0)
        dYu = np.gradient(self.Y, axis=1)
        dYv = np.gradient(self.Y, axis=0)
        dZu = np.gradient(self.Z, axis=1)
        dZv = np.gradient(self.Z, axis=0)

        # Compute cross product of partial derivatives
        cross_x = dYu * dZv - dZu * dYv
        cross_y = dZu * dXv - dXu * dZv
        cross_z = dXu * dYv - dYu * dXv

        # Magnitude of cross product = differential surface element
        dS = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

        # Numerical integration over v and u using Simpson's rule
        area = simpson(simpson(dS, self.v), self.u)
        return area

    def compute_edge_length(self):
        # Boundary at v = w/2
        v_edge = self.w / 2
        u = self.u
        x = (self.R + v_edge * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v_edge * np.cos(u / 2)) * np.sin(u)
        z = v_edge * np.sin(u / 2)

        # Arc length approximation
        dx = np.gradient(x)
        dy = np.gradient(y)
        dz = np.gradient(z)
        ds = np.sqrt(dx**2 + dy**2 + dz**2)

        length = simpson(ds, u)
        return length

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none')
        ax.set_title("Mobius Strip")
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    mobius = MobiusStrip(R=1, w=0.5, n=200)
    area = mobius.compute_surface_area()
    length = mobius.compute_edge_length()

    print(f"Approximate Surface Area: {area:.5f}")
    print(f"Approximate Edge Length: {length:.5f}")

    mobius.plot()
