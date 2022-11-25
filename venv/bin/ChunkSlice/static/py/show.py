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
    import numpy as np
    from stl.mesh import Mesh
    from flask import url_for

    # # Read the STL using numpy-stl
    # # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    # mesh = Mesh.from_file(file_name)

    # plot = vpl.mesh_plot(mesh, scalars=mesh.z)
    
    # # Optionally the plot created by mesh_plot can be passed to color_bar
    # vpl.color_bar(plot, "Heights")
    # vpl.show()
    # print(mesh.y)

    polydata = vpl.PolyData()

    polydata.points = np.array([[0, 0, 0],
                                [1, 0, 0],         
                                [1, 1, 0],
                                [0, 1, 0],
                                [0, 0, 1],
                                [1, 0, 1],
                                [1, 1, 1],
                                [0, 1, 1]], float)  

    # Create a wire-frame triangle passing through vertices [0, 1, 2, 0].
    polydata.lines = np.array([
            [0, 1, 2, 3, 0], # z = 0
            [0, 1, 5, 4, 0], # y = 0
            [0, 3, 7, 4, 0], # x = 0
            [4, 5, 6, 7, 4], # z = 1
            [3, 2, 6, 7, 3], # y = 1
            [1, 2, 6, 5, 1]  # x = 1
            ])

    # Create a solid triangle with vertices [0, 1, 2] as it's corners.
    polydata.polygons = np.array([
            [0, 1, 2, 3, 0], # z = 0
            [0, 1, 5, 4, 0], # y = 0
            [0, 3, 7, 4, 0], # x = 0
            [4, 5, 6, 7, 4], # z = 1
            [3, 2, 6, 7, 3], # y = 1
            [1, 2, 6, 5, 1]  # x = 1
            ])

    # The polydata can be quickly inspected using
    polydata.quick_show()

    # When you are happy with it, it can be turned into a proper plot
    # object like those output from other ``vpl.***()`` commands. It will be
    # automatically added to `vtkplotlib.gcf()` unless told otherwise.
    plot = polydata.to_plot()
    vpl.show()