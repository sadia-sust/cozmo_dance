#Project Description
We have developed this for an assignment of our Sensor and IOT course. Our approach was to set up Cozmo to dance (make various movements and do actions) for the music. 

The Cozmo robot, which is an accessible and low-cost platform, has also been used to personalize tutoring, foster collaboration and inclusion, and facilitate in-home human interactions.
We used these interactive behaviors to choreograph Cozmo to dance to a song.

#Sensor Setup
1. Download the Cozmo app on a supported device (We have used an iPhone).
2. On a Unix workstation, download Python (already installed) and the Cozmo Python API using the pip command.
3. Create a Python script to control Cozmo.

#cozmo_dance
A Python script uses the Cozmo API to control the robot and make it dance to a song. 
In the beginning, the script will call the set_all_backpack_lights() function to set up cozmo backpack light blue. Then we used drive_straight(), play_anim(), turn_in_place(), move_lift(), move_head(), drive_wheels(), etc. functions to make cozmo drive straight for a given distance, play goggle sound, make a turn for a given angle, move the hand to lift, move wheels in given direction respectively. 


