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
    im=scp.grab()
    r, g, b=im.getpixel((x, y))
    hval=rgb2hex(r, g, b)
    pyperclip.copy(hval)
    
#mouse listeners
def on_click(x, y, button, pressed):
    if pressed:
        thr1=Thread(target=do_work, args=(x, y))
        if not thr1.is_alive():
            thr1.start()
        
    else:
        pass
def on_scroll(x, y, dx, dy):
    pass
def on_move(x, y):
    pass



   

    
#keyboard listeners
current=set()


def key_onpress(key):
  
    if key==keyboard.Key.ctrl_l:
        global startedflag
        startedflag=True
        
    if key==keyboard.Key.f1:
            global run
            run=False
               
def key_onrelease(key):
    
    if key==keyboard.Key.ctrl_l:
        global startedflag
        startedflag=False
     
    








if __name__=='__main__':
    
    listener = keyboard.Listener(
    on_press=key_onpress,
    on_release=key_onrelease)
    if listener.is_alive():
        listener.stop()
    listener.start()
   
    listener1= mouse.Listener(
                    on_move=on_move,
                    on_click=on_click,
                    on_scroll=on_scroll)
    while run:
       if not startedflag:
           
           if listener1.is_alive():
               listener1.stop()
               while listener1.is_alive():
                   pass
               

       else:
           if listener1.is_alive():
               continue
          
           if not listener1.is_alive():
               listener1 = mouse.Listener(
                    on_move=on_move,
                    on_click=on_click,
                    on_scroll=on_scroll)
               listener1.start()
               while not listener1.is_alive():
                   pass
       
    listener.stop()
    
 
