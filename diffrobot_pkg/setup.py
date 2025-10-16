import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'diffrobot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nectar A. Gonzalez Negron',
    maintainer_email='nectargonzalez@outlook.com',
    description='Differential drive robot simulation ROS2 ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'kinematics_node = diffrobot_pkg.kinematics_node:main',
            'encoder_node = diffrobot_pkg.encoder_node:main',
            'reset_client = diffrobot_pkg.reset_client:main',
        ],
    },
)
