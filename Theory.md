# 📐 Theory – Electric Field from a Uniformly Charged Ring

This document explains the physics and mathematics behind the electric field simulations shown in this project.

---

## 🧲 Physical Setup

Consider this **uniformly charged circular ring**:

- Lies in the **x–y plane** (at `z = 0`)
- Centered at the origin
- Radius: `a`
- Constant **line charge density**: `ρₗ` (in C/m)

---

## ⚡ Electric Field Expression

The electric field `E` due to a **continuous line charge** is given by:


Where:

- `R` is the vector from the charge element to the observation point
- `R̂` is the unit vector of `R` (i.e., `R / |R|`)
- `dl` is the differential element of arc length along the ring
- `ε₀` is the vacuum permittivity (≈ 8.85 × 10⁻¹² F/m)

---

## 🔢 Numerical Approximation

To simulate this in Python, we **discretize the ring into N small segments**, and approximate the integral with a summation:


Where:

- `Rᵢ` is the displacement vector from segment `i` to the observation point
- `|Rᵢ|` is the magnitude of that vector
- `Δlᵢ` is the length of each segment (`Δl = 2πa / N`)

This approach treats the ring as a series of tiny straight wire segments, each contributing to the total electric field at a given point.

---

## 🧮 Implementation Strategy

- Compute the `x`, `y` positions of `N` segments on the ring
- For each sample point in 3D space, calculate vector contributions from all segments
- Sum the contributions to find the resulting electric field vector at that point

The code supports visualization through:

- **Mayavi** for electric field streamlines
- **Matplotlib** for 3D vector fields (`quiver`)

---

## 💡 Example Parameters

- Radius: `a = 0.05 m`
- Line charge density: `ρₗ = 10 C/m`
- Discretization: `N = 100` segments
- Sample grid: `15 × 15 × 15` points across 3D space

---

## 📊 What the Plots Represent

Each arrow in the 3D plots shows the **direction and magnitude** of the electric field at a sample point.

- In the **Mayavi plot**, field lines show continuous flow and curvature.
- In the **Matplotlib plot**, `quiver` arrows represent field vectors directly.

These visualizations reveal the symmetry and behavior of fields in space — especially how the field focuses along the z-axis above the ring’s center.

---

## 🔁 Ideas for Extension

- Add electric potential (`V`) visualization
- Stack multiple rings or add point charges
- Compare field behavior for different charge distributions


