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
The thermal camera used is a LWIR Lepton 2.5 thermal camera form Flir. 
![bilde](https://user-images.githubusercontent.com/93716653/141095818-e9caf765-f32e-46e3-97bd-b7295250fb4e.png)

The first thing to do is to download Flir Lepton Application at https://lepton.flir.com/software-sdk/. 
When the installing is done, open the app and plug the camera in the USB port of the computer. Now the camera should connect and the image should show on the screen. Then the camera is ready to take pictures just by clicking on "take snapshot".
![thermal-image](https://user-images.githubusercontent.com/93716653/141096533-c1c76f43-3cf9-4013-9a62-343739ea1aba.PNG)


## Computer vision
Start by making a folder named "object detection". Create a new folder called "images" inside "object detection". In the folder "images", make two new folders called "train" and "val". Place 20 images in train, 20 in val and 10 in object detection. 

Label the object in the images and annotate the images in VGG Image Annotator (VIA) at https://www.robots.ox.ac.uk/~vgg/software/via/via.html.
Uploade the pictures form the folder "train" and choose the polygon opion and lable the object. When the object is labeled, use attributes to name the object and press toggle annotation editor to use the attribute. Then save the file as "via_region_data.json". Place this file in the folder "train" and do the same procedure for the images in the "val" folder and place the "via_region_data.json" file for them in the same folder.
![object-labeling](https://user-images.githubusercontent.com/93716653/141098079-a2a9b670-6cf0-4755-bec7-ba5a0015cf88.PNG)

To train the images. Install Anaconda Navigator 4.8.3 and make an own environment in here. Install Spyder 3.3.6 in Anaconda, which is the program used to code in Python 3.7 and install Tensorflow 2 and skikit 0.16.2.
<img width="1420" alt="Skjermbilde 2021-11-10 kl  11 42 08" src="https://user-images.githubusercontent.com/93716653/141098796-069adaa2-0aca-4764-84e6-a06110718ad1.png">

Pyton codes with pre-traind coco models "mask\_rcnn\_coco.h5" were provided by the University of Agder, consisting of two files; "bollard.py" and "bollard\_detection.py". These files need to be put in the object detcetion folder. The files cam be seen in this github room. 

Open the terminal in Anaconda and change the path to the object detection folder. Start the training with the command "python bollard.py train --dataset=images\ --weights=coco". This command runs through 10 epoch, with 9 training steps per epoch. In total the training is running 90 times. 
![terminal2](https://user-images.githubusercontent.com/93716653/141100222-d5cddd70-54bb-4f08-a1bc-3180846e4ace.PNG)
![terminal5](https://user-images.githubusercontent.com/93716653/141100233-3a1e1a5d-3700-40d1-934c-93d64521fe5b.PNG)

When the training is done. Go to the folder logs in object detection and take the latest file and place it in the object detection folder. Now place the same file in the "bollard_detection.py" file and place on of the images in the object detection folder in this file. Then press run. The file sould run and the object detection should be done. 
![Skjermbilde-pythonscreen](https://user-images.githubusercontent.com/93716653/141100486-fbda1659-b6b7-4e1b-bb44-bfbeaaf0db32.PNG)


