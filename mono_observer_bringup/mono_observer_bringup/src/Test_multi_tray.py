#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time

class TrajectoryTest(Node):

    def __init__(self):
        super().__init__('trajectory_test')
        topic_name = "/mono_observer_trajectory_controller/joint_trajectory"
        self.trajectory_publisher = self.create_publisher(JointTrajectory, topic_name, 10)
        self.joints = ['base_1_joint', '1_2_joint', '2_3_joint']
        self.goal_positions_list = [
                            [0.0, 0.0, 0.0],
                            [-0.5236, -0.5236, -0.5236],   # -30°
                            [-1.0472, -1.0472, -1.0472],   # -60°
                            [-1.5708, -1.5708, -1.5708],   # -90° 
                            [-2.0944, -2.0944, -2.0944],   # -120°
                            [-2.6179, -2.6179, -2.6179],   # -150°
                            [-3.1416, -3.1416, -3.1416],   # -180°
                        ]
        self.current_goal_index = 0
        self.trajectory_active = False
        self.timer = self.create_timer(3, self.timer_callback)
        self.get_logger().info('Controller is running and publishing to topic: {}'.format(topic_name))

    def timer_callback(self):
        if not self.trajectory_active and self.current_goal_index < len(self.goal_positions_list):
            self.publish_trajectory(self.goal_positions_list[self.current_goal_index])
            self.current_goal_index += 1
            self.trajectory_active = True
        if self.current_goal_index >= len(self.goal_positions_list):
            self.current_goal_index = 0            

    def publish_trajectory(self, goal_positions):
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = goal_positions
        point.time_from_start = Duration(sec=2)
        trajectory_msg.points.append(point)
        self.trajectory_publisher.publish(trajectory_msg)
        self.get_logger().info('Published trajectory: {}'.format(goal_positions))
        self.create_timer(3, self.trajectory_complete_callback)  # Wait for the trajectory to complete

    def trajectory_complete_callback(self):
        self.get_logger().info('Completed trajectory {}'.format(self.current_goal_index))
        time.sleep(2)
        self.trajectory_active = False

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TrajectoryTest()
    rclpy.spin(trajectory_publisher_node)
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()