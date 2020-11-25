from pygame import midi
from helpers.usbPorts import ledUSB, gloveUSB
import time
import serial
import sys
import getopt
from helpers.songs import getSongPart, getSongs
from mido import MidiFile
import subprocess
import signal
from helpers.fileChecker import fileExists
import os

pathPrefix = '/home/marc/Bachelorarbeit/data/'
id = 0
condition = ''
part = 0
attempt = 0
usage = "playSong.py -i id -c gold/gnew -p 1/2/3/4/12/34"
try:
    opts, args = getopt.getopt(sys.argv[1:],
                               "hi:c:p:",
                               ["id=", "condition=", "part="])
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
        if(part != 0 and part != 1 and
           part != 2 and part != 3 and
           part != 4 and part != 12 and part != 34):
            print("The session has to be either '1', '2', '3' or '4'")
            sys.exit()

if id == 0 or condition == "":
    print(usage)
    sys.exit()

if part == 0:
    songName, song = getSongs(id, condition)
else:
    songName, song = getSongPart(id, condition, part)
print(songName)
print(song)
# songName_LED = songName
songName_LED = songName.split(":")[1]
# print(songName_LED)

KEYDOWN = 144
KEYUP = 128

midi.init()
try:
    output = midi.Output(2)
except Exception as e:
    print("Problem with keyboard output")
    print(e)
    exit()

#get serials for peripherials
serLed = serial.Serial(ledUSB, 9600)
serGlove = serial.Serial(gloveUSB, 9600)
time.sleep(2)
#send song to peripherilas
serLed.write(songName_LED.encode())
serGlove.write(songName.encode())
time.sleep(1)
notes_list_orig = []
i = 0
while i < len(song):
    if i > 0:
        time.sleep(song[i][2]/1000)
    output.note_on(song[i][0], 80, 0)
    # add note to list
    notes_list_orig.append(song[i][0])
    if i+1 != len(song) and song[i+1][2] == 0:
        output.note_on(song[i+1][0], 80, 0)
        notes_list_orig.append(song[i+1][0])
        time.sleep(song[i][1]/1000)
        output.note_off(song[i][0], 0, 0)
        output.note_off(song[i+1][0], 0, 0)
        i = i+2
    else:
        time.sleep(song[i][1]/1000)
        output.note_off(song[i][0], 0, 0)
        i = i+1

# find a file name to save
path_file = pathPrefix + str(id) + '/' + condition + '/'
found_file = False
file_name = part
i = 0
while not found_file:
    # check if file exists
    if fileExists(path_file+str(file_name)+".mid"):
        file_name = str(part) + "_" + str(i)
        i = i + 1
    else:
        found_file = True

port = subprocess.Popen("arecordmidi -l |  awk '$2 ~ /CASIO/ {print $1}'",
                        shell=True, stdout=subprocess.PIPE)
x = subprocess.Popen('arecordmidi -p ' +
                     port.stdout.read().decode("utf-8").rstrip() +
                     ' ' + path_file +
                     str(file_name) + ".mid",
                     shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

print("Started Capture")
print("Press Enter to Stop Capture")
input()
print("Stopping Capture")
os.killpg(os.getpgid(x.pid), signal.SIGTERM)


print("printing notes")
print(notes_list_orig)
mid = MidiFile(path_file + str(file_name)+'.mid', clip=True)
for i, track in enumerate(mid.tracks):
    notesArray = []
    for msg in track:
        if msg.type == "note_on":
            notesArray.append(msg.note)
    print(notesArray)
