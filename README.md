# Mobius-strip


### 3D plot  

![Screenshot 2025-05-27 092102](https://github.com/user-attachments/assets/5612bf93-58dc-4541-bdc4-d77387840a1b)


### How you structured the code

---

#### 1. `MobiusStrip` Class (Encapsulation)

All logic is modularized within a single class for reusability and clarity.

```python
class MobiusStrip:
    def __init__(self, R, w, n): ...
```

---

#### 2. Mesh Generation (`_generate_mesh`)

Implements the parametric equations to generate the 3D surface grid.

```python
def _generate_mesh(self):
    x = (R + v⋅cos(u/2))⋅cos(u)
    y = (R + v⋅cos(u/2))⋅sin(u)
    z = v⋅sin(u/2)
```

---

#### 3. Surface Area Calculation (`compute_surface_area`)

Uses numerical approximation via the cross product of partial derivatives and integrates using `scipy.integrate.simpson`.

---

#### 4. Edge Length Calculation (`compute_edge_length`)

Samples points along the boundary at `v = w/2`, computes differential arc lengths, and integrates.

---

#### 5. Visualization (`plot`)

Renders a 3D plot using `matplotlib` for visual verification of the modeled Möbius strip.

---

#### 6. Main Execution Block (`if __name__ == "__main__":`)

For testing the class: instantiates an object, prints computed values, and shows the plot.

---
###  How I Approximated the Surface Area:

---

#### Step 1: Parametric Surface

The Möbius strip is defined parametrically as:

* $x(u,v), y(u,v), z(u,v)$
* With parameters $u \in [0, 2\pi],\ v \in [-w/2, w/2]$

---

#### Step 2: Compute Partial Derivatives

Numerically compute:


* Done using `np.gradient()` on meshgrid arrays $X, Y, Z$

---

#### Step 3: Cross Product of Tangents

Surface element $dS$ is the magnitude of:


---

#### Step 4: Numerical Integration

Apply **Simpson’s Rule** twice (along `v` then `u`) using `scipy.integrate.simpson`:

```python
area = simpson(simpson(dS, v), u)
```

---
### Challenges Faced

---

#### 1. Handling `scipy` Import Errors

* Initially used `simps` (deprecated in newer versions).
* Fixed by switching to `simpson` from `scipy.integrate`.

---

#### 2. Numerical Stability

* Computing partial derivatives with `np.gradient()` needed a sufficiently high resolution (`n ≥ 100`) for accurate surface area.
* Low `n` values led to jagged surfaces and poor area estimates.

---

#### 3. Edge Calculation

* Boundary curve is not trivial due to twisting.
* Required evaluating the parametric equations at `v = ±w/2` and applying numerical differentiation carefully.

---

#### 4. Visualization Orientation

* Plotting the Möbius strip needed tuning `matplotlib`’s 3D projection for clarity (especially for wide strips).

---

#### 5. Mesh Symmetry

* Mesh grid generation had to respect the non-orientable nature of the Möbius strip to avoid visual artifacts or mismatched derivatives.


