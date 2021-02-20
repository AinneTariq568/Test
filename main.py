


import key
import blink
import KeyAlphabet
import numpy as np
import cv2

x_axis = 30
y_axis = 10
w = 60
h = 70
delay =0
while True:

    KeyAlphabet(x_axis, y_axis, w, h)
    if x_axis == 550 and y_axis == 85:
        KeyAlphabet(x_axis, y_axis, w * 2, h)
    if x_axis == 550 and y_axis == 160:
        KeyAlphabet(x_axis+35, y_axis, w+10, h)
    if x_axis == 30 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w*4+40, h)
    if x_axis == 315 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w * 3-5, h)
    if x_axis == 510 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w+10 , h)
    if x_axis == 585 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w+10 , h)
    if x_axis == 660 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w +10, h)


  
        

   
