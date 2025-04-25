#!/usr/bin/env python3

import math
from std_msgs.msg import Int16
from mono_observer_driver_interface.msg import ServoCtrl

class PosToIK():
    def __init__(self):
        pass

    def ToAngleInt(rad:float) -> int:
        return int((rad*180)/math.pi)

    def clamp(num:float,maxVal:float,minVal:float) -> float:
        return max(minVal,min(maxVal,num))
    
    # inverse kinematicks for a 3dof (1 rot in z and 2 rotations in x)
    def GetIK(pos:ServoCtrl) -> ServoCtrl:  # must be a ServoCtrl and return a ServoCtrl
        _i = 0
        
        _h_0_1_z = 50
        _h_0_1_x = 0
        _h_1_2 = 87.5
        _h_2_p = 100
        


        for element in pos.angles:
            _i = _i + 1

        _i = 0
        newServoControl = ServoCtrl()

        try:
            #para el angulo 0_Theta_1
            angle1 = math.atan2(pos.angles[1],pos.angles[0])
            newServoControl.angles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle1),90,-90))

            #para el angulo 2_Theta_3
            angle3 = math.acos((pow(pos.angles[0],2)+pow((pos.angles[2]-_h_0_1_z),2)-pow(_h_1_2,2)-pow(_h_2_p,2))/(2*_h_1_2*_h_2_p))
            
            #para el angulo 1_Theta_2
            alpha = 180-angle3
            _h_1_p = math.sqrt(pow(_h_1_2,2)+pow(_h_2_p,2)-2*_h_1_2*_h_2_p*math.cos(alpha))
            angle2 = (math.atan2((pos.angles[2]-_h_0_1_z),(pos.angles[0]-_h_0_1_x))) - (math.acos((-pow(_h_2_p,2)+pow(_h_1_2,2)+pow(_h_1_p,2))/(2*_h_1_2*_h_1_p)))

            newServoControl.angles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle2),90,-90))
            newServoControl.angles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle3),90,-90))
            return newServoControl
        except Exception as e:
            print(f"Error al realizar el calculo de {pos.angles[0]},{pos.angles[1]},{pos.angles[2]}: {e}")
            newServoControl.angles.append(int(0))
            newServoControl.angles.append(int(0))
            newServoControl.angles.append(int(0))
            return newServoControl
