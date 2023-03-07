"""
import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep
# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section
def light_to_servo_pos(light):
    light_max = 320
    return 180 - ((light/light_max) * 180)
# Loop Section
while True:
    servo.angle = light_to_servo_pos(cp.light)
    print(servo.angle)
    sleep(0.5)

"""
""" LAB 3 pt 1
import board
from adafruit_hcsr04 import HCSR04
from time import sleep
# Setup Section
sonar = HCSR04(trigger_pin=board.TX, echo_pin=board.A6)
# Function Section
# Loop Section
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    sleep(0.5)
"""

""" LAB 3 pt 2.1
import board
import pwmio
from adafruit_circuitplayground import cp
from adafruit_hcsr04 import HCSR04
import adafruit_motor.servo
from time import sleep
# Setup Section
sonar = HCSR04(trigger_pin=board.TX, echo_pin=board.A6)
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section
def servo_pos(dist):
    dist_min = 5
    dist_max = 50
    dist = min((max((dist, dist_min)), dist_max))
    return (((dist-dist_min)/(dist_max-dist_min)) * 180)
# Loop Section
while True:
    try:
        servo.angle = servo_pos(sonar.distance)
        print((sonar.distance, servo.angle))
    except RuntimeError:
        print("Retrying!")
    sleep(0.5)
"""

"""
# Import Section
import board
from adafruit_circuitplayground import cp
from adafruit_hcsr04 import HCSR04
from time import sleep
# Setup Section
led_brightness = 0.25
t=0
dt = 0.25
sonar = HCSR04(trigger_pin=board.TX, echo_pin=board.A6)
cp.pixels.fill((255,0,0))
cp.pixels.brightness = 0
# Function Section
def pixel_flip():
    if cp.pixels.brightness > 0:
        cp.pixels.brightness = 0
    else:
        cp.pixels.brightness = led_brightness
# Loop Section
while True:
    try:
        d = sonar.distance
        # Closer than 15 cm is Dangerously Close
        if d <=5:
            pixel_flip()
            if t >= 1.0:
                cp.play_tone(440, 0.25)
                t=0
        # Closer than 15 cm is Very Close
        elif d <= 15:
            pixel_flip()
        # Closer than 30 cm is Close
        elif d <= 30:
            if t >= 1.0:
                pixel_flip()
                t=0
        # Farther than 25 cm is Safe
        else:
            cp.pixels.brightness = 0
        print((d,))
        t+=dt
    except RuntimeError:
        print("Retrying!")
    sleep(dt)

"""
# PROJECT CODE
import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep

# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section

# User Specified Max Time (minutes)

MAX = 1

# Timer Variables
MAX_TIME = MAX * 60
timer = 0
interval = 0
count = 0
cp.pixels.brightness = 0.1
x = 0
# Loop Section

while True:
    # OVERFLOW DETECTION
    if (cp.button_a and timer == MAX_TIME):
        x = 0
        timer = 0
        interval = 0
        cp.pixels.fill((0,0,0))
    # SET LOCK DURATION
    if (cp.button_a and timer < MAX_TIME):
        cp.play_tone(460+x, 0.15)
        x += 10
        timer += MAX_TIME/10
        interval += 1
        cp.pixels[interval-1] = (0, 255, 0)
        sleep(0.25)
        print("WILL LOCK FOR", timer, "SECONDS")
    # SET LOCK
    elif cp.button_b:
        print("LOCKED FOR", timer, "SECONDS")
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

        # UNLOCK
        servo.angle = 0
        timer = 0
        cp.pixels.fill((0,255,0))
        sleep(0.5)
        cp.pixels.fill((0,0,0))
        print("UNLOCKED")
        for i in range(3):
            cp.play_tone(800, 0.25)
    else:
        continue
