import os
import time
import datetime
import json
from dateutil import parser
import operator

def change_working_directory(path):
    os.chdir(path)
    folder = os.getcwd()
    return folder

def replace_and_sort(remove):
    dictio = {}
    for file in os.listdir():
        file_name, file_ex = os.path.splitext(file)
        file_name = file_name.replace(remove, '')
        date = datetime.datetime.fromtimestamp(os.path.getctime(file))
        date = str(date)
        date = parser.parse(date)
        epoch = date.timestamp()
        epoch = int(epoch)
        dictio[epoch] = file_name
        sorted_dict = dict(sorted(dictio.items()))
    count = 1
    sorted_dict_reversed = {v: k for k, v in sorted_dict.items()}
    for name in sorted_dict_reversed:
        new_name = name.replace(name, f"{count}. {name}")
        count=count+1
        for file in os.listdir():
            file_name, file_ex = os.path.splitext(file)
            file_name = file_name.replace(remove, '')
            if name in file_name:
                os.rename(file, f"{new_name}.mp4")
                # print(file, f"\n{new_name}.mp4")
                # print()
    return sorted_dict


folder = change_working_directory(r"E:\Information Technology\Git\ITPro.TV")
dictionary = replace_and_sort('- Intro to Git - Intro to Git')

# print(folder)
# print(json.dumps(dictionary, indent=2))

