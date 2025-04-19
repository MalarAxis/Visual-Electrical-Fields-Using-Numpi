# Visual-Electrical-Fields-Using-Numpi
This project will contist of building upon the vector program I created

This repository has two different scripts, one that expresses the Electric Field in a Vector field while the other has a visual of the curvature of the field.

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

