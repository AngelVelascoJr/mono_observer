#!/usr/bin/env python3

import rclpy
import inverse_kinematics
from inverse_kinematics import GetIK
from rclpy.node import Node
from mono_observer_driver_interface.msg import ServoCtrl

class TestPosition(Node):

    def __init__(self):
        super().__init__('test_position')
        topic_name= "/robot_message"
        self.TerminalInput = ""        
        self.trajectory_publisher = self.create_publisher(ServoCtrl, topic_name,10)
        #self.timer = self.create_timer(1, self.timer_callback)
        self.get_logger().info("Node working, waiting for imput...")

    def GetTerminalInput(self,Str:str):
        self.ConvertedTrayectoryInput = str.split(Str,",")

    def CreateIK(self):
        self.IK = GetIK(self.ConvertedTrayectoryInput)
    
    def PublishAngleToTopic(self):
        self.trajectory_publisher.publish(self.IK)
        

        

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TrajectoryTest()
    while True:
        trajectory_publisher_node.GetTerminalInput(input("Write the position to reach( format '##,##,##,...')"))
        trajectory_publisher_node.CreateIK()
        trajectory_publisher_node.PublishAngleToTopic()

    rclpy.spin(trajectory_publisher_node)
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()