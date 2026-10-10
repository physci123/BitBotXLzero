Function reference
==================

.. currentmodule:: bitbotXL

These are the functions in ``bitbotXL.py``. The BitBot Classic library,
``bitbotClassic.py``, has exactly the same functions; see :doc:`classic` for
what is different on that robot.

Movement
--------

Speeds are from 0 (stopped) to 100 (full speed). Give a ``duration_ms`` and
the robot stops by itself after that time; leave it out and the robot keeps
going until you call :func:`stop`.

.. autofunction:: move_forward
.. autofunction:: move_backwards
.. autofunction:: turn_left
.. autofunction:: turn_right
.. autofunction:: stop

LEDs
----

The BitBot has 12 RGB LEDs numbered 0 to 11: 0-5 on the left arm and 6-11 on
the right arm. Functions with ``led`` (singular) control one LED by index;
functions with ``leds`` (plural) control all of them.

Colours are ``(red, green, blue)`` tuples with each value from 0 to 255. These
are built in: ``RED``, ``GREEN``, ``BLUE``, ``YELLOW``, ``PURPLE``, ``WHITE``.

.. autofunction:: led_on
.. autofunction:: led_off
.. autofunction:: leds_on
.. autofunction:: leds_off

Buzzer
------

.. autofunction:: buzzer

Sensors
-------

.. autofunction:: get_distance
.. autofunction:: get_left_light
.. autofunction:: get_right_light
.. autofunction:: get_left_line
.. autofunction:: get_right_line
