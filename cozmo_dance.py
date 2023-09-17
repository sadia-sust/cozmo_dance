#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

''' Cozmo's dance
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps



def cozmo_program(robot: cozmo.robot.Robot):

    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.drive_straight(distance_mm(80), speed_mmps(30)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    robot.drive_straight(distance_mm(-80), speed_mmps(30)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    for _ in range(2):
        robot.drive_straight(distance_mm(20), speed_mmps(50)).wait_for_completed()
        for _ in range(2):
            robot.move_lift(20) 
            time.sleep(1) 
            robot.move_lift(-10)
            time.sleep(1)
        robot.move_head(-5)
        robot.set_head_angle(degrees(-25.0)).wait_for_completed()  
        robot.move_head(0.05)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        
    for _ in range(2):
        robot.move_lift(20) 
        time.sleep(1) 
        robot.move_lift(-10)
        time.sleep(1)
    robot.move_head(-5)

    robot.set_head_angle(degrees(-25.0)).wait_for_completed()  
    robot.move_head(0.05)


    robot.turn_in_place(degrees(-90)).wait_for_completed()
    # time.sleep(2.5)
    robot.set_head_angle(degrees(-25.0)).wait_for_completed()  
    robot.move_head(25.0)

    for _ in range(2):
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(-360)).wait_for_completed()

    # robot.turn_in_place(degrees(-110)).wait_for_completed()
    robot.move_lift(1) 
    time.sleep(1) 
    robot.move_lift(-100)
    # time.sleep(1)
    robot.move_head(-5)

    robot.set_head_angle(degrees(-25.0)).wait_for_completed()  
    robot.move_head(0.05)

    for _ in range(4):
        robot.drive_straight(distance_mm(20), speed_mmps(50)).wait_for_completed()
        robot.set_head_angle(degrees(-25.0)).wait_for_completed()  
        robot.move_head(25.0)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_head(-5)
    
    
    robot.move_head(-5)
    
    robot.move_lift(-5)

    robot.drive_wheels(25, 50)

    time.sleep(3)

    robot.move_head(5)
    robot.move_lift(5)
    robot.drive_wheels(50, -50)
    #time.sleep(3)
    robot.move_lift(-5)

    robot.move_head(5)
    robot.move_lift(5)
    robot.drive_wheels(-50, 50)
    time.sleep(3)
    robot.move_lift(-5)
   
    


cozmo.run_program(cozmo_program)
