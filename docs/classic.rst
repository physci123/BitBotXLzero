BitBot Classic
==============

.. currentmodule:: bitbotClassic

``bitbotClassic.py`` is the same library for the older BitBot Classic. It has
exactly the same functions as ``bitbotXL.py``, so a program written for one
robot works on the other by changing only the import line::

   from microbit import *
   import bitbotClassic as bot

Upload ``bitbotClassic.py`` to the micro:bit instead of ``bitbotXL.py``.

What is different
-----------------

The line sensors share their pins with the micro:bit's buttons: the left
sensor with button B and the right sensor with button A. A program can't tell
a button press from a line sensor reading, so don't use the buttons in a
program that follows a line.

Everything else behaves the same as on the BitBot XL.

Functions
---------

.. autofunction:: move_forward
.. autofunction:: move_backwards
.. autofunction:: turn_left
.. autofunction:: turn_right
.. autofunction:: stop
.. autofunction:: led_on
.. autofunction:: led_off
.. autofunction:: leds_on
.. autofunction:: leds_off
.. autofunction:: buzzer
.. autofunction:: get_distance
.. autofunction:: get_left_light
.. autofunction:: get_right_light
.. autofunction:: get_left_line
.. autofunction:: get_right_line
