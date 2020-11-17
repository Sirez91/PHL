songA = [
    76,
    79,
    84,
    60,
    64,
    67,
    72,
    71,
    76,
    67,
    76,
    69,
    74,
    71,
    79,
    84,
    79,
    84,
    67,
    72,
    64,
    67
]

timeBetweenNotesA = [
    0,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    0,
    48,
    0,
    48,
    0,
    48,
    0
]

durationNotesA = [
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    0,
    869,
    0,
    869,
    0,
    869,
    0
]


fingersrsA = [
    1, 3, 5, 1, 3, 5, 4, 3, 5, 1, 5, 1, 4, 2, 2, 5, 2, 5, 2, 5, 1, 2
]

# key, note duration, time between notes 70
fullSongA = [list(pair) for pair in zip(songA, durationNotesA, timeBetweenNotesA, fingersrsA)]

songB = [
    64,
    67,
    72,
    67,
    72,
    77,
    83,
    81,
    79,
    77,
    81,
    83,
    64,
    72,
    65,
    67,
    69,
    72,
    77,
    81,
    84,
    83,
    84,
    71,
    72
]

timeBetweenNotesB = [
    0,
    48,
    48,
    48,
    0,
    48,
    0,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48
]

durationNotesB = [
    869,
    869,
    869,
    869,
    0,
    869,
    0,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869,
    869
]

# key, note duration, time between notes 70
fingersrsB = [
    1, 2, 5, 2, 5, 2, 5, 4, 3, 2, 4, 5, 1, 5, 2, 3, 4, 5, 2, 3, 5, 4, 5, 4, 5
]

fullSongB = [list(pair) for pair in zip(songB, durationNotesB, timeBetweenNotesB, fingersrsB)]


def getSongs(id, phase):
    if (phase == "gold"):
        if ((id % 2) == 0):
            songName = "gold:songB"
            song = fullSongB
        else:
            songName = "gold:songA"
            song = fullSongA
    else:
        if ((id % 2) == 0):
            songName = "gnew:songA"
            song = fullSongA
        else:
            songName = "gnew:songB"
            song = fullSongB
    return songName, song


def getSongPart(id, phase, part):
    if (phase == "gold"):
        if ((id % 2) == 0):
            songName = "gold:songB_" + str(part)
            song = extractPart('songB', part)
        else:
            songName = "gold:songA_" + str(part)
            song = extractPart('songA', part)
    else:
        if ((id % 2) == 0):
            songName = "gnew:songA_" + str(part)
            song = extractPart('songA', part)
        else:
            songName = "gnew:songB_" + str(part)
            song = extractPart('songB', part)
    return songName, song


def extractPart(songName, part):
    song = []
    if (songName == "songA"):
        if (part == 1):
            song = fullSongA[0:4]
        elif (part == 2):
            song = fullSongA[4:8]
        elif (part == 3):
            song = fullSongA[8:14]
        elif (part == 4):
            song = fullSongA[14:22]
        elif (part == 12):
            song = fullSongA[0:8]
        elif (part == 34):
            song = fullSongA[8:22]
    else:
        if (part == 1):
            song = fullSongB[0:7]
        elif (part == 2):
            song = fullSongB[7:14]
        elif (part == 3):
            song = fullSongB[14:21]
        elif (part == 4):
            song = fullSongB[21:25]
        elif (part == 12):
            song = fullSongB[0:14]
        elif (part == 34):
            song = fullSongB[14:25]
    return song
