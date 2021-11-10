# Imagine with Drone

## Assemble the Drone
To Assemble the Holybro X500 drone, the manual given in the kit was followed.
All parts are shown in the picture below.
![bilde](https://user-images.githubusercontent.com/93716653/141079907-9faa4ec3-3991-48e3-ba79-532ee90136d1.png)
(picture borrowed from https://docs.px4.io/v1.12/en/frames_multicopter/holybro_x500_pixhawk4.html)

Step 1:
Start with attaching the motor to the motor base and the carbon fiber tube-arm, using the Socket cap screw (M3*5,16pcs).
<img width="749" alt="Skjermbilde 2021-11-10 kl  10 30 40" src="https://user-images.githubusercontent.com/93716653/141088024-d278c79b-1648-4f17-92a2-b322b104a6cd.png">


Step 2:
Now the chassis is going to be assambled. Take the slide bars, take the two pylons and attach them to the slide bars. Put the 8 hanger rubber ring gasket inside the 8 hangers, and then place the hangers on the slide bars. Attach the battery mounting board on the pylons and the PAN/TILT platform board on the hangers on the slide bar with the Cross countersunk head srews (M2.5*5,12pcs).
<img width="733" alt="Skjermbilde 2021-11-10 kl  10 30 54" src="https://user-images.githubusercontent.com/93716653/141088085-3a78be92-0ac0-4e3a-951f-97caf52bebb9.png">


Step 3: 
Now it's time to mount the carbon fiber bottom plate to the four hangers in the middel of the slide bars with the Socket cap screw (M2.5*6,8pcs). Also, attach the Nylon stud (M3*6+6,4pcs) in the Nylon screw (M3*6,4pcs) in four of the hols in the inner circle on the bottom plate.  
<img width="732" alt="Skjermbilde 2021-11-10 kl  10 31 04" src="https://user-images.githubusercontent.com/93716653/141088116-5c212f0d-f970-46d0-b3c1-c052123825d3.png">


Step 4:
Attach the Power module to the center of the bottom plate. Then take the fiber carbon top plate and use the Pan head screw (M3*30,16pcs) to attach the arms with the motors by using the 16 nylon straps and the Locknut (M3,16pcs) to lock them in place. 
<img width="758" alt="Skjermbilde 2021-11-10 kl  10 31 12" src="https://user-images.githubusercontent.com/93716653/141088145-fc6e5381-7d16-4b7c-8f9d-ae52bc982891.png">


Step 5:
Use the Socket cap screw (M3*8,8pcs) to attach the Landing gear-Vertical pole to the bottom plate. Attach the Landing gear-cross bar to the bottom of the vertical pole. Skrew the propellers on, silver mark on counter-clockwise and black on clockwise rotation.
<img width="752" alt="Skjermbilde 2021-11-10 kl  10 31 19" src="https://user-images.githubusercontent.com/93716653/141088185-37104160-221d-4d7f-8556-4d4c57b8e381.png">

The pictures in these steps are borrowed from the Holybro X500 assamble manual to get an easier understandig of how to assamble the drone (http://www.holybro.com/manual/Holybro_X500_FrameKit_AssemblyGuide.pdf).

After these steps are done, the wires to the motors needs to be attached. The red wire goes on the red wire, black on black, and the blur wore from the motors goes on the yellow and black twisted wire which are connected to the power module. Pixhawk 4 is going to be mounted on the top plate and so are the GPS tower and the telemerty radio. The GPS is connected to the Pixhawk 4 in "GPS module" and the telemetry radio is connected to "TELEM1". The cable from the power module is connected to the "I/O-PWM-out" in Pixhawk 4 and the "PWR1" at the power modulde is connected to "Power1" on the Pixhawk 4.
<img width="541" alt="Skjermbilde 2021-11-10 kl  10 48 27" src="https://user-images.githubusercontent.com/93716653/141090286-f05a6a30-4b2d-4cf4-8f43-8ed96c9547dd.png">

Now the assemble of the drone is done. 

## Connect to QGroundControl and remote controller
Next step is to connect the Pixhawk 4 to the QGroundControl which is used to calibrate all the sensors and controll the drone. 

Go to http://qgroundcontrol.com/downloads/ and download the application. 

When QGroundControl is installed, first use the cable to the Pixhawk 4 and connect it to a computer with a USB port. Then the vehicle should connect itself.
<img width="1433" alt="Skjermbilde 2021-11-10 kl  11 07 21" src="https://user-images.githubusercontent.com/93716653/141093394-7733754c-d51c-4a57-b3cb-dc9f933c718a.png">

In QGroundControl, press the icon in the left upper corner and go to Vehicle Setup.
<img width="1437" alt="Skjermbilde 2021-11-10 kl  11 09 18" src="https://user-images.githubusercontent.com/93716653/141093727-04222b52-9b84-44ea-b2c8-642b157c51c9.png">

Here choose Firmware and uplode the PX4 Flight Stack vX.X.X Stable Release.
<img width="733" alt="Skjermbilde 2021-11-10 kl  11 12 23" src="https://user-images.githubusercontent.com/93716653/141094229-47b66e65-05b7-4999-8e90-5c1de1d21894.png">

Now go to Airframe and choose "Holybro S500" and click apply and restart.
<img width="1433" alt="Skjermbilde 2021-11-10 kl  11 13 38" src="https://user-images.githubusercontent.com/93716653/141094376-b5d0ae5b-0346-4971-9195-7da6e8e11c25.png">

Next step is to callibrate the sensors. Go to sensors and start with calibration the compass, gyroscope, accelerometer, level horizon and the orientation. Follow the instructions on the screen. 
<img width="1431" alt="Skjermbilde 2021-11-10 kl  11 15 38" src="https://user-images.githubusercontent.com/93716653/141094849-d038af54-97f3-4492-a3c7-c25edfcd1384.png">

Then it's time for the Radio setup. Follow the instructions on the screen and point the sticks in every direction shown.
<img width="1436" alt="Skjermbilde 2021-11-10 kl  11 18 36" src="https://user-images.githubusercontent.com/93716653/141095154-9d81eb59-5b1c-4b42-8879-d2985c957c3f.png">

Now, fix the flight mode setup like in the picture below. 
<img width="1427" alt="Skjermbilde 2021-11-10 kl  11 18 59" src="https://user-images.githubusercontent.com/93716653/141095307-a02eddd7-2ecc-4271-80e2-38020bd443c9.png">

Go to power setup and put in the necessary information for the battery and callibrate the battery. Make sure the propellers are removed. 
<img width="1436" alt="Skjermbilde 2021-11-10 kl  11 19 57" src="https://user-images.githubusercontent.com/93716653/141095492-cfb3f724-db96-4a18-b95e-500f70b862d5.png">

Now it's time to fly the drone.


## Thermal camera setup




## Computer vision
