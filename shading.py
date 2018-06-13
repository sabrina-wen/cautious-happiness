def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

def avgVertexNormals(polygons) :
    #dict with polygon index, list of three vertices
    polygon_v = polygon_vertices(polygons)
    #print polygon_v
    #dict with vertex as key, list of polygon indices
    v_polygon = vertices_polygons(polygons, polygon_v)
    #print v_polygon
    #calc normals for each polygon
    all_normals = all_poly_normals(polygons);
    #print all_normals
    #calc avg normals
    avg_normals = calc_avg_normals(polygons, v_polygon, all_normals)
    return avg_normals

def polygon_vertices(polygons) :
    polygon_v = dict();
    #dict with polygon index, list of three vertices
    for i in range(0, len(polygons), 3):
        polygon_v[i] = [polygons[i],
                        polygons[i+1],
                        polygons[i+2]]
    return polygon_v

def all_poly_normals(polygons) :
    polygon_n = dict();
    #dict with polygon index, list of three vertices
    for i in range(0, len(polygons), 3):
        polygon_n[i] = calculate_normal(polygons, i)
    return polygon_n

def vertices_polygons(polygons, polygon_v) :
    #dict with vertices as keys, list of polygon indices as value
    #go through polygons
    vertices = dict()
    for v in polygons:
        #if we don't already have an entry
        #stringify v
        vertex = ' '.join(str(e) for e in v)
        if vertex not in vertices:
            #create a list with all polygons containing vertex
            p_with_v = [];
            #traverse through our dict containing polygons and their vertices
            for poly in polygon_v:
                #if our vertex is in that list of vertices
                if v in polygon_v[poly]:
                    #include the index of the polygon
                    p_with_v.append(poly)
            #add the vertex and its list of polygon indices to the vertices dict
            vertices[vertex] = p_with_v
    return vertices



def calc_avg_normals(polygons, v_polygon, all_normals):
    poly_normals = dict()
    #go through dict and calculate normals for each polygon then avg it
    for vertex in v_polygon:
        #create a list for normals
        normals = [];
        #traverse thru list of polygons indices
        for poly in v_polygon[vertex]:
            #this will return the normal
            normals.append(all_normals[poly])
        #find avg of normals
        #find totals of x y and z values
        normal_avg = [0, 0, 0];
        for normal in normals:
            normal_avg[0] += normal[0]
            normal_avg[1] += normal[1]
            normal_avg[2] += normal[2]
        #divide by number of normals
        normal_avg[0] /= len(normals)
        normal_avg[1] /= len(normals)
        normal_avg[2] /= len(normals)
        #add to list of vertex with avged normals
        poly_normals[vertex] = normal_avg
    return poly_normals


'''
p = [[0, 5, 0], [0, 0, 0], [0, 0, 5],
     [0, 5, 0], [0, 0, 5], [0, 5, 5],
     [0, 5, 5], [0, 0, 5], [5, 0, 5],
     [0, 5, 5], [5, 0, 5], [5, 5, 5],
     [0, 5, 0], [0, 5, 5], [5, 5, 5],
     [0, 5, 0], [5, 5, 5], [5, 5, 0],
     [5, 0, 0], [0, 0, 0], [0, 5 ,0],
     [0, 5, 0], [5, 5, 0], [5, 0, 0],
     [5, 5, 0], [5, 5, 5], [5, 0, 5],
     [5, 0, 5], [5, 0, 0], [5, 5, 0],
     [0, 0, 0], [5, 0, 0], [5, 0, 5],
     [5, 0, 5], [0, 0, 5], [0, 0, 0]]



avgVertexNormals(p)
'''
