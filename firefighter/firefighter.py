from subsystems import Drivetrain
from time import sleep

# H-drive drivetrain
drivetrain = Drivetrain()

while (True):
    drivetrain.arcade_drive(1.0, 0.0, 0.0)
