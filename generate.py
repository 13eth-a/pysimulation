import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# Dimensions for size
initial_length = 1.0
initial_width = 1.0
initial_height = 1.0

# Initial position of the first tower
x_start = 0
y_start = 0
z_start = 0.5

# Gap between towers
tower_gap = 2.0

# Number of rows and columns
num_rows = 5
num_columns = 5

# Create towers
for r in range(num_rows):
    for c in range(num_columns):
        x = x_start + c * tower_gap
        y = y_start + r * tower_gap
        z = z_start

        length = initial_length
        width = initial_width
        height = initial_height

        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[height, length, width])
            z += height  # Move the block up by its height
            length *= 0.9  # Decrease dimensions by 10%
            width *= 0.9
            height *= 0.9

pyrosim.End()
