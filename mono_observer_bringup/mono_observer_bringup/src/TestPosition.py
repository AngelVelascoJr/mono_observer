#!/usr/bin/env python3

import rclpy
import inverse_kinematics
from inverse_kinematics import PosToIK
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
        self.FormatedTrayectoryInput = ServoCtrl()
        for value in self.ConvertedTrayectoryInput:
            self.FormatedTrayectoryInput.angles.append(int(value,base=10))
        self.get_logger().info("Data formated correctly")

    def CreateIK(self):
        self.IK = PosToIK.GetIK(pos=self.FormatedTrayectoryInput)
    
    def PublishAngleToTopic(self):
        self.get_logger().info("publishing data to topic")
        for value in self.IK.angles:
            self.get_logger().info(str(value))
        self.trajectory_publisher.publish(self.IK)
        

        

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