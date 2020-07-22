'''
计算解题时长

输入文件 testSample1.json

输出文件 timeCost.json
'''

import json

# 读json
json_data = open("../../resource/test_data1_group5.json", encoding="utf-8").read()
data = json.loads(json_data)

# 基础时间和罚时（根据题目难度）
# 单位：ms
# 基础时间为15/30/45min
# 罚时为10分钟
json_data = open("../../out/demoOutPut/leetcodeDifficulty.json", encoding="utf-8").read()
problems = json.loads(json_data)
def get_base_time(problem_name: str) ->int:
    index_of_ = len(problem_name) - 1
    while problem_name[index_of_] != '_':
        index_of_ -= 1
    problem_name = problem_name[57: index_of_]
    # print(problem_name)
    diff = 0
    for k, v in problems.items():
        if v["name"] == problem_name:
            diff = v["difficulty"]
            break
    return diff * 15 *60 *1000

timeUnit = 10 * 60 * 1000

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
        baseTime = get_base_time(case["case_zip"])

        lastUpTime = 0

        for upload in case["upload_records"]:
            tryTimes += 1
            currUpTime = case["upload_time"]
            if tryTimes == 0:
                timeCost += baseTime
            else:
                timeCost += min(timeUnit, currUpTime - lastUpTime)
            lastUpTime = currUpTime

        t = {"caseId": case["case_id"], "tryTimes": tryTimes, "timeCost": timeCost}
        resOfCurrU["cases"].append(t)
        res[Uid] = resOfCurrU


# 写json
with open("../../out/demoOutPut/time_cost_of_test1_group5.json", "w") as f:
    json.dump(res, f)
