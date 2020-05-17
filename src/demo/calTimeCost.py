import json

# 读json
json_data = open("../../resource/testSample1.json", encoding="utf-8").read()
data = json.loads(json_data)

# 基础时间和罚时（根据题目难度）
# 单位：ms
# 基础时间为15/30/45min
# 罚时为二分之一基础时间
baseTime = 15 * 60 * 1000
timeUnit = baseTime / 2

# 遍历data
keyVector = []
for k, v in data.items():
    keyVector.append(k)

# 遍历并计算时长
res = {}
for Uid in keyVector:
    resOfCurrU = {"uId": Uid, "cases": []}

    for case in data[Uid]["cases"]:
        tryTimes = 0
        timeCost = 0

        for upload in case["upload_records"]:
            tryTimes += 1
            if tryTimes == 0:
                timeCost += baseTime
            else:
                timeCost += timeUnit

        t = {"caseId": case["case_id"], "tryTimes": tryTimes, "timeCost": timeCost}
        resOfCurrU["cases"].append(t)
        res[Uid] = resOfCurrU


# 写json
with open("../../out/demoOutPut/timeCost.json", "w") as f:
    json.dump(res, f)
