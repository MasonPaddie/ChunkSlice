# import vtkplotlib as vpl
# from stl.mesh import Mesh

# def foo():
#     print('I am a python!')
#     import numpy 
#     from stl import mesh
#     from matplotlib import pyplot

#     # Create a new plot
#     figure = pyplot.figure()
#     axes = mplot3d.Axes3D(figure)

#     # Load the STL files and add the vectors to the plot
#     your_mesh = mesh.Mesh.from_file(url_for('main.stl', file_name = file.name))
#     axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

#     # Auto scale to the mesh size
#     scale = your_mesh.points.flatten()
#     axes.auto_scale_xyz(scale, scale, scale)

#     # Show the plot to the screen
#     pyplot.show()

def showSTL(path):
    import vtkplotlib as vpl
    from stl.mesh import Mesh

    # Read the STL using numpy-stl
    mesh = Mesh.from_file(path)

    # Plot the mesh
    vpl.mesh_plot(mesh)

    # Show the figure
    vpl.show()
