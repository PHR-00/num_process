# my_algorithms/my_algorithms/number_processor_node.py
import rclpy
from rclpy.node import Node
from my_interfaces.msg import Num
from my_interfaces.srv import ProcessNum 

class NumberProcessorNode(Node):

    def __init__(self):
        super().__init__('number_processor_service_node')
 
        self.srv = self.create_service(
            ProcessNum, 
            'process_num', 
            self.process_num_callback
        )
        self.get_logger().info('数字处理服务节点已启动，等待请求...')

    def process_num_callback(self, request, response):

        input_num = request.num
        self.get_logger().info(f'收到服务请求，输入数字: {input_num}')

        if input_num == 0:
            response.processed_num = 1
            return response
        
        response.processed_num = input_num * 3
        
        self.get_logger().info(f'正在返回处理结果: {response.processed_num}')
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = NumberProcessorNode()
    rclpy.spin(node) 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()









# class NumberProcessorNode(Node):
#     """
#     一个节点，订阅'/number'话题，将数字乘以2，并发布到'/processed_number'。
#     """
#     def __init__(self):
#         super().__init__('number_processor_node')
#         self.subscription_ = self.create_subscription(
#             Num,
#             'number',
#             self.listener_callback,
#             10)
#         self.publisher_ = self.create_publisher(Num, 'processed_number', 10)
#         self.get_logger().info('数字处理节点已启动，等待接收数字...')

#     def listener_callback(self, msg):
#         self.get_logger().info(f'收到: {msg.num}')
        
#         processed_msg = Num()
#         processed_msg.num = msg.num * 2 # 核心逻辑：将数字乘以2
        
#         self.publisher_.publish(processed_msg)
#         self.get_logger().info(f'发布处理后结果: {processed_msg.num}')

# def main(args=None):
#     rclpy.init(args=args)
#     node = NumberProcessorNode()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()