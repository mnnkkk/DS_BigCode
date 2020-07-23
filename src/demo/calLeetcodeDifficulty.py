'''
解析leetcode题目难度

输入文件 leetcode_web_page.txt
    格式  6和9组成的最大数字
          204,75.1%,简单
          1324
          ...

输出文件 leetcode_difficulty.json
    格式  "1": {
            "qId": 1,
            "name": "两数之和",
            "leetcodePassRate": 0.484,
            "difficulty": 1
            }, ...
'''

import json


def trans_difficulty(s):
    if s == "简单":
        return 1
    elif s == "中等":
        return 2
    else:
        return 3


res = {}

f = open("../../resource/leetcode_web_page.txt", "r", encoding="utf-8")
for i in range(1321):
    # 题目编号
    line = f.readline()
    qId = int(line)
    sub_res = {"qId": qId}

    # 题名
    line = f.readline().strip("\n")
    sub_res["name"] = line

    # 题解数 通过率 难度
    line = f.readline().strip("\n")
    l = line.split(",")
    pass_rate = float(l[1][0:4]) / 100
    sub_res["leetcodePassRate"] = pass_rate
    sub_res["difficulty"] = trans_difficulty(l[2])

    res[qId] = sub_res

# 写json
with open("../../out/demoOutPut/leetcode_difficulty.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
