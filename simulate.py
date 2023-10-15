import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(10000)
exit(print(backLegSensorValues))

#manage display time
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)

 #touch sensor for back leg
backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#print back leg sensor value
print(backLegTouch)
    



p.disconnect()