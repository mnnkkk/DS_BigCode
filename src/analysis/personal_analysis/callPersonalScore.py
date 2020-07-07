'''
获得个人能力详情
'''

import json

# 读json
json_data = open("../../../out/analysisOutPut/personal/personal_detail.json", encoding="utf-8").read()
personal_details = json.loads(json_data)

json_data = open("../../../resource/test_data1_group5_problem_list.json", encoding="utf-8").read()
problem_list = json.loads(json_data)


# 遍历data
keyVector = []
for k, v in personal_details.items():
    keyVector.append(k)

# 整理信息
res = {}
for Uid in keyVector:
    resOfCurrU = {
        "uId": Uid,
        "overall_pass_rate": 0,
        "hard_pass_rate": 0,
        "medium_pass_rate": 0,
        "easy_pass_rate": 0,
        "overall_sum_score": 0,
        "hard_sum_score": 0,
        "medium_sum_score": 0,
        "easy_sum_score": 0,
        "overall_average_score": 0,
        "hard_average_score": 0,
        "medium_average_score": 0,
        "easy_average_score": 0,
        "cases": []
    }
    all_ct = 0
    easy_ct = 0
    medium_ct = 0
    hard_ct = 0
    all_up_time = 0
    easy_up_time = 0
    medium_up_time = 0
    hard_up_time = 0
    all_pass = 0
    easy_pass = 0
    medium_pass = 0
    hard_pass = 0

    for case in personal_details[Uid]["cases"]:
        problem_name = case["problem_name"]
        difficulty = problem_list[problem_name]["difficulty"]
        score = float(case["final_score"])
        final_score = case["final_score"]
        up_times = case["upload_time"]
        sub_case = {
            "problem_name": problem_name,
            "difficulty": difficulty
        }

        score *= difficulty
        score *= max(1, 16 - case["upload_time"]) / 15
        score *= max(1, 40 - case["sonar_issue_num"]) / 40
        score *= max(1, 20 - case["CNN"]) / 20
        score = int(score)
        sub_case["score"] = score

        resOfCurrU["overall_sum_score"] += score
        all_ct += 1
        all_up_time += up_times
        if final_score == 100:
            all_pass += 1
        if difficulty == 1:
            resOfCurrU["easy_sum_score"] += score
            easy_ct += 1
            easy_up_time += up_times
            if final_score == 100:
                easy_pass += 1
        elif difficulty == 2:
            resOfCurrU["medium_sum_score"] += score
            medium_ct += 1
            medium_up_time += 1
            if final_score == 100:
                medium_pass += 1
        else:
            resOfCurrU["hard_sum_score"] += score
            hard_ct += 1
            hard_up_time += 1
            if final_score == 100:
                hard_pass += 1
        resOfCurrU["overall_average_score"] = int(resOfCurrU["overall_sum_score"] / max(1, all_ct))
        resOfCurrU["easy_average_score"] = int(resOfCurrU["easy_sum_score"] /  max(1, easy_ct))
        resOfCurrU["medium_average_score"] = int(resOfCurrU["medium_sum_score"] /  max(1, medium_ct))
        resOfCurrU["hard_average_score"] = int(resOfCurrU["hard_sum_score"] /  max(1, hard_ct))
        resOfCurrU["overall_pass_rate"] = int(100* all_pass / max(1, all_ct)) / 100
        resOfCurrU["easy_pass_rate"] = int(100* easy_pass / max(1, easy_ct)) / 100
        resOfCurrU["medium_pass_rate"] = int(100* medium_pass / max(1, medium_ct)) / 100
        resOfCurrU["hard_pass_rate"] = int(100* hard_pass / max(1, hard_ct)) / 100
        resOfCurrU["cases"].append(sub_case)

    res[Uid] = resOfCurrU

# 写json
with open("../../../out/analysisOutPut/personal/personal_score.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)