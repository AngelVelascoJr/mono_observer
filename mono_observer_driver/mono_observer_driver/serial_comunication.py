#!/usr/bin/env python3

import rclpy
import serial.tools.list_ports as port_list

from rclpy.node import Node
from driver_interface.msg import BuzzerCtrl

class RobotNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__topic_pub = self.create_subscription(BuzzerCtrl, '/mensaje', self.__recieve_positions_clbk, 10)

    def __recieve_positions_clbk(self, msg:BuzzerCtrl):
        self.get_logger().info(f"")

def main(args=None):
    rclpy.init(args=args)
    robot_node = RobotNode('servo_node')
    rclpy.spin(robot_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()