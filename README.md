# ComputerVision

David Szczecina
30/09/2022

This library is designed to run on a Raspberry Pi with a webcam connected to it. 
Using TensorFlow Lite, Open CV, a trained model and SQL, we have a library which can automatically detect what objects and animals are currently in the view of the camera, save the image, and store the image metadata in a SQL server (date, time, image number, file location, object detected, accuracy)


Next steps:

Connect DSLR camera to rPi so that high quality photos can be captured when animals in focus.
mount camera on camera slider, and program to keep the detected object in the center of frame

Add sensor data the the SQL server so that I can also have ambient conditions when certain animals are detected

