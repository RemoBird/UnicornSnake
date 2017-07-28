#!/usr/bin/python

import time

import random

import unicornhat as unicorn

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event2')

positionen=[[3,4],[3,5],[3,6]]
enemy=[4,4]

lauf=[1,0]

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.3)

while True:
    head=[positionen[0][0]+lauf[0],positionen[0][1]+lauf[1]]
    if head[0]>7:
        head[0]=0
    if head[0]<0:
        head[0]=7
    if head[1]>7:
        head[1]=0
    if head[1]<0:
        head[1]=7
    print (head)
    positionen.insert(0,head)
    unicorn.clear()
    for i, val in enumerate(positionen):
        unicorn.set_pixel(val[0],val[1],0,255,0)

    unicorn.set_pixel(enemy[0],enemy[1],255,0,0)
    if (head[0]==enemy[0]) & (head[1]==enemy[1]):
        unicorn.set_pixel(head[0],head[1],0,0,255)
    else: positionen.pop()
        
    unicorn.show()
    time.sleep(1)
