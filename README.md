# 🧱 Crystal Structure Visualization and Analysis using Python

This project explores and visualizes basic crystal structures (FCC, BCC, HCP) using Python-based computational tools. It performs analysis on lattice parameters, coordination numbers, and theoretical densities using both built-in functions and real crystallographic data.

---

## 🚀 Features

- 📐 Generate unit cell structures (FCC, BCC, HCP) using ASE
- 📊 Analyze lattice parameters and unit cell volumes
- 🔍 Calculate theoretical densities using physical principles
- 🧪 Determine coordination number using `pymatgen`
- 🌐 Interactive 3D visualization of atomic structures using `nglview`

---

## 🛠️ Tech Stack

- [ASE](https://wiki.fysik.dtu.dk/ase/) – Atomic Simulation Environment
- [pymatgen](https://pymatgen.org/) – Python Materials Genomics
- [nglview](http://nglviewer.org/nglview/) – 3D atomic structure viewer
- Jupyter Notebook / VS Code

---

## 📂 Folder Structure
1. data/
   - Al_fcc.cif
   - Fe_bcc.cif
   - Mg_hcp.cif
2. structure_analysis.ipynb
3. README.md

How to run?
pip install ase pymatgen nglview matplotlib


📘 Learning Outcomes

- Understand atomic packing in common crystal structures
- Apply computational tools to perform basic materials analysis
- Practice working with .cif files and unit cell visualization
- Learn scientific computation using open-source Python tools

📌 Future Improvements

- Add band structure / DOS calculations using DFT codes
- Include thermal expansion and stress analysis
- Create an interactive Streamlit or web interface
