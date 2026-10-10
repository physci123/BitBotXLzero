"""Simple library for the 4tronix BitBot Classic on a micro:bit (MicroPython).

This has exactly the same functions as bitbotXL.py, so a program written
for one robot works on the other by changing only the import line.

Usage:
    import bitbotClassic as bot

    bot.move_forward(50, 1000)   # forward at 50% speed for 1 second
    print(bot.get_distance())    # distance to the nearest object in cm

Speeds are 0-100 (percent). Pass duration_ms to a movement function to
have it stop automatically after that time; leave it out to keep moving
until you call stop().

The line sensors share their pins with buttons A and B, so on the Classic
a program can't tell a button press from a line sensor reading.
"""
from microbit import pin0, pin1, pin2, pin5, pin8, pin11, pin12, pin13, pin14, pin15, pin16, sleep
from utime import ticks_us, sleep_us
import neopixel

# Pins (see https://4tronix.co.uk/blog/?p=2317)
_LEFT_A, _LEFT_B = pin0, pin8
_RIGHT_A, _RIGHT_B = pin1, pin12
_BUZZER = pin14
_SONAR = pin15
_LIGHT = pin2          # both light sensors are read on this pin...
_LIGHT_SELECT = pin16  # ...and this one chooses which: 0 = left, 1 = right
_LINE_LEFT = pin11     # shared with button B
_LINE_RIGHT = pin5     # shared with button A

NUM_LEDS = 12  # 0-5 left arm, 6-11 right arm

# Handy colours for led_on() and leds_on()
RED = (60, 0, 0)
GREEN = (0, 60, 0)
BLUE = (0, 0, 60)
YELLOW = (60, 40, 0)
PURPLE = (40, 0, 40)
WHITE = (40, 40, 40)

_leds = neopixel.NeoPixel(pin13, NUM_LEDS)


def _drive(pin_a, pin_b, power):
    """Set one motor. power is -100 (full reverse) to 100 (full forward)."""
    power = max(-100, min(100, power))
    pwm = int(abs(power) * 1023 / 100)
    if power >= 0:
        pin_a.write_analog(pwm)
        pin_b.write_analog(0)
    else:
        pin_a.write_analog(0)
        pin_b.write_analog(pwm)


def _set_motors(left, right, duration_ms=None):
    _drive(_LEFT_A, _LEFT_B, left)
    _drive(_RIGHT_A, _RIGHT_B, right)
    if duration_ms is not None:
        sleep(duration_ms)
        stop()


# ---------------------------------------------------------------- movement
def move_forward(speed=50, duration_ms=None):
    """Drive both wheels forward.

    Args:
        speed: Motor power from 0 (stopped) to 100 (full speed). Very low
            values may not be enough to turn the wheels. Default 50.
        duration_ms: How long to drive, in milliseconds. The robot stops
            when the time is up and the function then returns. If None
            (the default) the function returns immediately and the robot
            keeps driving until stop() or another movement is called.

    Example:
        bot.move_forward(60, 2000)  # forward for 2 seconds, then stop
    """
    _set_motors(speed, speed, duration_ms)


def move_backwards(speed=50, duration_ms=None):
    """Drive both wheels backwards.

    Args:
        speed: Motor power from 0 (stopped) to 100 (full speed). Default 50.
        duration_ms: How long to drive, in milliseconds, before stopping.
            If None (the default) the robot keeps reversing until stop()
            or another movement is called.

    Example:
        bot.move_backwards(40, 500)  # reverse for half a second
    """
    _set_motors(-speed, -speed, duration_ms)


def turn_left(speed=50, duration_ms=None):
    """Spin on the spot, anticlockwise (left wheel back, right wheel forward).

    Args:
        speed: Motor power from 0 (stopped) to 100 (full speed). Default 50.
        duration_ms: How long to turn, in milliseconds, before stopping.
            If None (the default) the robot keeps turning until stop()
            or another movement is called. The angle turned depends on
            speed, duration and surface, so you will need to experiment.

    Example:
        bot.turn_left(50, 600)  # roughly a quarter turn on a smooth floor
    """
    _set_motors(-speed, speed, duration_ms)


def turn_right(speed=50, duration_ms=None):
    """Spin on the spot, clockwise (left wheel forward, right wheel back).

    Args:
        speed: Motor power from 0 (stopped) to 100 (full speed). Default 50.
        duration_ms: How long to turn, in milliseconds, before stopping.
            If None (the default) the robot keeps turning until stop()
            or another movement is called.

    Example:
        bot.turn_right(50, 600)
    """
    _set_motors(speed, -speed, duration_ms)


def stop():
    """Stop both motors immediately.

    Example:
        bot.move_forward()   # no duration: keeps going
        sleep(1000)
        bot.stop()
    """
    _set_motors(0, 0)


