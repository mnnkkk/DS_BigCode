import json


def transdifficulty(s):
    if s == "简单":
        return 1
    elif s == "中等":
        return 2
    else:
        return 3


res = {}

f = open("../../resource/leetcodeWebPage.txt", "r", encoding="utf-8")
for i in range(1321):
    # 题目编号
    line = f.readline()
    qId = int(line)
    subRes = {"qId": qId}

    # 题名
    line = f.readline().strip("\n")
    subRes["name"] = line

    # 题解数 通过率 难度
    line = f.readline().strip("\n")
    l = line.split(",")
    passRate = float(l[1][0:4]) / 100
    subRes["leetcodePassRate"] = passRate
    subRes["difficulty"] = transdifficulty(l[2])

    res[qId] = subRes

# 写json
with open("../../out/demoOutPut/leetcodeDifficulty.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
