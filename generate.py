import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

#dimensions for size
length = 1
width = 1
height = 1

#dimensions for position of box
x = 0
y = 0
z = 0.5

for i in range(5):
    for i in range (10):
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[height, length, width])
        z += 1   
        length = .9 * length
        width = .9 * width
        height = .9 * height
    x += 1

        





pyrosim.End()