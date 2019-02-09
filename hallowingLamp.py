# The most basic of basic neopixel programs, written for a small desk light I made using
# a neo-pixel strip.

import board
import neopixel
import random
import time

pixels = neopixel.NeoPixel(board.EXTERNAL_NEOPIXEL, 30,brightness=1,auto_write=False)

while True:
    pixels.fill((255,45,0)) #Solid Orange

    #pixels[(random.randint(0,29))] = ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))) #Rainbow colors

    ''' pixels[(random.randint(0,29))] = (255,45,0) #Flickering orange
    pixels.show()
    time.sleep(0.01)
    pixels[(random.randint(0,29))] = (255,45,0)
    pixels.show()
    time.sleep(0.01)
    pixels[(random.randint(0,29))] = (0,0,0)
    pixels.show()
    time.sleep(0.01) '''
