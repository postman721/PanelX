# PanelX
Python+QT5 panel

A Pyqt5 panel that shows opened windows. 
Written with less than 50 lines of code for Linux.

Notice. This panel is meant to be transparent. Install xcompmgr, compiz etc.

![panel](https://user-images.githubusercontent.com/29865797/98471180-3b43ca00-21f3-11eb-9876-466fbba1a5e4.jpg)


License: PanelX v.0.1 Copyright (c) 2020 JJ Posti <techtimejourney.net> 
This program comes with ABSOLUTELY NO WARRANTY 
For details see: http://www.gnu.org/copyleft/gpl.html.  
This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991")


Dependencies(packages may be different depending on distribution):

    sudo apt-get install -y xcompmgr python3-pyqt5  python3-wnck python3-gi gir1.2-wnck-3.0


To get transparency running do something like this on your startup scripts:

    xcompmgr &

To run the actual panel on the background: 

    python panelx.py &
