from setuptools import find_packages, setup

package_name = 'my_algorithms'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phr',
    maintainer_email='phr@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'number_publisher = my_algorithms.number_publisher_node:main',
            'number_processor = my_algorithms.number_processor_node:main',


        ],
    },
)
