#!/usr/bin/env python3

import math
from std_msgs.msg import Int16

class PosToIK():
    def __init__(self):
        pass

    def ToAngleInt(rad:float) -> int:
        return int((rad*180)/math.pi)

    def clamp(num:float,maxVal:float,minVal:float) -> float:
        return num#max(minVal,min(maxVal,num))
    
    # inverse kinematicks for a 3dof (1 rot in z and 2 rotations in y)
    def GetIK(pos:list[int]) -> list[int]:
        _i = 0
        
        _h_0_1_z = 50
        _h_0_1_x = 0
        _h_1_2 = 87.5
        _h_2_p = 100
        
        ServoAngles = []
        
        xp = pos[0]
        yp = pos[1]
        zp = pos[2]

        try:
            #para el angulo 0_Theta_1
            angle1 = math.atan2(yp,xp)
            ServoAngles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle1),0,-180))

            #para el angulo 2_Theta_3
            angle3 = math.acos((pow(xp,2)+pow((zp-_h_0_1_z),2)-pow(_h_1_2,2)-pow(_h_2_p,2))/(2*_h_1_2*_h_2_p))
            
            #para el angulo 1_Theta_2
            #alpha = math.pi-angle3
            dx = xp - _h_0_1_x
            dz = zp - _h_0_1_z
            _h_1_p = math.sqrt(dx**2 + dz**2)
            #_h_1_p = math.sqrt(pow(_h_1_2,2)+pow(_h_2_p,2)-2*_h_1_2*_h_2_p*math.cos(alpha))
            angle2 = (math.atan2((xp-_h_0_1_x),(zp-_h_0_1_z))) - (math.acos((-pow(_h_2_p,2)+pow(_h_1_2,2)+pow(_h_1_p,2))/(2*_h_1_2*_h_1_p)))

            ServoAngles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle2),90,-90))
            ServoAngles.append(PosToIK.clamp(PosToIK.ToAngleInt(angle3),90,-90))
            return ServoAngles
        except Exception as e:
            print(f"Error al realizar el calculo de {xp},{yp},{zp}: {e}")
            ServoAngles.append(int(0))
            ServoAngles.append(int(0))
            ServoAngles.append(int(0))
            return ServoAngles
