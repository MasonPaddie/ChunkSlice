def showSTL(file_name):
    import vtkplotlib as vpl
    from stl.mesh import Mesh
    from flask import url_for

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file(file_name)

    # Plot the mesh
    vpl.mesh_plot(mesh)

    # Show the figure
    vpl.show()