# -------------------------------------------------------------------- LEDs
def led_on(led, colour=WHITE):
    """Turn on a single LED, leaving the others unchanged.

    The BitBot has 12 RGB LEDs: 0-5 on the left arm and 6-11 on the right.
    To control all of them at once use leds_on().

    Args:
        led: Which LED to light, 0 to 11.
        colour: An (r, g, b) tuple, each value from 0 to 255. Use your
            own, e.g. (0, 50, 50), or a built-in: RED, GREEN, BLUE, YELLOW,
            PURPLE, WHITE. Default WHITE. Keep values low (under about
            60) as the LEDs are very bright.

    Example:
        bot.led_on(0, bot.GREEN)    # first LED green
        bot.led_on(11, (0, 0, 50))  # last LED blue
    """
    _leds[led] = colour
    _leds.show()


def led_off(led):
    """Turn off a single LED, leaving the others unchanged.

    Args:
        led: Which LED to turn off, 0 to 11.

    Example:
        bot.led_off(3)
    """
    led_on(led, (0, 0, 0))


def leds_on(colour=WHITE):
    """Turn on all 12 LEDs in the same colour.

    Args:
        colour: An (r, g, b) tuple, each value from 0 to 255, or a
            built-in colour such as RED. Default WHITE.

    Example:
        bot.leds_on(bot.RED)      # all LEDs red
        bot.leds_on((0, 50, 50))  # all LEDs a custom colour
    """
    for i in range(NUM_LEDS):
        _leds[i] = colour
    _leds.show()


def leds_off():
    """Turn off all 12 LEDs.

    Example:
        bot.leds_off()
    """
    leds_on((0, 0, 0))


# ------------------------------------------------------------------ buzzer
def buzzer(duration_ms=200):
    """Sound the buzzer at its fixed tone (about 2.4kHz).

    The buzzer is a simple on/off type, so the pitch cannot be changed.
    The function waits until the beep has finished.

    Args:
        duration_ms: Length of the beep in milliseconds. Default 200.

    Example:
        bot.buzzer(500)  # half-second beep
    """
    _BUZZER.write_digital(1)
    sleep(duration_ms)
    _BUZZER.write_digital(0)


# ----------------------------------------------------------------- sensors
def get_distance(timeout_us=30000):
    """Measure the distance to the nearest object with the ultrasonic sensor.

    Works best on hard, flat surfaces facing the sensor. Soft or angled
    objects may not reflect the sound back. Readings take up to about
    30 ms, so don't call it more often than every 50 ms or so.

    Args:
        timeout_us: How long to wait for the echo, in microseconds, before
            giving up. The default (30000) corresponds to about 5 m.

    Returns:
        The distance in centimetres as a whole number, or -1 if no echo
        was received (nothing in range, or the object reflected no sound).

    Example:
        if 0 <= bot.get_distance() < 15:
            bot.stop()   # something is closer than 15 cm
    """
    _SONAR.write_digital(1)
    sleep_us(10)
    _SONAR.write_digital(0)
    _SONAR.set_pull(_SONAR.NO_PULL)

    t0 = ticks_us()
    while _SONAR.read_digital() == 0:
        if ticks_us() - t0 > timeout_us:
            return -1
    start = ticks_us()
    while _SONAR.read_digital() == 1:
        if ticks_us() - start > timeout_us:
            return -1
    return int(0.01715 * (ticks_us() - start))


def get_left_light():
    """Read the left light sensor.

    Returns:
        A number from 0 (dark) to 1023 (very bright). Readings depend on
        the room lighting, so measure your own thresholds.

    Example:
        if bot.get_left_light() > bot.get_right_light():
            bot.turn_left(30)   # turn towards the light
    """
    _LIGHT_SELECT.write_digital(0)
    return _LIGHT.read_analog()


def get_right_light():
    """Read the right light sensor.

    Returns:
        A number from 0 (dark) to 1023 (very bright).

    Example:
        print(bot.get_right_light())
    """
    _LIGHT_SELECT.write_digital(1)
    return _LIGHT.read_analog()


def get_left_line():
    """Read the left line-following sensor (underneath the robot).

    This sensor shares its pin with button B, so pressing B changes
    the reading.

    Returns:
        1 means "over the line"
        0 means "not over the line"

    Example:
        on_line = bot.get_left_line() == 1
    """
    return _LINE_LEFT.read_digital()


def get_right_line():
    """Read the right line-following sensor (underneath the robot).

    This sensor shares its pin with button A, so pressing A changes
    the reading.

    Returns:
        1 means "over the line"
        0 means "not over the line"

    Example:
        on_line = bot.get_right_line() == 1
    """
    return _LINE_RIGHT.read_digital()
