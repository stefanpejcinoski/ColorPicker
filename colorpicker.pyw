# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pynput import keyboard, mouse
import pyscreenshot as scp
import pyperclip
from colormap import rgb2hex
from threading import Thread
startedflag=False;
run=True;

#workerthread
def do_work(x, y):
 
    
    global startedflag
    if not startedflag:
        return
  
    im=scp.grab()
    r, g, b=im.getpixel((x, y))
    hval=rgb2hex(r, g, b)
    pyperclip.copy(hval)
    
    
#screencap and processing action
def execute():
    global startedflag
    startedflag=True
   
    

#keyboard listeners
current=set()


def key_onpress(key):
  
    if key==keyboard.Key.ctrl_l:
            execute()
    if key==keyboard.Key.f1:
            global run
            run=False
            
def key_onrelease(key):
        global startedflag
        startedflag=False
        return






#mouse listener
def on_click(x, y, button, pressed):
    if pressed:
        thr1=Thread(target=do_work, args=(x, y))
        thr1.start()
        return
    else:
        return
def on_scroll(x, y, dx, dy):
    pass
def on_move(x, y):
    pass
if __name__=='__main__':
    listener1 = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
    if listener1.is_alive():
        listener1.stop()
    listener1.start()

    listener = keyboard.Listener(
    on_press=key_onpress,
    on_release=key_onrelease)
    if listener.is_alive():
        listener.stop()
    listener.start()


    while run:
        pass
    listener.stop()
    listener1.stop()
