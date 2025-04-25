#!/usr/bin/env python3

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
        super().__init__('test_position')
        topic_name= "/mono_observer_trajectory_controller/joint_trajectory"
        self.TerminalInput = ""
        self.PositionList = []
        self.trajectory_publisher = self.create_publisher(JointTrajectory, topic_name,10) #Esta mal, necesita otro tipo de mensajes para funcionar xd
        self.joints = ['base_1_joint', '1_2_joint', '2_3_joint']
        self.get_logger().info(f"Node publishing in {topic_name}, waiting for input...")

    def GetTerminalInput(self,Str:str):
        self.ConvertedTrayectoryInput = str.split(Str,",")
        self.UnityMessage = ServoCtrl()
        self.TrayectoryMessage = JointTrajectory()
        self.TrayectoryMessage.joint_names = self.joints
        for value in self.ConvertedTrayectoryInput:
            self.PositionList.append(int(value,base=10))
            self.UnityMessage.angles.append(int(value,base=10))
        self.get_logger().info("Data formated")

    def CreateIK(self):
        self.IK = PosToIK.GetIK(pos=self.UnityMessage.angles)
    
    def PublishAngleToTopic(self):
        point = JointTrajectoryPoint()
        angleFloatArray = []
        for value in self.IK:
            angleFloatArray.append(radians(value))
            self.get_logger().info(f"{value}: {radians(value)}")
        point.positions = angleFloatArray
        point.time_from_start = Duration(sec=2)
        self.TrayectoryMessage.points.append(point)
        self.get_logger().info("publishing data to topic")
        self.trajectory_publisher.publish(self.TrayectoryMessage)
        #self.trajectory_publisher.publish(self.IK)
        

        

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TestPosition()
    while True:
        trajectory_publisher_node.GetTerminalInput(input("Write the position to reach [mm]( format '##,##,##,...')"))
        trajectory_publisher_node.CreateIK()
        trajectory_publisher_node.PublishAngleToTopic()

    rclpy.spin(trajectory_publisher_node)
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()