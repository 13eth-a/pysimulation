import pyrosim.pyrosim as pyrosim

#creates world for robot
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])
    pyrosim.End()

#creates robot
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -1, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, 0, 0])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 1, 0.5], size=[1, 1, 1])
    
    
    
    pyrosim.End()

Create_World()
Create_Robot()