"""Keep the BitBot XL 10cm away from the object in front of it.

Upload this as main.py (alongside bitbotXL.py). Press A to start, B to stop.
Hold your hand or a book in front of the robot and move it back and forth.
"""
from microbit import display, button_a, button_b, sleep, Image
import bitbotXL as bot

TARGET_CM = 10    # distance to hold
TOLERANCE_CM = 1  # close enough: don't move
GAIN = 3          # speed per cm of error: bigger reacts harder
MIN_SPEED = 20    # slower than this and the wheels may not turn
MAX_SPEED = 50

display.show(Image.ARROW_N)
while not button_a.was_pressed():
    sleep(50)

while not button_b.was_pressed():
    distance = bot.get_distance()
    error = distance - TARGET_CM  # positive: too far, negative: too close

    if distance == -1 or abs(error) <= TOLERANCE_CM:
        # Nothing detected, or already at the right distance
        bot.stop()
    else:
        speed = max(MIN_SPEED, min(MAX_SPEED, abs(error) * GAIN))
        if error > 0:
            bot.move_forward(speed)
        else:
            bot.move_backwards(speed)

    sleep(50)

bot.stop()
display.show(Image.NO)
