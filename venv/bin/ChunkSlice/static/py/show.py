def showSTL(file_name):
    import vtkplotlib as vpl
    from stl.mesh import Mesh
    from flask import url_for
    import gridfs
    from ChunkSlice.extensions import mongo

    chunk_collection = mongo.db
    data = chunk_collection.fs.files.find_one({'filename': file_name})
    obj_id = data['_id']
    out_data = gridfs.GridFS(chunk_collection).get(obj_id).read()

    # Read the STL using numpy-stl
    # mesh = Mesh.from_file(url_for('main.stl', file_name = file_name))
    mesh = Mesh.from_file(file_name, fh=gridfs.GridFS(chunk_collection).get(obj_id))
    
    # Plot the mesh
    vpl.mesh_plot(mesh)

    # Show the figure
    vpl.show()

def get_points(file_name, des_h):
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

    # Polydata
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


    test_coor_arr = []

    # Make coor_arr containing the coorindates of every location that contains a block
    for i in range(len(x_coors)):

        # Rounds to the closest 0.5
        x = math.floor(np.mean(x_coors[i])) + 0.5
        y = math.floor(np.mean(y_coors[i])) + 0.5
        z = math.floor(np.mean(z_coors[i])) + 0.5

        coor = [x, y, z]

        # Gets the minimum z-coordinate
        if i == 0:
            z_min = z
        elif z_min > z and i > 0:
            z_min = z

        # Gets the maximum z-coordinate
        if i == 0:
            z_max = z
        elif z_max < z and i > 0:
            z_max = z
        
        # Gets the minimum y-coordinate
        if i == 0:
            y_min = y
        elif y_min > y and i > 0:
            y_min = y

        # Gets the maximum y-coordinate
        if i == 0:
            y_max = y
        elif y_max < y and i > 0:
            y_max = y

        # Gets the minimum x-coordinate
        if i == 0:
            x_min = x
        elif x_min > x and i > 0:
            x_min = x

        # Gets the maximum x-coordinate
        if i == 0:
            x_max = x
        elif x_max < x and i > 0:
            x_max = x

        test_coor_arr.append(coor)

    # Remove duplicates from coordinate array
    # https://stackoverflow.com/questions/21065347/remove-duplicates-in-two-dimensional-array-while-maintaining-sequence
   
    coor_arr = []
    for elem in test_coor_arr:
        if elem not in coor_arr:
            coor_arr.append(elem)

    polydata.points = np.array(coor_arr, float)  

    # Plot
    plot = polydata.to_plot()
    vpl.scatter(polydata.points, color='green', radius = 0.5)
    vpl.show()
    return [int(x_max-x_min + 1), int(y_max-y_min + 1), int(z_max-z_min + 1), int(len(coor_arr))]

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

    # Polydata
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


    test_coor_arr = []

    # Make coor_arr containing the coorindates of every location that contains a block
    for i in range(len(x_coors)):

        # Rounds to the closest 0.5
        x = math.floor(np.mean(x_coors[i])) + 0.5
        y = math.floor(np.mean(y_coors[i])) + 0.5
        z = math.floor(np.mean(z_coors[i])) + 0.5

        coor = [x, y, z]

        # Gets the minimum z-coordinate
        if i == 0:
            z_min = z
        elif z_min > z and i > 0:
            z_min = z

        # Gets the maximum z-coordinate
        if i == 0:
            z_max = z
        elif z_max < z and i > 0:
            z_max = z
        
        # Gets the minimum y-coordinate
        if i == 0:
            y_min = y
        elif y_min > y and i > 0:
            y_min = y

        # Gets the maximum y-coordinate
        if i == 0:
            y_max = y
        elif y_max < y and i > 0:
            y_max = y

        # Gets the minimum x-coordinate
        if i == 0:
            x_min = x
        elif x_min > x and i > 0:
            x_min = x

        # Gets the maximum x-coordinate
        if i == 0:
            x_max = x
        elif x_max < x and i > 0:
            x_max = x

        test_coor_arr.append(coor)

    # Remove duplicates from coordinate array
    # https://stackoverflow.com/questions/21065347/remove-duplicates-in-two-dimensional-array-while-maintaining-sequence
   
    coor_arr = []
    for elem in test_coor_arr:
        if elem not in coor_arr:
            coor_arr.append(elem)

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
        rgb_poly.append([0,12,12])

    polydata.polygon_colors = np.array(rgb_poly, float)
    print(rgb_poly)
    # Plot
    
    plot = polydata.to_plot()

    vpl.show()
    return [int(x_max-x_min + 1), int(y_max-y_min + 1), int(z_max-z_min + 1), int(len(coor_arr))]

