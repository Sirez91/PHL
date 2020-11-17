import sys, getopt
import subprocess
import signal
import os
from helpers.dwt_hard import compareSongs
from helpers.songs import getSongs
from helpers.fileChecker import fileExists

if (os.system('arecordmidi -l | grep CASIO') != 0):
    print("Piano is not connect")
    sys.exit()

usage = 'learningTest.py -i <id> -a <attempt> -c <condition> -s <session>'
ident = 0
attempt = ""
condition = ""
session = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:a:c:s:",["id=","attpemt=","condition=","session="])
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
    elif opt in ("-a", "--attpemt"):
        attempt = arg
    elif opt in ("-c", "--condition"):
        condition = arg
    elif opt in ("-s", "--session"):
        session = arg

if (ident == 0 or attempt == "" or condition == "" or session == ""):
    print(usage)
    sys.exit()

if(session != "1" and session != "2" and
    session != "1-aided" and session != "2-aided"):
    print("The session has to be either '1', '2', '1-aided' or '2-aided'")
    sys.exit()

if(condition != "active" and condition != "passive"):
    print("The condition has to be either 'active' or 'passive'")
    sys.exit()

path = "/home/teco/PHL/retentionData/" + str(ident) + '/' + condition + '/session' + session + '/'

#check if file exists
if(fileExists(path+attempt+".mid")):
    print("file exists")
    sys.exit()

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
songName, song = getSongs(ident, condition)
if (songName == "songA"):
   originalSong="/home/teco/PHL/audio/RetentionPhraseA.mid"
else:
   originalSong="/home/teco/PHL/audio/RetentionPhraseB-10.mid"
justPlayed = path + attempt + ".mid"
print(compareSongs(originalSong, justPlayed))
