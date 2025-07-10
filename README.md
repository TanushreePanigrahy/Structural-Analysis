# 🧱 Crystal Structure Visualization and Analysis using Python

This project explores and visualizes basic crystal structures (FCC, BCC, HCP) using Python-based computational tools. It performs analysis on lattice parameters, coordination numbers, and theoretical densities using both built-in functions and real crystallographic data.


## 🚀 Features

- 📐 Generate unit cell structures (FCC, BCC, HCP) using ASE
- 📊 Analyze lattice parameters and unit cell volumes
- 🔍 Calculate theoretical densities using physical principles
- 🧪 Determine coordination number using `pymatgen`
- 🌐 Interactive 3D visualization of atomic structures using `nglview`
- 

## 🛠️ Tech Stack

- [ASE](https://wiki.fysik.dtu.dk/ase/) – Atomic Simulation Environment
- [pymatgen](https://pymatgen.org/) – Python Materials Genomics
- [nglview](http://nglviewer.org/nglview/) – 3D atomic structure viewer
- Jupyter Notebook / VS Code


## 📂 Folder Structure
1. cif/
   - Al_fcc.cif
   - Fe_bcc.cif
   - Mg_hcp.cif
2. templates/
   - index.html
4. structure_analysis.ipynb
5. app.py
6. README.md

## 🔧 How it Works

### `index.html`

- Located in the `templates/` folder
- Provides a simple UI where the user can:
  - Select a material from a dropdown (Al, Fe, Mg)
  - Click **Analyze**
- Sends a POST request to `/analyze` using JavaScript
- Displays the returned structural data dynamically on the same page

### `app.py`

- A Flask web server with two routes:
  - `/` — Renders the HTML page
  - `/analyze` — Accepts a material name (e.g., "Al"), loads the corresponding `.cif` file, and:
    - Uses `pymatgen` to parse the structure
    - Uses `CrystalNN` to determine coordination number and nearest neighbors
    - Computes density and lattice information
- Returns all this info as a JSON response

  ![2025-06-29](https://github.com/user-attachments/assets/47f33401-f139-4fc8-bc5f-1ad8c7d86fe8)
  works on http://127.0.0.1:5000/


📘 Learning Outcomes

- Understand atomic packing in common crystal structures
- Apply computational tools to perform basic materials analysis
- Practice working with .cif files and unit cell visualization
- Learn scientific computation using open-source Python tools

📌 Future Improvements

- Add band structure / DOS calculations using DFT codes
- Include thermal expansion and stress analysis
- Create an interactive Streamlit or web interface
