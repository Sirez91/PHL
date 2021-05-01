import sys, getopt
import csv
import os
from helpers.dwt_hard import compareSongs
from helpers.fileChecker import fileExists, existsDirectory, createPath
from helpers.songs import getSongPath

pathPrefix = '/home/marc/Bachelorarbeit/data/'
condition = ''
participants = 0;

try:
    opts, args = getopt.getopt(sys.argv[1:],
                               "hp:",
                               ["participants="])
except getopt.GetoptError:
    print('collectData.py -p <participants>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('collectData.py -p <participants>')
        sys.exit()
    elif opt in ("-p", "--participants"):
        participants = int(arg)
        if(participants<1):
            print("Needs at least 1 participant")
            sys.exit()

def getScore(path):
    # Using readlines()
    file1 = open(path, 'r')
    Lines = file1.readlines()
 
    score = 0;
    # Strips the newline character
    for line in Lines:
        splitted = line.split(" ");
        if(splitted[1] != "driver"):
            score += int(splitted[1]);
    return score;

with open('game_results.csv', 'w', newline='') as file:
        writer = csv.writer(file);
        writer.writerow(["id", "score"]);
        id = 1;
        while(id <= participants):
            print("id: " + str(id));
            writer.writerow([id, getScore(pathPrefix+str(id)+"/gnew/game.txt")]);
            id+=1;



