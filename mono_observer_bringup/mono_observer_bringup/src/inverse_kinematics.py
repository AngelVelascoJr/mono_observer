#!/usr/bin/env python3

from std_msgs.msg import Int16
from mono_observer_driver_interface.msg import ServoCtrl

class PosToIK():
    def __init__(self):
        pass

    # inverse kinematicks for a 3dof (1 rot in z and 2 rotations in x)
    def GetIK(pos:ServoCtrl) -> ServoCtrl:  # must be a ServoCtrl and return a ServoCtrl
        _i = 0
        
        for element in pos.angles:
            _i = _i + 1

        _i = 0
        newServoControl = ServoCtrl()
        for element in pos.angles:
            newelement = -int(element)
            newServoControl.angles.append(newelement)

        return newServoControl