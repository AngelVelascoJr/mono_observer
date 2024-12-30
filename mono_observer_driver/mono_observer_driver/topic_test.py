#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mono_observer_driver_interface.msg import ServoCtrl
from random import randint

class TopicTestNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__topic_pub = self.create_publisher(ServoCtrl, '/robot_message', 10)
        self.__timer = self.create_timer(5, self.__send_rand_positions_clbk)

    # recieve data from main pc as topic message
    def __send_rand_positions_clbk(self):  
        self.__values = []
        self.__random_pos_count = randint(1, 3)
        for count in range(self.__random_pos_count):
            self.__values.append(randint(0, 180))
        self.get_logger().info(f"sending {self.__random_pos_count} data")
        for i in range(self.__values.count):
            self.get_logger().log(f"{i}.- {self.__values[i]}")
        # send data throughth port to driver

def main(args=None):
    rclpy.init(args=args)
    robot_node = TopicTestNode('topic_test_node')
    rclpy.spin(robot_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()