'''
计算全体人员题目通过率

输入文件 testSample1.json

输出文件 passRate.json
'''

import json

# 读json
json_data = open('../../resource/testSample1.json', encoding='utf-8').read()
data = json.loads(json_data)


# 遍历data
keyVector = []
for k, v in data.items():
    keyVector.append(k)
# print(keyVector)


# 清洗data
res = {}
for Uid in keyVector:
    resOfCurrU = {"uId": Uid}
    allAnsNum = 0
    correctAnsNum = 0

    for x in data[Uid]["cases"]:
        for y in x["upload_records"]:
            allAnsNum += 1
            if y["score"] == 100.0:
                correctAnsNum += 1

    resOfCurrU["overallPassRate"] = correctAnsNum / allAnsNum
    res[Uid] = resOfCurrU

# 写json
with open('../../out/demoOutPut/passRate.json', 'w') as f:
    json.dump(res, f)
