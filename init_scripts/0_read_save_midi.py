# Import the PyGame package, with the MIDI functionality specifically
from pygame import midi
# mido to write the midi data to file
from mido import Message, MidiFile, MidiTrack, tick2second

#Define constants
KEYDOWN = 144
KEYUP = 128

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# To use MIDI functionality, we need to first initialize MIDI
midi.init()

# List the MIDI devices that can be used
for i in range(0, midi.get_count()):
    print(i, midi.get_device_info(i))

# Start the input stream
try:
    # input = midi
    input = midi.Input(3)
except Exception as e:
    print("Problem with keyboard input")
    print(e) 
    exit()

print('Entering loop')
boolean = True
while (boolean):

    # Detect keypress on input
    if input.poll():

        # Get MIDI event information
        eventlist = input.read(1000)
        print(eventlist)
        for e in eventlist:
            print(e)
            print(e[1])
            if (e[0][1] == 36):
                mid.save('new_song1.mid')
                boolean = False
                break
            if (e[0][0] == KEYDOWN):
                track.append(Message('note_on', note=e[0][1], velocity=e[0][2], time=midi.time()))
            elif (e[0][0] == KEYUP):
                track.append(Message('note_off', note=e[0][1], velocity=e[0][2], time=midi.time()))
input.close()
# Close the midi interface
midi.quit()
