#! python3

#time_sorted_file_organiser.py - python script for sort the files in the folder by modified time
                                # and changes the names to a prefix followed by a number.

import os, sys, re, shutil
from pathlib import Path


def sorterOrganiser(directory, prefix, suffix):
    
#TODO: use os.listdir to get all the filenames in a folder.
    path = Path(directory)
    files = os.listdir(path)
    # nameRegex = re.compile(r'^(.*?)\.(.*)$', re.IGNORECASE)
#TODO: sort the list according to the modified time using stat().st_mtime.
    timeStamps = []
    for file in files:
        timeStamps.append((Path(directory) / file).stat().st_mtime)
    print(timeStamps)
    filesDict = { key:value for key, value in zip(files, timeStamps)}
    sortedFiles = dict(reversed(sorted(filesDict.items(), key=lambda item: item[1])))
    print(sortedFiles)

#TODO: rename files to have an assigned prefix and a serial number as suffix.
    serialNum = 1
    for key in sortedFiles:
        if suffix in key:
            shutil.move(key, f'{prefix}{serialNum}.{suffix}')
            #TODO: return the name of the file before and after sorting
            print(f'{key} is changed to: {prefix}{serialNum}.{suffix}')
            serialNum += 1

sorterOrganiser('/home/maak/spam', 'spam', 'js')