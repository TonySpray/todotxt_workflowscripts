#! /usr/bin/env python

import os
import shutil


file_1 = '/Path/to/todo/todo.txt'
file_2 = '/Users/youruser/Library/Application Support/Notational Data/todo.txt'
debug = False

def main():
    f1_mod_time = os.path.getmtime(file_1)
    f2_mod_time = os.path.getmtime(file_2)

    if f1_mod_time > f2_mod_time:
        shutil.copy2(file_1, file_2)
        if debug: print("Moved {0} to {1}".format(file_1, file_2))
    elif f2_mod_time > f1_mod_time:
        shutil.copy2(file_2, file_1)
        if debug: print("Moved {0} to {1}".format(file_2, file_1))
    else:
        if debug: print("No file changes, exit")


if __name__ == '__main__':
    main()
