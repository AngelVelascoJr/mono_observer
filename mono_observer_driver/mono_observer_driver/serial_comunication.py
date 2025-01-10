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
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=3)
        self.get_logger().info(f"conected to {self.ser.port}, serial conection status: {self.ser.is_open}")
        self.get_logger().info("started listening")

    # recieve data from main pc as topic message
    def __recieve_positions_clbk(self, msg:ServoCtrl):  
        self.get_logger().info(f"{len(msg.angles)} data received")
        i = 0
        message = ''
        for data in msg.angles:
            self.get_logger().info(f"{i}.- {data}")
            i += 1
            message += f'{data}'
            if i < len(msg.angles):
                message += ','
        message += 'E'
        # send data throughth port to driver
        self.ser.write((f"{message}").encode())
        self.get_logger().warning(f"message sended: {message}")
        # self.get_logger().warning(f"Send successfull, reciebed: {self.ser.read_until(b'E')}")    #Recieve feedback from Dricer with same format

def main(args=None):
    rclpy.init(args=args)
    robot_node = RobotNode('servo_node')
    rclpy.spin(robot_node)
    robot_node.ser.close()
    rclpy.shutdown()

if __name__ == "__main__":
    main()