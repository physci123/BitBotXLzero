"""Line follower for the BitBot XL.

Upload this as main.py (alongside bitbotXL.py). Press A to start, B to stop.
"""
from microbit import display, button_a, button_b, sleep, Image
import bitbotXL as bot

SPEED = 20       # forward speed
TURN_SPEED = 15  # speed when correcting

display.show(Image.ARROW_N)
while not button_a.was_pressed():
    sleep(50)

while not button_b.was_pressed():
    left = bot.get_left_line()
    right = bot.get_right_line()

    if left and right:
        bot.stop()
    elif left:
        bot.turn_left(TURN_SPEED)
    elif right:
        bot.turn_right(TURN_SPEED)
    else:
        # Lost the line: keep turning the way we last saw it go
        bot.move_forward(SPEED)

    sleep(10)

bot.stop()
display.show(Image.NO)
