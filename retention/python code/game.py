import os, sys, getopt
import threading
import subprocess
import signal
from time import sleep
from helpers.hapticSong import pup
from helpers.songs import fullSongB, fullSongA, getSongs


class GameController:
    __instance = None
    stop_threads = False

    @staticmethod
    def getInstance():
        if GameController.__instance == None:
            GameController()
        return GameController.__instance

    def __init__(self):
        if GameController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GameController.__instance = self

    def startGame(self, song, songName, phase, ident):
        # start game
        self.x = subprocess.Popen('gweled >> ~/PHL/retentionData/' + str(ident) + '/gweled/score' + phase + '.txt',
                             shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

        # start vibrations and audio
        self.thread = pup(song, songName)
        self.thread.start()

        #kill in 20 minutes
        self.y = threading.Thread(target=self.killAfterMinutes)
        self.y.start()

    def killAfterMinutes(self):
        sleep(20*60)
        self.thread.stop()
        GameController.stop_threads = True
        print("Game Stoped")
        os.killpg(os.getpgid(self.x.pid), signal.SIGTERM)

usage = 'game.py -i <id> -p <phase>'
ident = 0
phase = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:p:",["id=","phase="])
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
    elif opt in ("-p", "--phase"):
        phase = arg

if (ident == 0 or phase == ''):
    print(usage)
    sys.exit()

songName, song = getSongs(ident, "passive")
gameController = GameController()
gameController.startGame(song, songName, phase, ident)
