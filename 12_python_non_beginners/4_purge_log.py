#!/bin/python3

import shutil  # Files Coping
import os # GetFileSize, Checka If file exists
import sys # For CLI argument

# 4_purge_log.py mylog.txt 10 5

if (len(sys.argv) < 4 ):
    print("Missing arguments! Use --> script.py 10 5 ")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if(os.path.isfile(file_name) == True):          # Cheks if MAIN file exists.
    logfile_size = os.stat(file_name).st_size   # Get Filesize in Bytes
    logfile_size = logfile_size // 1024         # Save in KBytes

    if(logfile_size >= limit_size):
        if(logs_number > 0):
            for currentFileNum in range(logs_number, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print(f"Copied: {src} to {dst}")
            shutil.copyfile(file_name, file_name + "_1")
            print(f"Copied {file_name} to {file_name} '_1'")
        myfile = open(file_name, 'w')
        myfile.close()