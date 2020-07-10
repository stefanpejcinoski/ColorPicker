# Introduction

Have you ever found an intresting color while browsing the internet or testing out some software and wanted to implement it in your design? 
ColorPicker will let you do that. Run the script and it will remain active in the background , hitting Ctrl and clicking anywhere on the screen
will pick out the color that the mouse cursor is pointing to and save it to your clipboard so you can paste it into your design software.

# Warning

This is a test version, there are no checks for user error, if you run multiple instances of the script it will create multiple event handlers for mouse/keyboard input
and it will result in erratic mouse movement/clicking and problems with keyboard input

# Guide

ColorPicker only works on Windows and Mac because of the way it takes screenshots
If not already installed, install Python and then the necessary packages.

Open up a command prompt and run:
```console
pip install colormap
pip install pyperclip
pip install pyscreenshot
pip install easydev
pip install pynput
``` 

then just run the script. 
To stop the script press F1.