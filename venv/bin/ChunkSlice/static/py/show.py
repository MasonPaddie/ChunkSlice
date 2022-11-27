def showSTL(file_name):
    import vtkplotlib as vpl
    from stl.mesh import Mesh
    from flask import url_for

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file((file_name))
    
    # Plot the mesh
    vpl.mesh_plot(mesh)

    # Show the figure
    vpl.show()

def get_points(file_name):
    import vtkplotlib as vpl
    import numpy as np
    import math
    import collections
    from stl.mesh import Mesh
    from operator import itemgetter
    from flask import url_for

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file(file_name)

    # Get the coorindates of each point in the mesh
    x_coors = mesh.x
    y_coors = mesh.y
    z_coors = mesh.z

    coor_arr = []
    
    #  # Make coor_arr containing the coorindates of every location that contains a block
    for i in range(len(x_coors)):

        inc = False

        # Rounds to the closest 0.5
        x = math.floor(np.mean(x_coors[i])/4) + 0.5
        y = math.floor(np.mean(y_coors[i])/4) + 0.5
        z = math.floor(np.mean(z_coors[i])/4) + 0.5

        coor = [x, y, z]

        # If the coordinate was recently added, do not add it again
        if i > 0:
            for elem in coor_arr[-10:]:
                if collections.Counter(elem) == collections.Counter(coor):
                    inc = True
            if inc == False:
                coor_arr.append(coor)
        elif i == 0:
            coor_arr.append(coor)

    # print(sorted(coor_arr, key=itemgetter(0,1,2)))
    polydata = vpl.PolyData()

    polydata.points = np.array(coor_arr, float)  

    # Plot
    plot = polydata.to_plot()
    vpl.scatter(polydata.points, color='green', opacity=None, radius = 0.2)
    vpl.show()

def get_cubes(file_name, des_h):
    import vtkplotlib as vpl
    import numpy as np
    import math
    import collections
    from stl.mesh import Mesh
    from operator import itemgetter
    from flask import url_for

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file(file_name)

    polydata = vpl.PolyData()

    # The overall height of the final object is set to the desired height set by the user
    h = des_h
    
    test_z_height = []
    for elem in mesh.z:
        test_z_height.append(np.mean(elem))

    # Get the current height of the object
    cur_h = (math.floor(max(test_z_height)) + 0.5) - (math.floor(min(test_z_height)) + 0.5)

    # Get the scale factor
    scale_fac = (h-1)/cur_h

    # Get the coorindates of each point in the mesh
    x_coors = scale_fac*mesh.x
    y_coors = scale_fac*mesh.y
    z_coors = scale_fac*mesh.z

    coor_arr = []


    # Make coor_arr containing the coorindates of every location that contains a block
    for i in range(len(x_coors)):

        inc = False

        # Rounds to the closest 0.5
        x = math.floor(np.mean(x_coors[i])) + 0.5
        y = math.floor(np.mean(y_coors[i])) + 0.5
        z = math.floor(np.mean(z_coors[i])) + 0.5

        coor = [x, y, z]
        if i > 0:

            # If the coordinate was recently added, do not add it again
            for elem in coor_arr[-10:]:
                if collections.Counter(elem) == collections.Counter(coor):
                    inc = True
            if inc == False:
                coor_arr.append(coor)
        elif i == 0:
            coor_arr.append(coor)

    cube_arr = []

    # Make array for cube vertices
    for elem in coor_arr:
        cube_arr.append([elem[0]-0.5, elem[1]-0.5, elem[2]-0.5])
        cube_arr.append([elem[0]+0.5, elem[1]-0.5, elem[2]-0.5])         
        cube_arr.append([elem[0]+0.5, elem[1]+0.5, elem[2]-0.5])
        cube_arr.append([elem[0]-0.5, elem[1]+0.5, elem[2]-0.5])
        cube_arr.append([elem[0]-0.5, elem[1]-0.5, elem[2]+0.5])
        cube_arr.append([elem[0]+0.5, elem[1]-0.5, elem[2]+0.5])
        cube_arr.append([elem[0]+0.5, elem[1]+0.5, elem[2]+0.5])
        cube_arr.append([elem[0]-0.5, elem[1]+0.5, elem[2]+0.5])        

    polydata.points = np.array(cube_arr, float)  

    line_arr = []
    solid_arr = []

    # Make arrays for lines and polygon faces
    for i in range(len(coor_arr)):
        line_arr.append([8*i + 0, 8*i + 1, 8*i + 2, 8*i + 3, 8*i + 0])
        line_arr.append([8*i + 0, 8*i + 1, 8*i + 5, 8*i + 4, 8*i + 0])
        line_arr.append([8*i + 0, 8*i + 3, 8*i + 7, 8*i + 4, 8*i + 0])
        line_arr.append([8*i + 4, 8*i + 5, 8*i + 6, 8*i + 7, 8*i + 4])
        line_arr.append([8*i + 3, 8*i + 2, 8*i + 6, 8*i + 7, 8*i + 3])
        line_arr.append([8*i + 1, 8*i + 2, 8*i + 6, 8*i + 5, 8*i + 1])
        

        solid_arr.append([8*i + 0, 8*i + 1, 8*i + 2, 8*i + 3, 8*i + 0])
        solid_arr.append([8*i + 0, 8*i + 1, 8*i + 5, 8*i + 4, 8*i + 0])
        solid_arr.append([8*i + 0, 8*i + 3, 8*i + 7, 8*i + 4, 8*i + 0])
        solid_arr.append([8*i + 4, 8*i + 5, 8*i + 6, 8*i + 7, 8*i + 4])
        solid_arr.append([8*i + 3, 8*i + 2, 8*i + 6, 8*i + 7, 8*i + 3])
        solid_arr.append([8*i + 1, 8*i + 2, 8*i + 6, 8*i + 5, 8*i + 1])

        # vpl.plot(np.array([cube_arr[8*i + 0],cube_arr[8*i + 1],cube_arr[8*i + 2],cube_arr[8*i + 3]]), join_ends=True, color="black", line_width=2.0)
        # vpl.plot(np.array([cube_arr[8*i + 0],cube_arr[8*i + 1],cube_arr[8*i + 5],cube_arr[8*i + 4]]), join_ends=True, color="black", line_width=2.0)
        # vpl.plot(np.array([cube_arr[8*i + 0],cube_arr[8*i + 3],cube_arr[8*i + 7],cube_arr[8*i + 4]]), join_ends=True, color="black", line_width=2.0)
        # vpl.plot(np.array([cube_arr[8*i + 4],cube_arr[8*i + 5],cube_arr[8*i + 6],cube_arr[8*i + 7]]), join_ends=True, color="black", line_width=2.0)
        # vpl.plot(np.array([cube_arr[8*i + 3],cube_arr[8*i + 2],cube_arr[8*i + 6],cube_arr[8*i + 7]]), join_ends=True, color="black", line_width=2.0)
        # vpl.plot(np.array([cube_arr[8*i + 1],cube_arr[8*i + 2],cube_arr[8*i + 6],cube_arr[8*i + 5]]), join_ends=True, color="black", line_width=2.0)
        
   
    # Create a wire-frame.
    polydata.lines = np.array(line_arr, float)

    
    # # Create a solid.
    polydata.polygons = np.array(solid_arr, float)

    rgb_poly = []

    for i in range(len(solid_arr)):
        rgb_poly.append([61,47,255])

    polydata.polygon_colors = np.array(rgb_poly, float)

    # Plot
    
    plot = polydata.to_plot()
    vpl.show()