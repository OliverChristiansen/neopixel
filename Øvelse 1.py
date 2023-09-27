from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12 
p = 26 
np = NeoPixel(Pin(p, Pin.OUT), n) 
 
np[0] = (0, 255, 0) 
np[1] = (0, 255, 0)
np[2] = (0, 255, 0)
np[3] = (0, 0, 255)
np[4] = (0, 0, 255)
np[5] = (0, 0, 255)
np[6] = (255, 0, 0)
np[7] = (255, 0, 0)
np[8] = (255, 0, 0)
np[9] = (255, 255, 0)
np[10] = (255, 255, 0)
np[11] = (255, 255, 0)


np.write()