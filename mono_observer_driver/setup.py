from setuptools import find_packages, setup

package_name = 'mono_observer_driver'

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
    maintainer='Angel Velasco',
    maintainer_email='davidvp.advp@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "serial_coms = mono_observer_driver.serial_comunication:main",
            "topic_test = mono_observer_driver.topic_test:main",
            "serial_test = mono_observer_driver.serial_pc_to_driver_test:main"
        ],
    },
)
