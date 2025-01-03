#!/usr/bin/env python3

import rclpy
import serial
import serial.tools.list_ports as port_list

from rclpy.node import Node
from mono_observer_driver_interface.msg import ServoCtrl

class RobotNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__topic_sub = self.create_subscription(ServoCtrl, '/robot_message', self.__recieve_positions_clbk, 10)
        self.get_logger().info("Trying to connect to port")
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            timeout=3)
        self.get_logger().info(f"serial conection: {self.ser.is_open}")
        self.get_logger().info("started listening")

    # recieve data from main pc as topic message
    def __recieve_positions_clbk(self, msg:ServoCtrl):  
        self.get_logger().info(f"{len(msg.angles)} data received")
        self.__i = 0
        for data in msg.angles:
            self.get_logger().info(f"{self.__i}.- {data}")
            self.__i += 1
        # send data throughth port to driver



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