'''
解析lizard结果

提交记录参照sonarRes.json
若lizard无该记录的解析结果，做标记

结果解释如下

    the nloc (lines of code without comments),
    CCN (cyclomatic complexity number),
    token count of functions.
    parameter count of functions.

'''

import json
import os

res = {}

path = '../../resource/cases/codes'
dir_names = os.listdir(path)

for dir_name in dir_names:
    up_time = dir_name[6:19]
    res[up_time] = {"isLizard": 0}


# f = open("../../resource/lizard_log.txt", "r", encoding="utf-8")
f = open("../../resource/lizard_log_group5.txt", "r", encoding="utf-8")
# fileLineNum = 21
file_line_num = 4099

for i in range((int)(file_line_num)):
    s = f.readline()
    if not s.startswith(" "):
        continue

    NLOC = int(s[0:7])
    AvgNLOC = float(s[7:17])
    AvgCCN = float(s[17:25])
    AvgToken = float(s[25:36])
    FunctionCnt = int(s[36:46])

    up_time = s[69:82]
    res[up_time] = {
        "isLizard": 1,
        "NLOC": NLOC,
        "AvgNLOC": AvgNLOC,
        "AvgCCN": AvgCCN,
        "AvgToken": AvgToken,
        "FunctionCnt": FunctionCnt
    }

# 写json
# with open("../../out/demoOutPut/lizardRes.json", "w", encoding="utf-8") as f:
with open("../../out/demoOutPut/lizardRes_group5.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
