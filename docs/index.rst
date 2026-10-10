BitBot XL library
=================

``bitbotXL.py`` lets you control the 4tronix BitBot XL with simple functions
from a micro:bit MicroPython program.

.. toctree::
   :maxdepth: 2

   api

Getting started
---------------

1. Upload **both** ``main.py`` (your program) and ``bitbotXL.py`` to the
   micro:bit.
2. At the top of your program, import the library::

      from microbit import *
      import bitbotXL as bot

3. Call functions with the ``bot.`` prefix::

      bot.move_forward(50, 1000)   # forward at half speed for 1 second
      print(bot.get_distance())

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Function
     - What it does
   * - :func:`~bitbotXL.move_forward`
     - Drive forwards
   * - :func:`~bitbotXL.move_backwards`
     - Drive backwards
   * - :func:`~bitbotXL.turn_left`
     - Spin anticlockwise
   * - :func:`~bitbotXL.turn_right`
     - Spin clockwise
   * - :func:`~bitbotXL.stop`
     - Stop the motors
   * - :func:`~bitbotXL.led_on` / :func:`~bitbotXL.led_off`
     - Turn one LED on / off by index
   * - :func:`~bitbotXL.leds_on` / :func:`~bitbotXL.leds_off`
     - Turn all LEDs on / off
   * - :func:`~bitbotXL.buzzer`
     - Beep
   * - :func:`~bitbotXL.get_distance`
     - Ultrasonic distance in cm
   * - :func:`~bitbotXL.get_left_light` / :func:`~bitbotXL.get_right_light`
     - Light level
   * - :func:`~bitbotXL.get_left_line` / :func:`~bitbotXL.get_right_line`
     - Line sensors
