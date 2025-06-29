from flask import Flask, render_template, request, jsonify
from pymatgen.core import Structure
from pymatgen.analysis.local_env import CrystalNN
import os

app = Flask(__name__)

# 🔒 Absolute path to this app.py's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    element = data.get('element')

    cif_path = os.path.join(BASE_DIR, 'cif', f'{element}.cif')

    print("Looking for CIF at:", cif_path)

    if not os.path.exists(cif_path):
        return jsonify({'error': f'CIF file for {element} not found at {cif_path}.'})

    try:
        structure = Structure.from_file(cif_path)
        cnn = CrystalNN()
        neighbors = cnn.get_nn_info(structure, 0)
        distances = [round(n['weight'], 3) for n in neighbors]

        return jsonify({
            'symbol': structure[0].species_string,
            'coordination': len(neighbors),
            'distances': distances,
            'lattice': structure.lattice.__class__.__name__,
            'density': round(structure.density, 3)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
