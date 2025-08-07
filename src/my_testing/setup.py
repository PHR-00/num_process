from setuptools import find_packages, setup

package_name = 'my_testing'

setup(
    name=package_name,
    version='0.0.0',
    package = [],
    # packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phr',
    maintainer_email='phr@todo.todo',
    description='Description:Launch tests',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
