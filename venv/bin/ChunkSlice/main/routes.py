from flask import Blueprint, render_template, redirect, request, url_for
from ChunkSlice.extensions import mongo
from ChunkSlice.static.py.show import showSTL
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
    return mongo.send_file(file_name)

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

    showSTL()

    return render_template('show.html', file = file)


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
    file = chunk_collection.find({'name': stl_name})
    chunk_collection.delete_one({'name': stl_name})
    return redirect(url_for('main.list'))