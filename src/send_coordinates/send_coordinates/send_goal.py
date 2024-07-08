import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalSender(Node):
    def __init__(self):
        super().__init__('goal_sender')
        self.publisher_ = self.create_publisher(PoseStamped, 'goal_pose', 10)

    def send_goal(self, x, y, z, qx, qy, qz, qw):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()

        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_msg.pose.position.z = z

        goal_msg.pose.orientation.x = qx
        goal_msg.pose.orientation.y = qy
        goal_msg.pose.orientation.z = qz
        goal_msg.pose.orientation.w = qw

        self.publisher_.publish(goal_msg)
        self.get_logger().info(f'Sent goal: [{x}, {y}, {z}, {qx}, {qy}, {qz}, {qw}]')


def main(args=None):
    rclpy.init(args=args)
    node = GoalSender()

    try:
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        z = float(input("Enter z coordinate: "))
        qx = float(input("Enter quaternion x: "))
        qy = float(input("Enter quaternion y: "))
        qz = float(input("Enter quaternion z: "))
        qw = float(input("Enter quaternion w: "))

        node.send_goal(x, y, z, qx, qy, qz, qw)
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
