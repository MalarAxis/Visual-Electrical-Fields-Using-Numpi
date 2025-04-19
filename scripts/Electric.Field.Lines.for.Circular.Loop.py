import numpy as np
import os
os.environ["QT_API"] = "pyqt5"

# Import the pyface.qt backend before importing mayavi
import pyface.qt

from mayavi import mlab
import tkinter as tk
from tkinter import simpledialog

# Constants
k = 8.9875517923e9  # Coulomb's constant (N m^2 C^-2)

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()

# User Inputs with simpledialog
a = float(simpledialog.askfloat("Input", "Enter the radius of the circular ring (m):"))
rho_l = float(simpledialog.askfloat("Input", "Enter the line charge density (C/m):"))
num_points = int(simpledialog.askinteger("Input", "Enter the number of points to discretize the circular ring:"))
num_samples = int(simpledialog.askinteger("Input", "Enter the number of samples for the electric field in x, y, and z directions:"))

# Discretize the circular ring
theta = np.linspace(0, 2 * np.pi, num_points)
x_ring = a * np.cos(theta)
y_ring = a * np.sin(theta)

# Calculate the electric field for a given point
def electric_field(x, y, z):
    Ex, Ey, Ez = 0, 0, 0
    for i in range(num_points):
        dx, dy, dz = x - x_ring[i], y - y_ring[i], z
        r = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        dEx, dEy, dEz = k * rho_l * (dx / r ** 3), k * rho_l * (dy / r ** 3), k * rho_l * (dz / r ** 3)
        Ex += dEx / num_points
        Ey += dEy / num_points
        Ez += dEz / num_points
    return np.array([Ex, Ey, Ez])

# Create a 3D grid of points to sample the electric field
x = np.linspace(-2 * a, 2 * a, num_samples)
y = np.linspace(-2 * a, 2 * a, num_samples)
z = np.linspace(-2 * a, 2 * a, num_samples)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Calculate the electric field at each point
E = np.vectorize(electric_field, signature='(),(),()->(n)')(X, Y, Z)
Ex, Ey, Ez = E[..., 0], E[..., 1], E[..., 2]

# Plot the 3D electric field lines
fig = mlab.figure(size=(800, 800))
field_lines = mlab.flow(X, Y, Z, Ex, Ey, Ez, seed_scale=2, seed_resolution=10, integration_direction='both')
charges = mlab.points3d(x_ring, y_ring, np.zeros_like(x_ring), scale_factor=a * 0.1, color=(1, 0, 0), mode='sphere')

# Draw the x, y, and z axes
mlab.outline(extent=(-2 * a, 2 * a, -2 * a, 2 * a, -2 * a, 2 * a), color=(0, 0, 0))
mlab.axes(extent=(-2 * a, 2 * a, -2 * a, 2 * a, -2 * a, 2 * a), xlabel='X', ylabel='Y', zlabel='Z', nb_labels=5, color=(0, 0, 0))

mlab.show()