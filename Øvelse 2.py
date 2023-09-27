from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)
def set_color(r, g, b):
            for pixel in range(n):
                np[pixel] = (r, g, b)
                np.write()

def clear():
    for pixel in range(n):
        np[pixel] = (0, 0, 0)
    np.write()
# lav en variabel som inkrementerer med 1 for hver omgang i loopet
# når variablens værdi er 10 eller højere, så stop loopet
count = 1
while True:
    set_color(255, 0, 0)
    sleep(0.5)
    set_color(0, 0, 0)
    sleep(0.5)
    count += 1
    print(count)
    if count == 11:
        break
    
    
    
    
    
    



                    