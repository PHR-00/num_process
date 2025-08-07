
# import unittest
# import time
# import rclpy
# import launch
# import launch_ros
# import launch_testing
# from rclpy.node import Node
# from my_interfaces.msg import Num
# import pytest
# from launch import LaunchDescription
# from launch_ros.actions import Node as LaunchNode 
# from launch_testing.actions import ReadyToTest


# @pytest.mark.launch_test
# def generate_test_description():
#     publisher_node = LaunchNode(
#         package='my_algorithms',
#         executable='number_publisher',
#         name='number_publisher'
#     )
#     processor_node = LaunchNode(
#         package='my_algorithms',
#         executable='number_processor',
#         name='number_processor'
#     )
#     return LaunchDescription([
#         publisher_node,
#         processor_node,
#         ReadyToTest()
#     ])


# class TestIntegration(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         rclpy.init()

#     @classmethod
#     def tearDownClass(cls):
#         rclpy.shutdown()

#     def setUp(self):
#         self.test_node = rclpy.create_node('test_subscriber_node')
#         self.get_logger().info('测试节点test_subscriber_node已创建')
#         self.received_messages = []

#     def tearDown(self):
#         self.test_node.destroy_node()
#         self.get_logger().info('测试结束，销毁测试节点')

#     def test_publisher_starts_ok(self, proc_output):
#         self.get_logger().info("正在检查 publisher 节点的启动日志...")
#         proc_output.assertWaitFor('数字发布节点已启动，将从1开始发布...',stream='stderr',timeout=1)
#         self.get_logger().info("Publisher 节点启动正常。")

#     def test_processor_starts_ok(self, proc_output):
       
#         self.get_logger().info("正在检查 processor 节点的启动日志...")
#         proc_output.assertWaitFor('数字处理节点已启动，等待接收数字...',stream='stderr',timeout=1)
#         self.get_logger().info("Processor 节点启动正常。")


#     def test_communication_and_logic(self):
#         sub = self.test_node.create_subscription(Num, '/processed_number', lambda msg: self.received_messages.append(msg.num), 10)
        
#         try:
#             end_time = time.time() + 5.0
#             while time.time() < end_time and len(self.received_messages) < 3:
#                 rclpy.spin_once(self.test_node, timeout_sec=0.1)

#             self.get_logger().info(f"检查接收到的消息。 Got: {self.received_messages}")
            
#             self.assertGreater(len(self.received_messages), 0, "未收到消息！")

#             expected_results = [i * 2 for i in range(1, len(self.received_messages) + 1)]
#             self.assertEqual(sorted(self.received_messages), sorted(expected_results))

#         finally:
#             self.test_node.destroy_subscription(sub)


#     def get_logger(self):
#         return self.test_node.get_logger()
    





# #从哪获取数据，如何获取数据