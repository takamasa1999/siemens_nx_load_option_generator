import os
import time
import sys
import json
from my_tool import my_reader

def sub_dirs_merge(sub_dirs):
    str = ""
    for dir in sub_dirs:
        dir = dir[0]
        dir = dir.replace("\\", "\\" + "\\")
        dir = '"' + dir + '"'
        str += " " + dir
    return str

print("Start: Loading programs. Please wait me a second...")

# directory part
current_dir = os.getcwd() #for pyinstaller. determine current directory from exe
setting_file_dir = current_dir + "/setting.def"
sub_dirs = os.walk(current_dir)
sub_dirs = sub_dirs_merge(sub_dirs)

#judge setting file existence and determine go through or not
if os.path.exists(setting_file_dir) == True:
    pass
else:
    print("Error...: setting.def was not found")
    while True:
           key = input("*press some keys for quit this programm")
           if not key:
               sys.exit()

setting = my_reader.LoadSetting(file_dir = setting_file_dir).load_as_text()

output_text = "LoadOptions_SearchPaths:" + sub_dirs + "\n" + setting

with open(current_dir + '\load_options.def', 'w') as f:
    f.write(output_text)
    f.close()

print("Success!: You can find load_options.def in same directory of this exe.")

while True:
       key = input("*press some keys for quit this programm")
       if not key:
           break