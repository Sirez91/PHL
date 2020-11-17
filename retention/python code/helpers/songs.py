songA = [74,
         76,
        77,
        76,
        74,
        76,
        79,
        72,
        76,
        72
]

timeBetweenNotesA = [
        0,14,14,14,7,7,14,14,14,14
]

durationNotesA = [
        237, 237, 237, 118, 118, 237, 237, 237, 237, 474
]

#key, note duration, time between notes 120
# fullSongA = [
#         [74,237,0],
#         [76,237,14],
#         [77,237,14],
#         [76,118,14],
#         [74,118,7],
#         [76,237,7],
#         [79,237,14],
#         [72,237,14],
#         [76,237,14],
#         [72,474,14]
# ]

#key, note duration, time between notes 70
fullSongA = [
        [74,434,0],
        [76,434,25],
        [77,434,25],
        [76,216,25],
        [74,216,13],
        [76,434,13],
        [79,434,25],
        [72,434,25],
        [76,434,25],
        [72,869,25]
]

songB = [72,
74,
76,
72,
79,
77,
74,
74,
77,
76,
72
]

#key, note duration, time between notes 70
fullSongB = [
        [72,434,0],
        [74,434,25],
        [76,434,25],
        [72,434,25],
        [79,434,25],
        [77,434,48],
        [74,434,25],
        [77,434,25],
        [76,434,25],
        [72,869,25]
]

def getSongs(id, phase):
        if (phase == "active"):
                if ((id % 2) == 0):
                        songName = "songB"
                        song = fullSongB
                else:
                        songName = "songA"
                        song = fullSongA
        else:
                if ((id % 2) == 0):
                        songName = "songA"
                        song = fullSongA
                else:
                        songName = "songB"
                        song = fullSongB
        return songName, song