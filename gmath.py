import math
from display import *
from shading import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 12
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 24

#gouraud shading functions
def gouraud_shading(polygons, view, ambient, light, areflect, dreflect, sreflect): # not sure what other parameters are needed??
    # calculate normal n for each vertex of the polygon where n = avg of normals of the polygons which include the vertex_normal
    vertex_normals = avgVertexNormals(polygons)
    vertex_intensity = {}
    # calculate vertex intensity
    for vertex in vertex_normals:
        i = get_lighting(vertex_normals[vertex], view, ambient, light, areflect, dreflect, sreflect)
        vertex_intensity[vertex] = i
    return vertex_intensity

# phong shading functions
def phong_shading():
    print "running phong now"
    return [255,0,0]

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(light[LOCATION])
    normalize(view)

    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    i = [0, 0, 0]
    i[RED] = int(a[RED] + d[RED] + s[RED])
    i[GREEN] = int(a[GREEN] + d[GREEN] + s[GREEN])
    i[BLUE] = int(a[BLUE] + d[BLUE] + s[BLUE])
    limit_color(i)

    return i


def calculate_ambient(alight, areflect):
    a = [0, 0, 0]
    a[RED] = alight[RED] * areflect[RED]
    a[GREEN] = alight[GREEN] * areflect[GREEN]
    a[BLUE] = alight[BLUE] * areflect[BLUE]
    return a

def calculate_diffuse(light, dreflect, normal):
    d = [0, 0, 0]

    dot = dot_product( light[LOCATION], normal)

    dot = dot if dot > 0 else 0
    d[RED] = light[COLOR][RED] * dreflect[RED] * dot
    d[GREEN] = light[COLOR][GREEN] * dreflect[GREEN] * dot
    d[BLUE] = light[COLOR][BLUE] * dreflect[BLUE] * dot
    return d

def calculate_specular(light, sreflect, view, normal):
    s = [0, 0, 0]
    n = [0, 0, 0]

    result = 2 * dot_product(light[LOCATION], normal)
    n[0] = (normal[0] * result) - light[LOCATION][0]
    n[1] = (normal[1] * result) - light[LOCATION][1]
    n[2] = (normal[2] * result) - light[LOCATION][2]

    result = dot_product(n, view)
    result = result if result > 0 else 0
    result = pow( result, SPECULAR_EXP )

    s[RED] = light[COLOR][RED] * sreflect[RED] * result
    s[GREEN] = light[COLOR][GREEN] * sreflect[GREEN] * result
    s[BLUE] = light[COLOR][BLUE] * sreflect[BLUE] * result
    return s

def limit_color(color):
    color[RED] = 255 if color[RED] > 255 else color[RED]
    color[GREEN] = 255 if color[GREEN] > 255 else color[GREEN]
    color[BLUE] = 255 if color[BLUE] > 255 else color[BLUE]


#vector functions
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
