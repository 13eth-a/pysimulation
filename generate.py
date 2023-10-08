import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

#dimensions for size
length = 1
width = 1
height = 1

#dimensions for position
x = 0
y = 0
z = 0.5

pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[height, length, width])

pyrosim.End()