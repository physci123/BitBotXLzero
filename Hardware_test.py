"""Hardware test for bitbotXL.py.

Put the robot on the floor with some clear space (or on blocks for the
motor tests). Each test announces itself on the display; press A to run it.
"""
from microbit import display, button_a, sleep, Image
import bitbotXL as bot


def wait_for_a(name):
    display.scroll(name, wait=False, loop=True)
    while not button_a.was_pressed():
        sleep(50)
    display.clear()


def show_values(label, read, seconds=5):
    """Show a live reading for a few seconds so you can wave a hand / torch at it."""
    for _ in range(seconds * 2):
        display.scroll(label + str(read()), delay=120)
        sleep(100)


def test_movement():
    wait_for_a("FWD")
    bot.move_forward(50, 1000)
    wait_for_a("BACK")
    bot.move_backwards(50, 1000)
    wait_for_a("LEFT")
    bot.turn_left(50, 600)
    wait_for_a("RIGHT")
    bot.turn_right(50, 600)


def test_leds():
    wait_for_a("LED")
    for colour in (bot.RED, bot.GREEN, bot.BLUE):
        bot.leds_on(colour)
        sleep(500)
    bot.leds_off()
    for i in range(bot.NUM_LEDS):  # chase along both arms
        bot.led_on(i, bot.PURPLE)
        sleep(100)
        bot.led_off(i)


def test_buzzer():
    wait_for_a("BUZZ")
    bot.buzzer(200)
    sleep(200)
    bot.buzzer(200)


def test_sensors():
    wait_for_a("DIST")
    show_values("D", bot.get_distance)
    wait_for_a("LLIGHT")
    show_values("L", bot.get_left_light)
    wait_for_a("RLIGHT")
    show_values("R", bot.get_right_light)
    wait_for_a("LLINE")
    show_values("L", bot.get_left_line)
    wait_for_a("RLINE")
    show_values("R", bot.get_right_line)


test_movement()
test_leds()
test_buzzer()
test_sensors()
bot.stop()
display.show(Image.YES)
