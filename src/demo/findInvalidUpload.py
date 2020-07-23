'''
面向用例："条件判断+print"结构数量>=5
'''
import json
import os
import re
from collections import Counter

path = '../../resource/cases_of_group5/codes'
dir_names = os.listdir(path)

res = []

for dir_name in dir_names:
    with open(path + "/" + dir_name, encoding="utf-8") as f:
        contents = f.read()
    # print(contents)
    words = contents.split()
    print_ct = 0
    is_last_if = False
    for x in words:
        if x.startswith("print") and is_last_if:
            print_ct += 1
        if x.__contains__(":"):
            is_last_if = True
        else:
            is_last_if = False
    if print_ct >=5:
        res.append(dir_name)

# 写json
with open('../../out/demoOutPut/invalidUpload.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)