import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/phr/vscode_project/ros2_launch_testing_ws/install/my_testing'
