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

def get_points(file_name):
    import vtkplotlib as vpl
    from stl.mesh import Mesh
    from flask import url_for

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file(file_name)

    plot = vpl.mesh_plot(mesh, scalars=mesh.z)
    
    # Optionally the plot created by mesh_plot can be passed to color_bar
    vpl.color_bar(plot, "Heights")
    vpl.show()
    print(mesh.y)