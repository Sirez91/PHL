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
                               "hc:p:",
                               ["condition=","participants="])
except getopt.GetoptError:
    print('collectData.py -c <condition> -p <participants>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('collectData.py -c <condition> -p <participants>')
        sys.exit()
    elif opt in ("-c", "--condition"):
        condition = arg
        if(condition != "pretest" and condition != "test" and condition != "posttest"):
            print("The condition " + condition + " is unknown")
            sys.exit()
    elif opt in ("-p", "--participants"):
        participants = int(arg)
        if(participants<1):
            print("Needs at least 1 participant")
            sys.exit()


def getErrors(recorded, id):
    originalSong = getSongPath(id, "gnew");
    return compareSongs(originalSong, recorded);
    
def getLowestErrors(folder, id):
    errors = 99;
    for filename in os.listdir(folder):
        fileErrors = getErrors(folder + "/" +filename, id);
        if(fileErrors < errors):
            errors = fileErrors;
    return errors;
    
def getLowestErrorsPostTest(folder, id):
    aidedErrors = 99;
    unaidedErrors = 99;
    counter=1;
    for filename in sorted(os.listdir(folder)):
        fileErrors = getErrors(folder + "/" +filename, id);
        print(filename + ' ' + str(fileErrors));
        if(counter > 3):
            if(fileErrors < aidedErrors):
                aidedErrors = fileErrors;
        else:
            if(fileErrors < unaidedErrors):
                unaidedErrors = fileErrors;
        counter+=1;
    if aidedErrors == 99:
        aidedErrors = unaidedErrors;
    return unaidedErrors, aidedErrors;

with open('results_' + condition + '.csv', 'w', newline='') as file:
    if(condition == "posttest"):
        writer = csv.writer(file);
        writer.writerow(["id", "errorsUnaided","errorsAided"]);
        id = 1;
        while(id <= participants):
            print("id: " + str(id));
            unaided, aided = getLowestErrorsPostTest(pathPrefix+str(id)+"/gnew/"+condition,id);
            writer.writerow([id, unaided, aided]);
            id+=1;
    else:
        writer = csv.writer(file);
        writer.writerow(["id", "errors"]);
        id = 1;
        while(id <= participants):
            print("id: " + str(id));
            writer.writerow([id, getLowestErrors(pathPrefix+str(id)+"/gnew/"+condition,id)]);
            id+=1;



