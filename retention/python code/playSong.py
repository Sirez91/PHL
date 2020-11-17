from pygame import midi
from helpers.usbPorts import ledUSB, gloveUSB
import time
import serial
import sys, getopt
from helpers.motor_dictionary import notes_to_motor
from helpers.songs import getSongs

usage = 'playSong.py -i <id> -c <condition>'
ident = 0
condition = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:c:",["id=","condition="])
except getopt.GetoptError:
    print(usage)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(usage)
        sys.exit()
    elif opt in ("-i", "--id"):
        try:
            ident = int(arg)
        except Exception as e:
            print("id was not an integer")
    elif opt in ("-c", "--condition"):
        condition = arg

if(condition != "active" and condition != "passive"):
    print("The condition has to be either 'active' or 'passive'")
    sys.exit()

songName, song = getSongs(ident, condition)

KEYDOWN = 144
KEYUP = 128

midi.init()
try:
    output = midi.Output(2)
except Exception as e:
    print("Problem with keyboard output")
    print(e)
    exit()

serLed = serial.Serial(ledUSB, 9600)
time.sleep(2)

serLed.write(songName.encode())
time.sleep(1)
for key in song:
    time.sleep(key[2]/1000)
    output.note_on(key[0], 80, 0)
    time.sleep(key[1]/1000)
    output.note_off(key[0], 0, 0)

output.close()
midi.quit()
