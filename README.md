# BitBotXLzero

A small MicroPython library for driving the [4tronix BitBot XL](https://4tronix.co.uk/blog/?p=2317)
robot from a BBC micro:bit. It wraps the motors, LEDs, buzzer and sensors in
simple functions such as `move_forward()` and `get_distance()`.

This reference is also online at
[bitbotxlzero.readthedocs.io](https://bitbotxlzero.readthedocs.io/en/latest/),
and [bitbotXL_cheatsheet.pdf](bitbotXL_cheatsheet.pdf) is a printable summary.

## Getting started

1. Upload **both** `main.py` (your program) and [bitbotXL.py](bitbotXL.py) to the micro:bit.
2. At the top of your program, import the library:

   ```python
   from microbit import *
   import bitbotXL as bot
   ```

3. Call functions with the `bot.` prefix:

   ```python
   bot.move_forward(50, 1000)   # forward at half speed for 1 second
   print(bot.get_distance())    # distance to the nearest object in cm
   ```

## Quick reference

| Function | What it does |
|---|---|
| [`move_forward(speed, duration_ms)`](#move_forward) | Drive forwards |
| [`move_backwards(speed, duration_ms)`](#move_backwards) | Drive backwards |
| [`turn_left(speed, duration_ms)`](#turn_left) | Spin anticlockwise |
| [`turn_right(speed, duration_ms)`](#turn_right) | Spin clockwise |
| [`stop()`](#stop) | Stop the motors |
| [`led_on(led, colour)`](#led_on) | Light one LED by index |
| [`led_off(led)`](#led_off) | Turn one LED off |
| [`leds_on(colour)`](#leds_on) | Light all LEDs |
| [`leds_off()`](#leds_off) | Turn all LEDs off |
| [`buzzer(duration_ms)`](#buzzer) | Beep |
| [`get_distance()`](#get_distance) | Ultrasonic distance in cm |
| [`get_left_light()`](#get_left_light) | Left light level |
| [`get_right_light()`](#get_right_light) | Right light level |
| [`get_left_line()`](#get_left_line) | Left line sensor |
| [`get_right_line()`](#get_right_line) | Right line sensor |

---

## Movement

Speeds are from **0 (stopped) to 100 (full speed)**. Very low speeds may not be
enough to turn the wheels.

If you give a `duration_ms`, the robot moves for that long and then stops. If
you leave it out, the function returns straight away and the robot keeps going
until you call `stop()` or another movement function.

### move_forward

```python
move_forward(speed=50, duration_ms=None)
```

Drive both wheels forwards.

| Parameter | Description |
|---|---|
| `speed` | 0 to 100. Default 50. |
| `duration_ms` | Time to drive in milliseconds, or `None` to keep going. |

```python
bot.move_forward(60, 2000)   # forward for 2 seconds, then stop
```

### move_backwards

```python
move_backwards(speed=50, duration_ms=None)
```

Drive both wheels backwards. Parameters are the same as `move_forward`.

```python
bot.move_backwards(40, 500)  # reverse for half a second
```

### turn_left

```python
turn_left(speed=50, duration_ms=None)
```

Spin on the spot, anticlockwise. The angle you turn depends on speed, duration
and the surface, so experiment to find a time that gives a quarter turn.

```python
bot.turn_left(50, 600)
```

### turn_right

```python
turn_right(speed=50, duration_ms=None)
```

Spin on the spot, clockwise. Parameters are the same as `turn_left`.

```python
bot.turn_right(50, 600)
```

### stop

```python
stop()
```

Stop both motors immediately.

```python
bot.move_forward()
sleep(1000)
bot.stop()
```

---

## LEDs

The BitBot has 12 RGB LEDs, numbered **0 to 11**: 0-5 on the left arm and 6-11
on the right arm.

Colours are `(red, green, blue)` tuples with each value from 0 to 255. The LEDs
are very bright, so keep values below about 60. These colours are built in:
`bot.RED`, `bot.GREEN`, `bot.BLUE`, `bot.YELLOW`, `bot.PURPLE`, `bot.WHITE`.

Functions with `led` in the name (singular) control **one** LED by its index.
Functions with `leds` (plural) control **all** of them.

### led_on

```python
led_on(led, colour=WHITE)
```

Turn on a single LED. The other LEDs are left as they were.

| Parameter | Description |
|---|---|
| `led` | LED index 0 to 11. |
| `colour` | An `(r, g, b)` tuple or a built-in colour. Default `WHITE`. |

```python
bot.led_on(0, bot.GREEN)    # first LED green
bot.led_on(11, (0, 0, 50))  # last LED blue
```

### led_off

```python
led_off(led)
```

Turn off a single LED. The other LEDs are left as they were.

| Parameter | Description |
|---|---|
| `led` | LED index 0 to 11. |

```python
bot.led_off(3)
```

### leds_on

```python
leds_on(colour=WHITE)
```

Turn on all 12 LEDs in the same colour.

| Parameter | Description |
|---|---|
| `colour` | An `(r, g, b)` tuple or a built-in colour. Default `WHITE`. |

```python
bot.leds_on(bot.RED)      # all LEDs red
bot.leds_on((0, 50, 50))  # all LEDs a custom colour
```

### leds_off

```python
leds_off()
```

Turn off all 12 LEDs.

```python
bot.leds_off()
```

---

## Buzzer

### buzzer

```python
buzzer(duration_ms=200)
```

Sound the buzzer. It is a simple on/off buzzer, so the pitch can't be changed.
The function waits until the beep has finished.

| Parameter | Description |
|---|---|
| `duration_ms` | Length of the beep in milliseconds. Default 200. |

```python
bot.buzzer(500)   # half-second beep
```

---

## Sensors

### get_distance

```python
get_distance(timeout_us=30000)
```

Measure the distance to the nearest object using the ultrasonic sensor.

**Returns:** the distance in centimetres (a whole number), or **-1** if no echo
was received (nothing in range, or the object didn't reflect any sound).

Notes:
- Works best on hard, flat objects facing the sensor. Soft or angled objects
  may not be detected.
- A reading takes up to about 30 ms, so don't call it more than every 50 ms or so.
- Remember to check for -1 before comparing distances!

```python
if 0 <= bot.get_distance() < 15:
    bot.stop()   # something is closer than 15 cm
```

### get_left_light

```python
get_left_light()
```

**Returns:** a number from 0 (dark) to 1023 (very bright). Readings depend on
the room lighting, so measure your own thresholds.

```python
if bot.get_left_light() > bot.get_right_light():
    bot.turn_left(30)   # turn towards the light
```

### get_right_light

```python
get_right_light()
```

**Returns:** a number from 0 (dark) to 1023 (very bright).

```python
print(bot.get_right_light())
```

### get_left_line

```python
get_left_line()
```

Read the left line-following sensor, underneath the robot.

**Returns:** `1` if the sensor is over the line, `0` if not (or if the sensor
could not be read).

```python
on_line = bot.get_left_line() == 1
```

### get_right_line

```python
get_right_line()
```

Read the right line-following sensor. Returns the same as `get_left_line`.

```python
on_line = bot.get_right_line() == 1
```

---

## Examples

### Stop before a wall

```python
from microbit import *
import bitbotXL as bot

bot.move_forward(40)
while True:
    d = bot.get_distance()
    if 0 <= d < 15:
        bot.stop()
        bot.buzzer(300)
        break
    sleep(60)
```

### More programs

More complete programs are in [Examples/](Examples/):

- [LineFollower.py](Examples/LineFollower.py) follows a black line using the two line sensors.
  [linefollowtiles.pdf](linefollowtiles.pdf) has printable track tiles.
- [KeepDistance.py](Examples/KeepDistance.py) holds the robot 10 cm from whatever is in front of it.

Upload either one as `main.py` alongside `bitbotXL.py`, then press A to start
and B to stop.

## Testing the hardware

[Hardware_test.py](Hardware_test.py) checks each part of the robot in turn.
Upload it as `main.py`; each test scrolls its name on the display and runs
when you press A.

## Building the docs

The documentation in [docs/](docs/) is built with Sphinx and hosted on
[Read the Docs](https://bitbotxlzero.readthedocs.io/en/latest/), which rebuilds
it on every push. To build it locally:

```
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs docs/_build/html
```

Then open `docs/_build/html/index.html`.

## License

Released under the [MIT License](LICENSE).
