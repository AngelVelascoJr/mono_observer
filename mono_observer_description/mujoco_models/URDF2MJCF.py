#!/usr/bin/env python3

import mujoco
model = mujoco.MjModel.from_xml_path('full_xacro.urdf')
mujoco.mj_saveLastXML('full_xacro.xml', model)
print("imported!")
