# Hand-gesture-control-computer

Purpose of project:-

In this project Instead of using a keyboard, mouse or joystick, we can use our hand 
gestures to control certain functions of a computer like play/pause a video, move 
forward/rewind a video, scroll up/down in a web page and many more. 

Concept of project:- 

The concept behind the project is very simple. We will place two Ultrasonic (US) 
sensors on top of our monitor and will read the distance between the monitor and 
our hand using Arduino based on this value of distance we will perform certain 
actions. To perform actions on our computer we use Python pyautogui library. 
The commands from Arduino are sent to the computer through serial port (USB). 
This data will be then read by python which is running on the computer and based 
on the read data an action will be performed. 
