import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

#dimensions for size
length = 1
width = 1
height = 1

#dimensions for position
x = 0
y = 0
z = 0.5


for r in range(5):
        for c in range(5):
            for i in range (10):
                pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[height, length, width])
                z += 1   
                length *= .9
                width *= .9
                height *= .9
        x += 1
        y += 1



        
pyrosim.End()