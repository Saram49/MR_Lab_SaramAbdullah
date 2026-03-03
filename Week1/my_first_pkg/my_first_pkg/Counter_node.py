import rclpy
from rclpy.node import Node


class SimpleNode(Node):
    def __init__(self):
        super().__init__('Counter_node')

        self.counter = 0

        # Timer: runs every 1 second
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info(
            f'Hello, Ros2 | Count: {self.counter}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()

    # Keeps node running continuously
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
