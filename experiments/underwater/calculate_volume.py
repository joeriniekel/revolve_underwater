from collada import *

def signedVolumeOfTriangle(triangle):
    p1, p2, p3 = triangle
    v321 = p3[0]*p2[1]*p1[2]
    v231 = p2[0]*p3[1]*p1[2]
    v312 = p3[0]*p1[1]*p2[2]
    v132 = p1[0]*p3[1]*p2[2]
    v213 = p2[0]*p1[1]*p3[2]
    v123 = p1[0]*p2[1]*p3[2]
    return float(1/6)*(-v321 + v231 + v312 - v132 - v213 + v123)


def volumeOfMesh(path):
    volume = 0.0

    mesh = Collada(path)
    triset = mesh.geometries[0].primitives[0]
    for triangle in triset.vertex[triset.vertex_index]:
        volume += signedVolumeOfTriangle(triangle)
    return volume


print(volumeOfMesh('models/rg_robot/meshes/TouchSensor.dae'))
