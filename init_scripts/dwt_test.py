#Test dtw
#Based on https://github.com/pierre-rouanet/dtw
from math import isinf
from numpy import array, zeros, full, argmin, inf, ndim
import numpy as np
from mido import MidiFile

def _traceback(D):
    i, j = array(D.shape) - 2
    p, q = [i], [j]
    while (i > 0) or (j > 0):
        tb = argmin((D[i, j], D[i, j + 1], D[i + 1, j]))
        if tb == 0:
            i -= 1
            j -= 1
        elif tb == 1:
            i -= 1
        else:  # (tb == 2):
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    return array(p), array(q)

def dtw(x, y, dist, warp=1, w=inf, s=1.0):
    """
    Computes Dynamic Time Warping (DTW) of two sequences.
    :param func dist: distance used as cost measure
    :param int warp: how many shifts are computed.
    :param int w: window size limiting the maximal distance between indices of matched entries |i,j|.
    :param float s: weight applied on off-diagonal moves of the path. As s gets larger, the warping path is increasingly biased towards the diagonal
    Returns the minimum distance
    """
    assert len(x)
    assert len(y)
    assert isinf(w) or (w >= abs(len(x) - len(y)))
    assert s > 0
    r, c = len(x), len(y)
    if not isinf(w):
        D0 = full((r + 1, c + 1), inf)
        for i in range(1, r + 1):
            D0[i, max(1, i - w):min(c + 1, i + w + 1)] = 0
        D0[0, 0] = 0
    else:
        D0 = zeros((r + 1, c + 1))
        D0[0, 1:] = inf
        D0[1:, 0] = inf
    D1 = D0[1:, 1:]  # view
    for i in range(r):
        for j in range(c):
            if (isinf(w) or (max(0, i - w) <= j <= min(c, i + w))):
                D1[i, j] = dist(x[i], y[j], len(x))
    jrange = range(c)
    for i in range(r):
        if not isinf(w):
            jrange = range(max(0, i - w), min(c, i + w + 1))
        for j in jrange:
            min_list = [D0[i, j]]
            for k in range(1, warp + 1):
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] * s, D0[i, j_k] * s]
            D1[i, j] += min(min_list)
    return D1[-1, -1]

def dtwLists(x, y, dist, warp=1, w=inf, s=1.0):
    """
    Computes Dynamic Time Warping (DTW) of two sequences.
    :param func dist: distance used as cost measure
    :param int warp: how many shifts are computed.
    :param int w: window size limiting the maximal distance between indices of matched entries |i,j|.
    :param float s: weight applied on off-diagonal moves of the path. As s gets larger, the warping path is increasingly biased towards the diagonal
    Returns the minimum distance
    """
    assert len(x)
    assert len(y)
    assert isinf(w) or (w >= abs(len(x) - len(y)))
    assert s > 0
    r, c = len(x), len(y)
    if not isinf(w):
        D0 = full((r + 1, c + 1), inf)
        for i in range(1, r + 1):
            D0[i, max(1, i - w):min(c + 1, i + w + 1)] = 0
        D0[0, 0] = 0
    else:
        D0 = zeros((r + 1, c + 1))
        D0[0, 1:] = inf
        D0[1:, 0] = inf
    D1 = D0[1:, 1:]  # view
    for i in range(r):
        for j in range(c):
            if (isinf(w) or (max(0, i - w) <= j <= min(c, i + w))):
                custom_distance = lambda x, y: 0 if x==y else 1
#                D1[i, j] = dist(x[i], y[j], dist=custom_distance)
                D1[i, j] = dist(x[i], y[j], dist=chord_distnce)
    ###C-test
    C = D1.copy()
    jrange = range(c)
    for i in range(r):
        if not isinf(w):
            jrange = range(max(0, i - w), min(c, i + w + 1))
        for j in jrange:
            min_list = [D0[i, j]]
            for k in range(1, warp + 1):
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] * s, D0[i, j_k] * s]
            D1[i, j] += min(min_list)
#    return D1[-1, -1]
    if len(x) == 1:
        path = zeros(len(y)), range(len(y))
    elif len(y) == 1:
        path = range(len(x)), zeros(len(x))
    else:
        path = _traceback(D0)
    return D1[-1, -1], C, D1, path

def midiToArray(mid):
    for i, track in enumerate(mid.tracks):
        notesArray = []
        print('Track {}: {}'.format(i, track.name))
        notesPressed = []
        notesReleased = []
        for msg in track:
#            print(msg)
            if (msg.type == "note_on"):
                notesPressed.append(msg.note)
            if (msg.type == "note_off"):
                notesReleased.append(msg.note)
                if (len(notesPressed) == len(notesReleased)):
                    notesArray.append(notesPressed)
                    notesPressed = []
                    notesReleased = []
        print(notesArray)
        return notesArray

custom_distance = lambda x, y: 0 if x==y else 1
def chord_distnce(x, y, len_chord):
    if x==y:
        return 0
    else:
        return (1 / len_chord)

#mid1 = MidiFile("RetentionPhraseA.mid")
#mid2 = MidiFile("subject1Session1Try1.mid.mid")
#d, cost_matrix, acc_cost_matrix, path = dtwLists([[1],[2],[3],[4,1,2]], [[1],[4],[3],[1,2]], dist=dtw)
#print(d)
#print(cost_matrix)
#print(acc_cost_matrix)
#print(path)
song = [[
74,
76,
77,
76,
74,
76,
79,
72,
76,
72
]]
play = [[
76,
74,
76,
77,
76,
74,
72,
79,
72
]]
#d = dtw(song,play,dist=custom_distance)
#print(d)
#
test = dtwLists(song, play, dist=dtw)
print(test)
