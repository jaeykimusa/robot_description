# go2_mujoco.py
# author: Jaey Kim
# date: 01/19/2026


import mujoco
import os


# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path relative to this file
xml_filename = os.path.join(current_dir, "go2", "go2.xml")

model = mujoco.MjModel.from_xml_path(xml_filename)
data = mujoco.MjData(model)