def plot_section(file_name, des_h, layer):
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

    test_coor_arr = []

    
    # Make coor_arr containing the coorindates of every location that contains a block
    for i in range(len(x_coors)):

        # Rounds to the closest 0.5
        x = math.floor(np.mean(x_coors[i])) + 0.5
        y = math.floor(np.mean(y_coors[i])) + 0.5
        z = math.floor(np.mean(z_coors[i])) + 0.5

        coor = [x, y, z]

        # Gets the minimum z-coordinate
        if i == 0:
            z_min = z
        elif z_min > z and i > 0:
            z_min = z

        # Gets the maximum z-coordinate
        if i == 0:
            z_max = z
        elif z_max < z and i > 0:
            z_max = z
        
        # Gets the minimum y-coordinate
        if i == 0:
            y_min = y
        elif y_min > y and i > 0:
            y_min = y

        # Gets the maximum y-coordinate
        if i == 0:
            y_max = y
        elif y_max < y and i > 0:
            y_max = y

        # Gets the minimum x-coordinate
        if i == 0:
            x_min = x
        elif x_min > x and i > 0:
            x_min = x

        # Gets the maximum x-coordinate
        if i == 0:
            x_max = x
        elif x_max < x and i > 0:
            x_max = x

        test_coor_arr.append(coor)

    # Remove duplicates from coordinate array
    # https://stackoverflow.com/questions/21065347/remove-duplicates-in-two-dimensional-array-while-maintaining-sequence
    coor_arr = []
    for elem in test_coor_arr:
        if elem not in coor_arr:
            coor_arr.append(elem)

    z_for_layer = z_min + (layer-1) 

    coor_for_layer = []

    # Makes the array for coordinates in the desired layer
    for elem in coor_arr:
        if elem[2] == z_for_layer:
            coor_for_layer.append(elem)  
        
    polydata.points = np.array(coor_for_layer, float)  

    # Make array for grid lines
    grid = []
    lines = []
    
    # Lines in y-direction
    lines.append([[x_min - 0.5, y_min - 0.5, z_for_layer],[x_min - 0.5, y_max + 0.5, z_for_layer]])

    for i in range(int(x_max - x_min)):
        lines.append([[x_min + i + 0.5, y_min - 0.5, z_for_layer],[x_min + i + 0.5, y_max + 0.5, z_for_layer]])

    lines.append([[x_max + 0.5, y_min - 0.5, z_for_layer],[x_max + 0.5, y_max + 0.5, z_for_layer]])

    # Lines in x-direction
    lines.append([[x_min - 0.5, y_min - 0.5, z_for_layer],[x_max + 0.5, y_min - 0.5, z_for_layer]])

    for i in range(int(y_max - y_min)):
        lines.append([[x_min - 0.5, y_min + i + 0.5, z_for_layer],[x_max + 0.5, y_min + i + 0.5, z_for_layer]])

    lines.append([[x_min - 0.5, y_max + 0.5, z_for_layer],[x_max + 0.5, y_max + 0.5, z_for_layer]])

    grid.append([lines])
   

    # Plot
    plot = polydata.to_plot() 
    
    vpl.plot(np.array(grid), line_width=2.0, color="black")

    # Makes a colored square for the center point
    vpl.polygon(np.array([
            [math.floor((x_min + x_max)/2) + 0, math.floor((y_min + y_max)/2) + 0, z_for_layer],
            [math.floor((x_min + x_max)/2) + 1, math.floor((y_min + y_max)/2) + 0, z_for_layer],
            [math.floor((x_min + x_max)/2) + 1, math.floor((y_min + y_max)/2) + 1, z_for_layer],
            [math.floor((x_min + x_max)/2) + 0, math.floor((y_min + y_max)/2) + 1, z_for_layer]
        ], float), color="red"
    )

    # Makes a square for the (0,0) point of plot
    vpl.polygon(np.array([
            [x_min - 0.5, y_min - 0.5, z_for_layer],
            [x_min + 0.5, y_min - 0.5, z_for_layer],
            [x_min + 0.5, y_min + 0.5, z_for_layer],
            [x_min - 0.5, y_min + 0.5, z_for_layer]
        ], float), color="grey"
    )
    # Insert colored point at every location for that layer
    vpl.scatter(polydata.points, color="blue", opacity=None, radius = 0.35)
    vpl.show()

    return [int(x_max-x_min + 1), int(y_max-y_min + 1), int(z_max-z_min + 1), int(len(coor_arr))]