# BitBotXLzero

A small MicroPython library for driving the [4tronix BitBot XL](https://4tronix.co.uk/blog/?p=2317)
robot from a BBC micro:bit. It wraps the motors, LEDs, buzzer and sensors in
simple functions such as `move_forward()` and `get_distance()`.

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

## What it can do

| Function | What it does |
|---|---|
| `move_forward(speed, duration_ms)` | Drive forwards |
| `move_backwards(speed, duration_ms)` | Drive backwards |
| `turn_left(speed, duration_ms)` | Spin anticlockwise |
| `turn_right(speed, duration_ms)` | Spin clockwise |
| `stop()` | Stop the motors |
| `led_on(led, colour)` / `led_off(led)` | Turn one LED on / off by index |
| `leds_on(colour)` / `leds_off()` | Turn all LEDs on / off |
| `buzzer(duration_ms)` | Beep |
| `get_distance()` | Ultrasonic distance in cm |
| `get_left_light()` / `get_right_light()` | Light level |
| `get_left_line()` / `get_right_line()` | Line sensors |

Speeds are from 0 (stopped) to 100 (full speed). If you give a `duration_ms`,
the robot moves for that long and then stops; if you leave it out, it keeps
going until you call `stop()` or another movement function.

The full reference is online at
[bitbotxlzero.readthedocs.io](https://bitbotxlzero.readthedocs.io/en/latest/).
It is also in [bitbotXL.md](bitbotXL.md), and
[bitbotXL_cheatsheet.pdf](bitbotXL_cheatsheet.pdf) is a printable summary.

## Example

Drive forwards and stop before hitting a wall:

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

The documentation in [docs/](docs/) is built with Sphinx:

```
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs docs/_build/html
```

Then open `docs/_build/html/index.html`.
