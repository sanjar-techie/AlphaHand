import modi 
import time 
import random
from commands import *

inp = random.randint(1, 3)

## Tests for tuning the modular electronics
if __name__ == "__main__":
    bundle = modi.MODI(1)
    motor1 = bundle.motors[0]
    motor2 = bundle.motors[1]
    display = bundle.displays[0]

    if inp=="scissor":
        display.text = "scissor"
        scissor(motor1, motor2)
        time.sleep(1)
        display.clear()
    elif inp=="rock":
        display.text = "rock"
        rock(motor1, motor2)
        time.sleep(1)
        display.clear()
    else:
        display.text("paper")
        paper(motor1, motor2)
        time.sleep(1)
        display.clear()

        