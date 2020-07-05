import os
import shutil

path = '../../resource/cases_of_group5/unpacked'
newPath = '../../resource/cases_of_group5/codes'
dir_names = os.listdir(path)

for dir_name in dir_names:
    print(dir_name)
    os.rename(path+"/"+dir_name+"/main.py", newPath+"/"+dir_name+".py")