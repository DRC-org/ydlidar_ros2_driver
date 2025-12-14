#!/usr/bin/python3

import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import LifecycleNode

from launch import LaunchDescription


def generate_launch_description():
    share_dir = get_package_share_directory("ydlidar_ros2_driver")
    parameter_file = LaunchConfiguration("params_file")
    node_name = "ydlidar_ros2_driver_node"

    params_declare = DeclareLaunchArgument(
        "params_file",
        default_value=os.path.join(share_dir, "params", "ydlidar.yaml"),
        description="FPath to the ROS2 parameters file to use.",
    )

    driver_node = LifecycleNode(
        package="ydlidar_ros2_driver",
        executable=node_name,
        name=node_name,
        namespace="/",
        output="screen",
        emulate_tty=True,
        parameters=[parameter_file],
    )

    return LaunchDescription(
        [
            params_declare,
            driver_node,
        ]
    )
