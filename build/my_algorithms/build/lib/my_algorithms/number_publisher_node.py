# my_algorithms/my_algorithms/number_publisher_node.py
import rclpy
from rclpy.node import Node
from my_interfaces.msg import Num  

class NumberPublisherNode(Node):

    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Num, 'number', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) # 频率1hz，1秒触发一次
        self.current_number_ = 1
        self.get_logger().info('数字发布节点已启动，将从1开始发布...')

    def timer_callback(self):
        msg = Num()
        msg.num = self.current_number_
        self.publisher_.publish(msg)
        self.get_logger().info(f'发布: {msg.num}')
        self.current_number_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()