# AutoJoin - Join Discord Channels Automatically at a specific time
Automate joining a discord channel using PyAutoGUI library with different features

A script to join a discord channel at a specific time automatically using PyAutoGUI library for Python 3.

Script either takes input for the time at which the channel is supposed to be joined or uses the already specified time.
On the desired time, using PytAutoGUI, the script switches window to discord and then searches the screen for a part of the screen 
that matches the snippet of server logo taken before. Then it pulls the coordinates of that server logo and clicks on it and then uses
a previously specified dictionary to join voice channel of the class based on what day it is(based on a predefined schedule as well). 

-For some reason, PyAutoGUI doesn't work with the light gray text and dark gray background of discord so I had to save the coordinates of 
 voice channels instead of searching them up on the screen. Tried different ways but no luck.
 
Pretty simple script. Decided to make it because I'm usually late to my online classes.

--My first github project
