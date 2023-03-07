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
