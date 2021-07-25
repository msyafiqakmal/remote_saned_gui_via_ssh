# remote_saned_gui_via_ssh
Simple GUI to run remote scanning using saned via ssh for Linux desktop (it can also be used for Mac/win since its uses pyqt).

## Problem Statement
I uses Canon E460 with saned as scanner program. I connected this scanner to my raspberry pi home server for shared home use during working from home. 
Couldnt find any remote scanning program for my liking.

## intent 
sharing just in case so that others to expand and improve

## Approach
hooked up the printer/scanner to the raspberry pi.
install saned on the remote machine (rpi)  
documentation on sane available via [here](https://linux.die.net/man/1/scanimage)

####  trigger remote scanning via:

```
ssh -p <port number> <ssh username>@<in address> scanimage >'<local machine path e.g. /home/msyafiqakmal/Picutres/Scanning/scanning.png>'
```

the program simply provide gui on the above

![Untitled.png](https://github.com/msyafiqakmal/remote_saned_gui_via_ssh/blob/master/Untitled.png)
![Completed.png](https://github.com/msyafiqakmal/remote_saned_gui_via_ssh/blob/master/Completed.png)

## To run:
Option1 : 
Configure default via yaml at least specify remote server username. the rest shall be picked up from gui. 

trigger via 
```
python3 scanner.py
```
save configuration in gui will save the parameters in yaml file.

Option2: Package it via pyinstaller (not covered here)
