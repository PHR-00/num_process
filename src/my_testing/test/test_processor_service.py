# test/test_processor_service.py
import unittest
import time
import rclpy
import pytest
from rclpy.node import Node
from my_interfaces.srv import ProcessNum # 导入服务接口
from launch import LaunchDescription
from launch_ros.actions import Node as LaunchNode 
from launch_testing.actions import ReadyToTest

@pytest.mark.launch_test
def generate_test_description():
    processor_service_node = LaunchNode(
        package='my_algorithms',
        executable='number_processor',
        name='number_processor_service_node'
    )
    return LaunchDescription([processor_service_node, ReadyToTest()])


class TestProcessorService(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.test_node = rclpy.create_node('service_client_test_node')

    def tearDown(self):
        self.test_node.destroy_node()

    def test_service(self, proc_info):

        client = self.test_node.create_client(ProcessNum, 'process_num')
        
        self.assertTrue(client.wait_for_service(timeout_sec=5.0), '服务未在5秒内上线！')
        
        test_cases = [
            (10, 30),
            (-5, -15),
            (0, 0),
            (1, 3),
            (100, 300)
        ]

        for test_input, expected_output in test_cases:

            request = ProcessNum.Request()
            request.num = test_input
            
            # 调用服务
            self.test_node.get_logger().info(f"正在发送请求: {test_input}...")
            future = client.call_async(request)
            
            # 使用 spin_until_future_complete 来等待服务响应，这会阻塞，直到 Future 完成（或超时）
            rclpy.spin_until_future_complete(self.test_node, future, timeout_sec=5.0)

            # 确认已成功完成
            self.assertTrue(future.done(), f"服务调用超时 (输入: {test_input})")
            
            response = future.result()
            self.assertIsNotNone(response, f"服务调用失败，未收到响应 (输入: {test_input})")
            
            self.assertEqual(
                response.processed_num, 
                expected_output,
                f"输入 {test_input} 时，响应结果不正确！"
            )
            self.test_node.get_logger().info(f"测试用例通过: 输入={test_input}, 响应={response.processed_num}")
            
        # 清理客户端
        self.test_node.destroy_client(client)