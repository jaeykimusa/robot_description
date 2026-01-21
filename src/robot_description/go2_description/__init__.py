import os
from importlib import resources

def get_scene_path():
    with resources.path("robot_description.go2_description", "scene.xml") as p:
        return str(p)