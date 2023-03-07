# PROJECT CODE

import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep
import simpleio
import time
from adafruit_hcsr04 import HCSR04


# Setup Section

pwm = pwmio.PWMOut(board.A3, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
cp.detect_taps = 2
cp.pixels.brightness = 0.1

# User Specified Max Time (minutes)

MAX = 0.5

# Timer Variables
MAX_TIME = MAX * 60
timer = 0
interval = 0
count = 0

# Loop Section
while True:
    while True:
        # OVERFLOW DETECTION
        if (cp.button_a and timer == MAX_TIME):
            timer = 0
            interval = 0
            cp.pixels.fill((0,0,0))
        # SET LOCK DURATION
        if (cp.button_a and timer < MAX_TIME):
            timer += MAX_TIME/10
            interval += 1
            #here different pixels and make a sound
            
            if(interval==1):
                 cp.pixels[0] = (255,0,0)
                 cp.play_tone(400, 0.25)
            if(interval==2):
                 cp.pixels[1] = (255,150,0)
                 cp.play_tone(410, 0.25)
            if(interval==3):
                cp.pixels[2]=(255,40,0)
                cp.play_tone(420, 0.25)
            if(interval == 4):
                cp.pixels[3] = (0, 255, 0)
                cp.play_tone(430, 0.25)
            if(interval == 5):
                cp.pixels[4] = (0,255,120)
                cp.play_tone(440, 0.25)
            if(interval == 6):
                cp.pixels[5] = (0,255,255)
                cp.play_tone(450, 0.25)
            if(interval == 7):
                cp.pixels[6] = (180,0,255)
                cp.play_tone(460, 0.25)
            if(interval == 8):
                 cp.pixels[7] = (255,0,20)
                 cp.play_tone(470, 0.25)
            if(interval == 9):
                 cp.pixels[8] = (255,255,255)
                 cp.play_tone(480, 0.25)
            if(interval == 10):
                 cp.pixels[9] = (255,0,0)
                 cp.play_tone(490, 0.25)
            sleep(0.25)
            print("WILL LOCK FOR", timer/60, "MINUTES")
        # SET LOCK
        elif cp.button_b:
            #after lock make a double sound
            cp.play_tone(460, 1)
            print("LOCKED FOR", timer/60, "MINUTES")
            # LOCKING ANIMATION
            for i in range (0, interval):
                cp.pixels[i] = (255, 0, 0)
                sleep(0.1)
            servo.angle = 90

            # TIMER
            while (timer != 0):
                sleep(1)
                count += 1
                # TIME REMAINING ANIMATION
                if (count == MAX_TIME/10):
                    cp.pixels[interval - 1] = (0, 0, 0)
                    interval -= 1
                    count = 0
                timer -= 1
                # PRINT REMANING TIME FOR DEBUGGING
                print(timer, "SECONDS REMAINING")
                #and cp.touch_TX and cp.touch_A5 and cp.touch_A6
                #overrides
            #play the ringtome
            t = time.time() + 5
            while time.time() < t:
                cp.play_tone(470, 0.15)
                cp.play_tone(570, 0.15)
                cp.play_tone(670, 0.15)

            servo.angle = 0
            timer = 0

            cp.pixels[0] = (255,0,0)

            cp.pixels[1] = (0,255,0)

            cp.pixels[2] = (0,255,255)
            cp.pixels[3] = (155, 100, 0)
            cp.pixels[4] = (210, 45, 0)
            cp.pixels[5] = (255, 255, 255)
            cp.pixels[6] = (255,0,255)
            cp.pixels[7] = (180,0,255)
            cp.pixels[8] = (255,255,0)
            cp.pixels[9] = (0,255,0)
            sleep(0.5)

            cp.pixels.fill((0,0,0))
            print("UNLOCKED")
        else:
            continue
