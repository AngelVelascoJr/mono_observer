#!/usr/bin/env python3

import rclpy
import inverse_kinematics
from math import radians
from time import sleep
from inverse_kinematics import PosToIK
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from mono_observer_driver_interface.msg import ServoCtrl

class TestPosition(Node):

    def __init__(self):
        super().__init__('test_position')
        topic_name= "/mono_observer_trajectory_controller/joint_trajectory"
        self.trajectory_publisher = self.create_publisher(JointTrajectory, topic_name,10) #Esta mal, necesita otro tipo de mensajes para funcionar xd
        self.joints = ['base_1_joint', '1_2_joint', '2_3_joint']
        self.get_logger().info(f"Node publishing in {topic_name}")

    def PublishAngleToTopic(self):
        self.get_logger().info("publishing data to topic")
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    self.postogo = [(x*20)-80,(y*20)-80,(z*20)-80]
                    self.IK = PosToIK.GetIK(pos=self.postogo)
                    self.TrayectoryMessage = JointTrajectory()
                    self.TrayectoryMessage.joint_names = self.joints
                    point = JointTrajectoryPoint()
                    point.positions.append(radians(self.IK[0]))
                    point.positions.append(radians(self.IK[1]))
                    point.positions.append(radians(self.IK[2]))
                    print(f"({self.postogo[0]},{self.postogo[1]},{self.postogo[2]}): [{self.IK[0]},{self.IK[1]},{self.IK[2]}] = {point.positions[0]} , {point.positions[1]} , {point.positions[2]}")
                    point.time_from_start = Duration(nanosec=500000000)
                    self.TrayectoryMessage.points.append(point)
                    self.trajectory_publisher.publish(self.TrayectoryMessage)
                    sleep(0.5)

        

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TestPosition()
    trajectory_publisher_node.PublishAngleToTopic()
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()