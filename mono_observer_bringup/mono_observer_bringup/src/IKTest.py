#!/usr/bin/env python3

from mono_observer_driver_interface.msg import ServoCtrl
from inverse_kinematics import PosToIK

class IKTestNode():
    def __init__(self):
        srvctrl = ServoCtrl()
        for x in range(150):
            for y in range(150):
                for z in range(150):
                    srvctrl = ServoCtrl()
                    srvctrl.angles.append(x)
                    srvctrl.angles.append(y)
                    srvctrl.angles.append(z)
                    self.IK = PosToIK.GetIK(pos=srvctrl)
                    
                    print(f"({x},{y},{z}= {self.IK.angles[0]} , {self.IK.angles[1]} , {self.IK.angles[2]}")


def main(args=None):
    robot_node = IKTestNode()

if __name__ == "__main__":
    main()