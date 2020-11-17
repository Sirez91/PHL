from mido import MidiFile

mid = MidiFile("vivaldi_spring_pn.mid")

for i, track in enumerate(mid.tracks):
    notesArray = []
    print('Track {}: {}'.format(i, track.name))
    notesPressed = []
    notesReleased = []
    for msg in track:
        print(msg)
        if (msg.type == "note_on"):
            notesPressed.append(msg.note)
        if (msg.type == "note_off"):
            notesReleased.append(msg.note)
            if (len(notesPressed) == len(notesReleased)):
                notesArray.append(notesPressed)
                notesPressed = []
                notesReleased = []
    print(notesArray)
