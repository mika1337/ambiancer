#!/usr/bin/env python3

import time

from ambiancer.bh1750 import BH1750
from ambiancer.rpibacklight import RpiBacklight

bh1750 = BH1750(1)
rb = RpiBacklight()

def luxToBrightness( lux ):
    if lux == 0:
        b = 0
    else:
        b = int(lux * 2)
        b = max(b,16)
        b = min(b,40)
    return b

direction       = 0
prev_direction  = 0
prev_brightness = 0

while True:
    lux = bh1750.read()
    brightness = luxToBrightness( lux )

    print("%3.1f lx => %d" % (lux,brightness))
    rb.setBrightness( brightness, transition=True)

    time.sleep(1)
