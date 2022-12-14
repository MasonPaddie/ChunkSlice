from flask import Blueprint, render_template, redirect, request, url_for
from ChunkSlice.extensions import mongo
from ChunkSlice.static.py.show import *
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

# Default route
@main.route('/home')
def index():
    return render_template('index.html')

# List route
@main.route('/list')
def list():
    chunk_collection = mongo.db.chunkslice
    files = chunk_collection.find()
    return render_template('list.html', files = files)

# STL Route
@main.route('/stl/<file_name>')
def stl(file_name):
    chunk_collection = mongo.db.chunkslice
    fs_file = mongo.db.fs.files.find({'filename': file_name})
    return mongo.send_file(fs_file)

# Create route
@main.route('/create', methods=['POST'])
def create():
    chunk_collection = mongo.db.chunkslice
    file = request.files['myfile']
    mongo.save_file(secure_filename(file.filename), file)
    chunk_collection.insert_one({'file': str(file.filename), 'name': request.form.get('stl_name')})
    return redirect(url_for('main.show', stl_name = request.form.get('stl_name')))

# Show Route
@main.route('/show/<stl_name>')
def show(stl_name):
    chunk_collection = mongo.db.chunkslice
    file = chunk_collection.find({'name': stl_name})

    return render_template('show.html', file = file)

# Function to show the graph on the show page
@main.route('/show/<stl_name>', methods=["POST", "GET"])
def show_graph(stl_name):
    chunk_collection = mongo.db.chunkslice
    file = chunk_collection.find_one({'name': stl_name})

    # Handles buttons
    # Bring up the graph corresponding to the button pressed
    [x_len, y_len, z_len, vol] = ["Enter a Height for the Model", "Enter a Height for the Model", "Enter a Height for the Model", "Enter a Height for the Model"]
    # Graph for 3D model 
    if request.method == "POST" and request.form['graph'] == 'stl':
        showSTL(file['file'])

    # Graph for plotting points    
    elif request.form['graph'] == 'points':
         [x_len, y_len, z_len, vol] = get_points(file['file'], int(request.form['des_h']))

    # Graph for plotting cubes    
    elif request.form['graph'] == 'cubes':
         [x_len, y_len, z_len, vol] = get_cubes(file['file'], int(request.form['des_h']))

    # Graph for plotting 2D cross section    
    elif request.form['graph'] == 'cross_section':
        [x_len, y_len, z_len, vol] = plot_section(file['file'], int(request.form['des_h']), int(request.form['layer']))

    return render_template('show.html', file = chunk_collection.find({'name': stl_name}), x_len = x_len, y_len = y_len, z_len = z_len, vol = vol)

# Edit Route
@main.route('/edit/<stl_name>', methods=['GET','POST'])
def edit(stl_name):
    chunk_collection = mongo.db.chunkslice
    file = chunk_collection.find({'name': stl_name})
    
    if request.method == 'POST':
        chunk_collection.update_one({'name': stl_name},{'$set': {"name": request.form.get('new_stl_name')}})
        return redirect(url_for('main.show', stl_name = request.form.get('new_stl_name')))
    else:
        return render_template('edit.html', file = file)

# Delete route
@main.route('/delete/<stl_name>', methods=['POST'])
def delete(stl_name):
    chunk_collection = mongo.db.chunkslice
    chunk_collection.delete_one({'name': stl_name})
    return redirect(url_for('main.list'))

if __name__ == '__main__':
    main.run_server(debug=True)