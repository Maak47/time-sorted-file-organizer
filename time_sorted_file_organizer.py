#! python3

#time_sorted_file_organizer.py - python script for sort the files in the folder by modified time
                                # and changes the names to a prefix followed by a number.

import os, sys, re, shutil
from pathlib import Path

usage = 'Usage: python3 time_sorted_file_organizer.py <path> <prefix> <extension>'

def sorterOrganizer(directory, prefix, suffix, reverse=None):
    #check whether the directory is present.
    if not os.path.exists(directory):
        print(f'Directory: "{directory}" does not exist.')
        print(usage)
        sys.exit(1)

    #check if the prefix is applicable.
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', prefix):
        print('Invalid prefix. Only letters, numbers and underscores are allowed.')
        print(usage)
        sys.exit(1)
    
    try:
    # use os.listdir to get all the filenames in a folder.
        path = Path(directory)
        files = os.listdir(path)
        # nameRegex = re.compile(r'^(.*?)\.(.*)$', re.IGNORECASE)

        # sort the list according to the modified time using stat().st_mtime.
        timeStamps = []
        for file in files:
            timeStamps.append((Path(directory) / file).stat().st_mtime)
        # print(timeStamps)
        filesDict = { key:value for key, value in zip(files, timeStamps)}

        if reverse:
            reverse = reverse.lower()
            if reverse == 'reverse' or reverse == 'r':
                sortedFiles = dict(reversed(filesDict.items(), key=lambda item: item[1]))
        sortedFiles = dict(sorted(filesDict.items(), key=lambda item: item[1]))
        # print(sortedFiles)

    # rename files to have an assigned prefix and a serial number as suffix.
        serialNum = 1
        for key in sortedFiles:
            if suffix in key:
                shutil.move(Path(path) / key, Path(path) / f'{prefix}{serialNum}.{suffix}')
                # return the name of the file before and after sorting
                print(f'{key} is changed to: {prefix}{serialNum}.{suffix}')
                serialNum += 1
    except FileNotFoundError as e:
        print(f'File not Found: {e}')
    except Exception as e:
        print(f'An error occured: {e}')

if len(sys.argv) < 4 or len(sys.argv) > 5:
    print(usage)
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        sorterOrganizer(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        sorterOrganizer(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])