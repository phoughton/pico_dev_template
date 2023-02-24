# Description: Example of flashing an LED on the board
from machine import Pin
from time import sleep
import config

pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
    sleep(config.DURATION_OF_BLINK)
