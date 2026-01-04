# Guardian Edge
## Instant Hazard Alert for Two-Wheelers via NICLA Vision

### Problem Statement
Two-wheeler riders that are riding through a solitary place may meet an accident which may not get them immediate medical and family help when it is needed.

### Goal of the project
Detect whether a two-wheeler rider is riding safely or unsafely in real time using edge device inference for low latency, low power resource constraints.

### Dataset Description
Dataset is as per the NICLA vision IMU: $a_x$, $a_y$, $a_z$, $g_x$, $g_y$, $g_z$

### Model Pipeline and Workflow
Model used: Decision Tree

#### Workflow
* Train the model using sliding window data for all the three activities - riding, jerking, and falling.
* Do EDA to find out important features.
* Extract the important features in the NICLA itself.
* Do inference on the NICLA itself to compute if it was shaking or not.
* Use the logic given in slides to predict the activity based on the inference result of both the devices.

### Deployment Details and Instructions to run the code
* Setup NICLA vision to connect to PC.
* Run the given main.py on NICLA visions A and B.
* Run the PhoneRecieverScript on the PC.

Note: Ultimately, we want the PC code to run on the Phone too. That is, both the IMU sensor B (in the experiment, it is NICLA vision B) and the final activity detection shall take place on phone itself.

### Team Member Name
1. Manas Kumar Mishra
2. Animesh Kumar
3. Adarsh Dubey
4. Varshan P A
5. Abhijeet Kumar

