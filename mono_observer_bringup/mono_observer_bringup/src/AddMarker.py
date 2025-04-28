#!/usr/bin/env python3

import rclpy
from random import Random
from rclpy.node import Node
from example_interfaces.msg import Float32MultiArray
from visualization_msgs.msg import Marker

class AddMarkerNode(Node):

    def __init__(self):
        super().__init__('test_angles')
        subscribe_topic_name = "/pos_to_marker"
        self.trayectory_subscriber = self.create_subscription(Float32MultiArray, subscribe_topic_name, self.TrajectoryToMarker, 10)
        publish_topic_name= "/marker_topic"
        self.marker_publisher = self.create_publisher(Marker, publish_topic_name,10)
        self.i = 0
        self.get_logger().info(f"Node publishing in {publish_topic_name}, listening from {subscribe_topic_name}")

    def TrajectoryToMarker(self, data_array:Float32MultiArray):
        print(f"publishing: {data_array}")
        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.id = self.i
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position.x = data_array.data[0]/1000
        marker.pose.position.y = data_array.data[1]/1000
        marker.pose.position.z = data_array.data[2]/1000
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.05
        marker.scale.y = 0.05
        marker.scale.z = 0.05
        marker.color.r = Random().randint(0,100)/100.0
        marker.color.g = Random().randint(0,100)/100.0
        marker.color.b = Random().randint(0,100)/100.0
        marker.color.a = 1.0
        self.marker_publisher.publish(marker)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    Marker_Maker_Node = AddMarkerNode()
    rclpy.spin(Marker_Maker_Node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()