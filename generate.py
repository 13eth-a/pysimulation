import pyrosim.pyrosim as pyrosim

#creates world for robot
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

#creates robot
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

Create_World()
Create_Robot()