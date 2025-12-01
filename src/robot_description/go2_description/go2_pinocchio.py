# go2_pinocchio.py
# author: Jaey Kim
# date: 12/01/2025


import pinocchio as pin


urdf_filename = "src/robot_description/go2_description/go2/go2.urdf"

joint_model = pin.JointModelComposite(2)
joint_model.addJoint(pin.JointModelTranslation())
joint_model.addJoint(pin.JointModelSphericalZYX())

model = pin.buildModelFromUrdf(urdf_filename, joint_model)
robot = pin.RobotWrapper(model)
data = model.createData()