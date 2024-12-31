#!/usr/bin/env python3

import rclpy
import serial
import serial.tools.list_ports as port_list
from rclpy.node import Node

class RobotNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("Trying to connect to port")
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            timeout=3)
        self.get_logger().info(f"serial conection: {self.ser.is_open}")
        self.get_logger().info("started listening")
        

def main(args=None):
    rclpy.init(args=args)
    robot_node = RobotNode('servo_node')
    while True:
        robot_node.get_logger().info(robot_node.ser.readline())        
    #rclpy.spin(robot_node)
    #robot_node.ser.close()
    #rclpy.shutdown()

if __name__ == "__main__":
    main()