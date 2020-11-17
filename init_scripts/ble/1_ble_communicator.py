from bluepy.btle import Scanner, DefaultDelegate, Peripheral, ADDR_TYPE_RANDOM
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

#peripheral = Peripheral("e8:d1:61:ef:b8:27", ADDR_TYPE_RANDOM, 0)
#peripheral = Peripheral("E0:DB:F3:E1:17:C0", ADDR_TYPE_RANDOM, 0)
peripheral = Peripheral("fd:2e:d8:e9:16:61", ADDR_TYPE_RANDOM, 0)
services = peripheral.getServices()

for i in services:
    for j in i.getCharacteristics():
        if j.properties == 14:
            characteristics = j

key = bytes([0xff, 0xff, 0xff, 0xff])
characteristics.write(key)
time.sleep(10)
key = bytes([0x00, 0x00, 0x00, 0x00])
characteristics.write(key)

