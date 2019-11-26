import bpy
import os
import math
from blender.renderer.segmentation_colormap import EGO_VEHICLE_COLOR
from blender.renderer.utils import duplicate_add_segmentation


def draw(gazebo_sim_path, scene_rgb, scene_seg):
    model_file = 'hull.dae'
    model_path = os.path.join(gazebo_sim_path, model_file)
    bpy.ops.wm.collada_import(filepath=model_path)

    ego_vehicle_name = 'ego_vehicle'
    bpy.context.active_object.name = ego_vehicle_name
    ego_vehicle = bpy.data.objects[ego_vehicle_name]
    ego_vehicle.rotation_euler = (0, 0, math.pi)
    scene_rgb.objects.link(ego_vehicle)

    duplicate_add_segmentation('seg-' + ego_vehicle_name, EGO_VEHICLE_COLOR, scene_seg)
    return ego_vehicle_name