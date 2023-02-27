import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep
import random
import neopixel
import simpleio
# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section

# Loop Section
timer = 0
while True:
    if (cp.button_a and timer < 10):
        timer += 1
        sleep(0.5)
        cp.pixels.brightness = 0.3
        cp.pixels[0] = (255, 0, 0)
        if(timer == 2):
            cp.pixels[1] = (0,255,0)
        if(timer == 3):
            cp.pixels[2] = (0,0,255)
        if(timer == 4):
            cp.pixels[3] = (0, 255, 255)
        if(timer == 5):
            cp.pixels[4] = (255, 255, 0)
        if(timer == 6):
            cp.pixels[5] = (255, 255, 255)
        if(timer == 7):
            cp.pixels[6] = (255,0,255)
        if(timer == 8):
             cp.pixels[7] = (180,0,255)
        if(timer == 9):
             cp.pixels[8] = (255,255,0)
        if(timer == 10):
             cp.pixels[9] = (0,255,0)
        print(timer)
    elif cp.button_b:
        print("locked")
        servo.angle = 180
        
        sleep(timer)
        import board

        print("donne")
        servo.angle = 0
        timer = 0
        freq = 440
        if(timer == 0):
            simpleio.tone(board.A1, frequency=freq, duration=1.0)
            sleep(2.0)

 # This is an A3
# Loop Section
    
    else:
        continue
