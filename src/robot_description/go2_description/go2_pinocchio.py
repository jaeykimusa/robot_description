# go2_pinocchio.py
# author: Jaey Kim
# date: 12/01/2025


import pinocchio as pin
import os


# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path relative to this file
urdf_filename = os.path.join(current_dir, "go2", "go2_EEs.urdf")

joint_model = pin.JointModelComposite(2)
joint_model.addJoint(pin.JointModelTranslation())
joint_model.addJoint(pin.JointModelSphericalZYX())

model = pin.buildModelFromUrdf(urdf_filename, joint_model)
robot = pin.RobotWrapper(model)
data = model.createData()
