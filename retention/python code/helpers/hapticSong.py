import time
import serial
from helpers.motor_dictionary import notes_to_motor
from helpers.stoppableThread import StoppableThread
from helpers.usbPorts import gloveUSB, ledUSB
from pygame import midi

class pup(StoppableThread):
    def __init__(self, fullSong, songName, *args, **kwargs):
        self.song = fullSong
        self.songName = songName
        super(pup, self).__init__(*args, **kwargs)

    def run(self):
        midi.init()
        try:
            output = midi.Output(2)
        except Exception as e:
            print("Problem with keyboard output")
            print(e)
            exit()
        ser = serial.Serial(gloveUSB, 9600)
        time.sleep(2)
        print(self.song)
        package = 'passive'
        if self.stopped():
            return
        for key in self.song:
            package= package + "," + str(notes_to_motor[key[0]]) + ":" + str(key[1])
        print(package)
        t_end = time.time() + 60 * 20
        while (time.time() < t_end ):
            ser.write(package.encode())
            time.sleep(1)
            # serLed = serial.Serial(ledUSB, 9600)
            # time.sleep(2)
            # serLed.write(self.songName.encode())
            # time.sleep(1)
            for key in self.song:
                time.sleep(100 / 1000)
                output.note_on(key[0], 80, 0)
                time.sleep(key[1] / 1000)
                output.note_off(key[0], 0, 0)
            time.sleep(20)