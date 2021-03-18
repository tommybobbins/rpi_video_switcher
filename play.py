#!/usr/bin/python3
from gpiozero import LED, Button
from time import sleep
from datetime import datetime
from subprocess import Popen
from signal import pause
from os import system

import os
button1 = Button(10)
button2 = Button(9)
vid1="home.mp4"
vid2="ssh.mp4"
os.system('killall omxplayer.bin')

def play_vid1():
    print ("Play looping default video")
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', vid1, '--loop'])

def play_vid2():
    print ("Play standalone video")
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', vid2])
    omxc.wait()
    # Belt and braces, kill this with fire
    os.system('killall omxplayer.bin')
    print ("Finished standalone video")

while True:
    play_vid1()
    button1.wait_for_press() 
    play_vid2()
