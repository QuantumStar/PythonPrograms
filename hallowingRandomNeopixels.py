import time
import board
import neopixel
import random
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

led.brightness = 1.0

while True:
    led[0] = (255, 45, 0)
    
