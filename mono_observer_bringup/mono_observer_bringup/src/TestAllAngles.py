#!/usr/bin/env python3

from time import sleep
import rclpy
import inverse_kinematics
from math import radians
from inverse_kinematics import PosToIK
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from mono_observer_driver_interface.msg import ServoCtrl

class TestPosition(Node):

    def __init__(self):
        super().__init__('test_angles')
        topic_name= "/mono_observer_trajectory_controller/joint_trajectory"
        self.trajectory_publisher = self.create_publisher(JointTrajectory, topic_name,10) #Esta mal, necesita otro tipo de mensajes para funcionar xd
        self.joints = ['base_1_joint', '1_2_joint', '2_3_joint']
        self.get_logger().info(f"Node publishing in {topic_name}, waiting for imput...")

    def PublishAngleToTopic(self):
        self.get_logger().info("publishing data to topic")
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    self.TrayectoryMessage = JointTrajectory()
                    self.TrayectoryMessage.joint_names = self.joints
                    point = JointTrajectoryPoint()
                    point.positions.append(radians((x*20)-90))
                    point.positions.append(radians((y*20)-90))
                    point.positions.append(radians((z*20)-90))
                    print(f"({x},{y},{z}= {point.positions[0]} , {point.positions[1]} , {point.positions[2]}")
                    point.time_from_start = Duration(nanosec=500000000)
                    self.TrayectoryMessage.points.append(point)
                    self.trajectory_publisher.publish(self.TrayectoryMessage)
                    sleep(0.5)
        #self.trajectory_publisher.publish(self.IK)
        
        

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TestPosition()
    trajectory_publisher_node.PublishAngleToTopic()
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()