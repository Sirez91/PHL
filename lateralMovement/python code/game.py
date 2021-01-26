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

    def startGame(self, song, songName, id, condition):
        # start game
        self.x = subprocess.Popen(f'gweled >> ~/Bachelorarbeit/data/{id}/{condition}/game.txt',
                             shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

        # start vibrations and audio
        self.thread = pup(song, songName)
        self.thread.start()

        #kill in 20 minutes
        self.y = threading.Thread(target=self.killAfterMinutes)
        self.y.start()

    def killAfterMinutes(self):
        sleep(30)#sleep(30*60)
        self.thread.stop()
        GameController.stop_threads = True
        print("Game Stoped")
        os.killpg(os.getpgid(self.x.pid), signal.SIGTERM)

id = 0
condition = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:c:",["id=","condition="])
except getopt.GetoptError:
    print('game.py -i <id>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('game.py -i <id> -c <condition>')
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


songName, song = getSongs(id, condition)
gameController = GameController()
gameController.startGame(song, songName, id, condition)
