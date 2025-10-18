import tinybit
from microbit import display, Image, sleep

# Display an arrow
display.show(Image.ARROW_S)

# Move the TinyBit car forward at speed 150.
tinybit.car_run(150)

# Pause the execution of the program for 2 seconds.
sleep(2000)

# Stop the TinyBit car after the specified duration has elapsed.
tinybit.car_stop()
