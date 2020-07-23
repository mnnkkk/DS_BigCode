'''
计算解题时长

输入文件 test_sample1.json

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

time_unit = 10 * 60 * 1000

# 遍历data
key_vector = []
for k, v in data.items():
    key_vector.append(k)

# 遍历并计算时长
res = {}
for uid in key_vector:
    res_of_curr_u = {"uId": uid, "cases": []}

    for case in data[uid]["cases"]:
        try_times = 0
        time_cost = 0
        base_time = get_base_time(case["case_zip"])

        last_up_time = 0

        for upload in case["upload_records"]:
            try_times += 1
            curr_up_time = case["upload_time"]
            if try_times == 0:
                time_cost += base_time
            else:
                time_cost += min(time_unit, curr_up_time - last_up_time)
            last_up_time = curr_up_time

        t = {"caseId": case["case_id"], "tryTimes": try_times, "timeCost": time_cost}
        res_of_curr_u["cases"].append(t)
        res[uid] = res_of_curr_u


# 写json
with open("../../out/demoOutPut/time_cost_of_test1_group5.json", "w") as f:
    json.dump(res, f)
