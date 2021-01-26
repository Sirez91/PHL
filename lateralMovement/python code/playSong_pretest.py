from pygame import midi
from helpers.usbPorts import ledUSB, gloveUSB
import time
import serial
import sys, getopt
from helpers.songs import getSongPart, getSongs

id = 0
condition = ''
part = 0
usage = "playSong_pretest.py -i id -c gold/gnew"
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:c:p:",["id=","condition=","part="])
except getopt.GetoptError:
    print('playSong.py -i <id>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('test.py -i <id>')
        sys.exit()
    elif opt in ("-i", "--id"):
        try:
            id = int(arg)
        except Exception as e:
            print("id was not an integer")
    elif opt in ("-c", "--condition"):
        condition = arg
        if(condition != "gold" and condition != "gnew"):
            print("The condition has to be either 'gold' or 'gnew'")
            sys.exit()
    elif opt in ("-p", "--part"):
        part = int(arg)
        if(part != 0 and part != 1 and part != 2 and part != 1 and part != 4 and part != 12 and part != 34):
            print("The session has to be either '1', '2', '3' or '4'")
            sys.exit()

if (id == 0 or condition == ""):
    print(usage)
    sys.exit()

if part == 0:
    songName, song = getSongs(id, condition)
else:
    songName, song = getSongPart(id, condition, part)
print(songName)
print(song)

KEYDOWN = 144
KEYUP = 128

midi.init()
try:
    output = midi.Output(2)
except Exception as e:
    print("Problem with keyboard output")
    print(e)
    exit()

if(condition == "gnew") {
    
}
#serGlove = serial.Serial(gloveUSB, 9600)
#time.sleep(2)
#serGlove.write(songName.encode())
#time.sleep(1)
i = 0
while i < len(song):
    if i > 0:
        time.sleep(song[i][2]/1000)
    output.note_on(song[i][0], 80, 0)
    if i+1 != len(song) and song[i+1][2] == 0:
        output.note_on(song[i+1][0], 80, 0)
        time.sleep(song[i][1]/1000)
        output.note_off(song[i][0], 0, 0)
        output.note_off(song[i+1][0], 0, 0)
        i = i+2
    else:
        time.sleep(song[i][1]/1000)
        output.note_off(song[i][0], 0, 0)
        i = i+1
