# Visualizing the Electric Field using Vector Fields and Field Lines

This repository has two different scripts, one that expresses the Electric Field in a Vector field while the other has a visual of the curvature of the field.

📘 [Read the Theory Notebook](./docs/Electrostatics_Theory.ipynb)

## 📷 Preview of the curvature of the Electric Field
![image](https://github.com/user-attachments/assets/a9e184a5-89e9-4791-a389-7464d91d5459)

## 🚀 Features
- Discretizes a charged ring
- Calculates 3D electric field vectors
- Visualizes field lines with Mayavi

## 🛠 Requirements
- Python 3.10+ Link: https://www.python.org/downloads/
- Mayavi
- NumPy
- PyQt5
- Pyface
- (Optional but preferable) Anaconda Link: https://www.anaconda.com/download

## 📦 Installation

When using Anaconda, insert the prompts below. Have not found a consistent way to use pip on windows without it causing a massive headache.

```bash
conda create -n electricfield-env python=3.10
conda activate electricfield-env
conda install -c conda-forge mayavi pyface pyqt numpy
```

## ▶️ Usage

Once you've installed the required environment (see above), follow these steps:

1. **Download the script** (`Electric.Field.Lines.for.Circular.Loop.py`) and place it somewhere easy to find — for example: Your Downloads folder 📂
2. **Open Anaconda Prompt** and activate your environment:

```bash
conda activate electricfield-env
```
3. Copy the directory of where your script is located. I perfer to copy as path as shown in the image below
![image](https://github.com/user-attachments/assets/3750e402-d1b2-4753-87b0-2775b43bf315)

4. Insert the following prompt. Note: Your path will be slightly different.
```bash
python "C:\Users\YourUsername\Downloads\Electric.Field.Lines.for.Circular.Loop.py"
```
5. You will be prompted on the following:
- Radius of the ring
- Line Charge density
- Number of points to discretize the ring
- Number of samples for the field in x, y, z directions

6. Enjoy the simulation 😁

---

## ⚡ Visualize Electric Fields Using Matplotlib (Vector Plot)

This script focuses primarily on showcasing the vector field of an Electric Field

---

### 🖼️ Preview of the Vector Field
![image](https://github.com/user-attachments/assets/f34bd111-e22a-4954-9e6e-02fe0fc23ae3) ![image](https://github.com/user-attachments/assets/60b18b13-43fb-4733-b13c-ecc68e023bd1)

---

### 🚀 Features

- Discretizes a charged ring
- Calculates 3D electric field vectors
- Visualizes vectors with `matplotlib.pyplot.quiver`

---

### 📦 Requirements

- Python 3.10+ Link: https://www.python.org/downloads/
- NumPy
- Matplotlib
- Tkinter (included with Python)
- (Optional but preferable) Anaconda Link: https://www.anaconda.com/download

---

### 🛠 Installation
When using Anaconda, insert the prompts below.
```bash
conda create -n electricfield-mpl python=3.10
conda activate electricfield-mpl
conda install numpy matplotlib
```
## ▶️ Usage

Once you've installed the required environment (see above), follow these steps:

1. **Download the script** (`Electric.Vector.lines.for.Circular.Loop.py`) and place it somewhere easy to find — for example: Your Downloads folder 📂
2. **Open Anaconda Prompt** and activate your environment:

```bash
conda activate electricfield-mpl
```
3. Copy the directory of where your script is located. I perfer to copy as path as shown in the image below
![image](https://github.com/user-attachments/assets/3750e402-d1b2-4753-87b0-2775b43bf315)

4. Insert the following prompt. Note: Your path will be slightly different.
```bash
python "C:\Users\YourUsername\Downloads\Electric.Vector.lines.for.Circular.Loop.py"
```
5. You will be prompted on the following:
- Radius of the ring
- Line Charge density
- Number of points to discretize the ring
- Number of samples for the field in x, y, z directions

6. Enjoy the simulation 😁
(Tip: You can zoom and rotate for better view of the field)

---
