#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from mono_observer_driver_interface.msg import UnityAngle

class TestPosition(Node):

    def __init__(self):
        super().__init__('joint_to_unity')
        trayectory_topic_name= "/mono_observer_trajectory_controller/joint_trajectory"
        unity_topic_name= "/unity/servo_angle"
        self.PositionList = []
        self.trajectory_subscriber = self.create_subscription(JointTrajectory, trayectory_topic_name, self.OnGetTrayectory, 10)
        self.ToUnityPublisher = self.create_publisher(UnityAngle, unity_topic_name, 10)
        self.get_logger().info(f"Node publishing in {unity_topic_name}, waiting for data in topic {trayectory_topic_name}...")

    def OnGetTrayectory(self, info:JointTrajectory):
        new_message = UnityAngle()
        self.get_logger().info("publishing data to unity topic:")
        for angle in info.points[0].positions:
            new_message.rad_angles.append(angle)
            self.get_logger().info(f"{angle}")
        self.ToUnityPublisher.publish(new_message)        

def main(args=None):
    rclpy.init(args=args)
    to_unity_node = TestPosition()
    rclpy.spin(to_unity_node)
    to_unity_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()