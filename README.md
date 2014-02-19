ProBuilder
==========

Builder GUI plug-in for Craft

This project is a plug-in program for the PC game 'Craft'. For more
information about the game itself, please refer to:
[Craft-Website](http://www.michaelfogleman.com/craft/)

    The builder script used by the application is from this project:
[Craft-Project](http:github.com/fogleman/Craft/)

###Code Details

This program is mainly written in Kivy/kv language although
Python crunches the numbers.

![](https://raw.github.com/MrSilent/ProBuilder/master/screenshot_2.png)

###Requirements

    -Python v2.7.2
    -Kivy v1.7.2

###Application

![](https://raw.github.com/MrSilent/ProBuilder/master/screenshot_1.png)

Features
========

* -Bitmap tab for easy bitmapping your ASCII art.
* -iBuilder is an increment/interval builder used for building multiple objects in iterations i.e. spiraled stairs.
* -Eleven build functions via builder.py script.
* -Eight individual tabs for multi-execution.
* -Tab titles correspond to build function for ease of location.
* -Input coordinates directly into text widgets or use the buttons/slider/scrollwheel for coarse/fine tuning.
* -Adjustable ranges.(A more sand-boxed approach to building)
* -Change target server/port on the go.
* -Check box to specify whether object should be filled or hollow.
* -Spinner buttons for simple function/block selection
* -Works on Android using Qpython.(Current version may be too difficult to use, simpler Droid version is in the works)
* -Runs on most all major operating systems and their distros.

Instructions
============

To launch the window make sure you have Kivy 1.7.2 installed.

##Unix:

Open a terminal and cd to the source directory. Type 'kivy main.py'.
Done

##Windows:

Right click the main.py file and choose 'open with' option. Browse to
where you unpacked the kivy folder and select the kivy.bat file.
Done

##Then:

1) First study the builder and main scripts carefully to get an
    understanding of what each input corresponds to.(Many functions do
    not require every available input, i.e. 'Sphere' only needs
    Centers, 'X', 'Y', 'Z', and 'Radius'.) Starting and center inputs
    are marked 'Ctr/ X, Y, and Z'. End point inputs are marked 'End/
    X, Y, and Z'.

2) Study the map and select a good spot with enough space to handle
the size of your object.

3) Select your build function/block type and if needed, refer the
builder script for inputs to use.

4) Set all text inputs to equal your target coordinates.

5) Objects are set to 'Hollow' by default, to change this, simply
        check the box above the 'Build It!' button so the label reads
        'Filled'.

6) Triple-quadruple check your settings, hit the 'Build It!' button,
sit back and watch it build.

Tip) You can always set the ranges for 'X' and 'Y' for your needs. For
    example: Say you have a cube from 30 to -30 X, 12 to 45 Y, and 30
    to -30 Z. To prevent damage to the walls of your structure, set
    the X and Z ranges to 29, -29 in order to prevent building outside
    the walls. To use this on a server that supports auth., you must
    place the auth.db file in the kivy install directory.

        Happy building!
            Kris Wolf

###iBuilder

![](https://raw.github.com/MrSilent/ProBuilder/master/ibuilder.png)
