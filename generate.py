import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

#dimensions for size
ih = 1
il = 1
iw = 1

#dimensions for position of first tower
ix = 0
iy = 0
iz = 0.5

#distance between towers
t_distance = 2

for r in range(5):
    for c in range(5):
        x = ix + c * t_distance
        y = iy + r * t_distance
        z = iz

        height = ih
        width = iw
        length = iw

        for i in range(10):
            
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[height, length, width])
            length *= .9
            width *= .9
            height *= .9

pyrosim.End()
