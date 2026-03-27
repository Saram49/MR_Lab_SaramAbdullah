import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn


class VelocityPublisher(Node):

    def __init__(self):
        super().__init__('velocity_publisher')

        self.turtle1_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.turtle2_publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.turtle3_publisher = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)

        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.spawn_turtle('turtle2', 4.3, 7.0, 0.0)
        self.spawn_turtle('turtle3', 4.5, 2.0, 0.0)

        self.timer_period = 0.1  # seconds
        self.square_state = 'forward'
        self.state_elapsed = 0.0
        self.forward_duration = 2.0
        self.turn_duration = 1.57

        self.turtle3_state = 'forward'
        self.turtle3_elapsed = 0.0
        self.turtle3_forward_duration = 1.0
        self.turtle3_turn_duration = 1.3

        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def spawn_turtle(self, name, x_pos, y_pos, theta):
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')

        request = Spawn.Request()
        request.x = x_pos
        request.y = y_pos
        request.theta = theta
        request.name = name

        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'{name} spawned successfully')
        else:
            self.get_logger().warn(f'Could not spawn {name} (it may already exist)')

    def timer_callback(self):
        
        turtle1_msg = Twist()
        if self.square_state == 'forward':
            turtle1_msg.linear.x = 2.0
            turtle1_msg.angular.z = 0.0
            if self.state_elapsed >= self.forward_duration:
                self.square_state = 'turn'
                self.state_elapsed = 0.0
        else:
            turtle1_msg.linear.x = 0.0
            turtle1_msg.angular.z = 1.57
            if self.state_elapsed >= self.turn_duration:
                self.square_state = 'forward'
                self.state_elapsed = 0.0

        self.turtle1_publisher.publish(turtle1_msg)

        # turtle2: circular motion with constant linear and angular velocity.
        turtle2_msg = Twist()
        turtle2_msg.linear.x = 1.5
        turtle2_msg.angular.z = 1.0
        self.turtle2_publisher.publish(turtle2_msg)

        # turtle3: simple triangle pattern.
        turtle3_msg = Twist()
        if self.turtle3_state == 'forward':
            turtle3_msg.linear.x = 1.6
            turtle3_msg.angular.z = 0.0
            if self.turtle3_elapsed >= self.turtle3_forward_duration:
                self.turtle3_state = 'turn'
                self.turtle3_elapsed = 0.0
        else:
            turtle3_msg.linear.x = 0.0
            turtle3_msg.angular.z = 1.6
            if self.turtle3_elapsed >= self.turtle3_turn_duration:
                self.turtle3_state = 'forward'
                self.turtle3_elapsed = 0.0

        self.turtle3_publisher.publish(turtle3_msg)

        self.state_elapsed += self.timer_period
        self.turtle3_elapsed += self.timer_period


def main(args=None):
    
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    rclpy.spin(velocity_publisher)
    # Destroy the node explicitly
    velocity_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

