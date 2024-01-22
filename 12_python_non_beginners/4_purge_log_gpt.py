#!/bin/python3

import shutil  # File Copying
import os      # File Operations
import sys     # Command-Line Arguments

def rotate_and_truncate_log(file_name, limit_size, logs_number):
    if len(sys.argv) < 4:
        print("Missing arguments! Use --> script.py 10 5 ")
        exit(1)

    if not os.path.isfile(file_name):
        print(f"The main log file '{file_name}' does not exist.")
        exit(1)

    logfile_size = os.stat(file_name).st_size // 1024  # Size in KBytes

    if logfile_size >= limit_size:
        if logs_number > 0:
            for currentFileNum in range(logs_number, 1, -1):
                src = f"{file_name}_{currentFileNum-1}"
                dst = f"{file_name}_{currentFileNum}"
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print(f"Copied: {src} to {dst}")
            
            shutil.copyfile(file_name, f"{file_name}_1")
            print(f"Copied {file_name} to {file_name}_1")

        with open(file_name, 'w') as myfile:
            print(f"Truncated {file_name}.")

if __name__ == "__main__":
    file_name = sys.argv[1]
    limit_size = int(sys.argv[2])
    logs_number = int(sys.argv[3])

    rotate_and_truncate_log(file_name, limit_size, logs_number)
