import os
import time

DAYS = 7                       # Maximal file age, older == delete
FOLDERS = [
    "/home/mr.wolf/Downloads/",
    "/home/mr.wolf/Pictures/Screenshots/",
]

TOTAL_DELETED_SIZE = 0          # Provided in bytes
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()      # Gets current time in seconds
ageTime = nowTime - 60*60*DAYS


def delete_old_files(folder):
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for folder_path, dirs, files in os.walk(folder):  # Changed loop variable name
        for file in files:
            fileName = os.path.join(folder_path, file)  # Changed variable name
            fileTime = os.path.getmtime(fileName)
            if fileTime  < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile           # Total Free Space added
                TOTAL_DELETED_FILE += 1                  # Deleted files count
                print(f"Deleting file: {str(fileName)}")
                os.remove(fileName)                      # Delete file


def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for folder_path, dirs, files in os.walk(folder):  # Changed loop variable name
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print(f"Deleting EMPTY Dir: {str(folder_path)}")  # Changed variable name
            os.rmdir(folder_path)  # Changed variable name
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)

#==============MAIN===================
start_time = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)

finish_time = time.asctime()

print("----------------------------------------------")
print(f"START TIME                  {str(start_time)}")
print(f"Total Deleted Size in MB    {str(TOTAL_DELETED_SIZE/1024/1024)}")  # Converted to MB
print(f"Total Deleted Files         {str(TOTAL_DELETED_FILE)}")
print(f"Total Deleted Dirs          {str(TOTAL_DELETED_DIRS)}")
print(f"FINISH TIME                 {str(finish_time)}")
print("-------------EOF------------------------------")
