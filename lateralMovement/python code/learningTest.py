import sys, getopt
import subprocess
import signal
import os
from helpers.dwt_hard import compareSongs

if (os.system('arecordmidi -l | grep CASIO') != 0):
    print("Piano is not connect")
    sys.exit()

usage = 'learningTest.py -i <id> -a <attempt> -c <condition>'
id = 0
attempt = ""
condition = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:a:c:",["id=","attpemt=","condition="])
except getopt.GetoptError:
    print(usage)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(usage)
        sys.exit()
    elif opt in ("-i", "--id"):
        try:
            id = int(arg)
        except Exception as e:
            print("id was not an integer")
    elif opt in ("-a", "--attpemt"):
        attempt = arg
    elif opt in ("-c", "--condition"):
        condition = arg
        if(condition != "active" and condition != "passive"):
            print("The condition has to be either 'active' or 'passive'")
            sys.exit()

if (id == 0 and attempt == "" and condition == ""):
    print(usage)
    sys.exit()

path = "~/PHL/retentionData/" + str(id) + '/' + condition + 'Learn/'
port = subprocess.Popen("arecordmidi -l |  awk '$2 ~ /CASIO/ {print $1}'", shell=True, stdout=subprocess.PIPE)
x = subprocess.Popen('arecordmidi -p ' +
                     port.stdout.read().decode("utf-8").rstrip() +
                     ' ' + path +
                     attempt + ".mid",
                     shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

print("Started Capture")
print("Press Enter to Stop Capture")
input()
print("Stopping Capture")
os.killpg(os.getpgid(x.pid), signal.SIGTERM)
originalSong="path"
justPlayed = path + attempt + ".mid"
print(compareSongs(originalSong, justPlayed))