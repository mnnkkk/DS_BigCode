'''
获得个人能力详情
'''

import json

# 读json
json_data = open("../../../out/analysisOutPut/personal/personal_detail.json", encoding="utf-8").read()
personal_details = json.loads(json_data)

json_data = open("../../../resource/test_data1_group5_problem_list.json", encoding="utf-8").read()
problem_list = json.loads(json_data)

json_data = open("../../../out/analysisOutPut/personal/personal_score.json", encoding="utf-8").read()
score_list = json.loads(json_data)


# 遍历data
keyVector = []
for k, v in personal_details.items():
    keyVector.append(k)

# 整理信息
res = {}
for Uid in keyVector:
    resOfCurrU = {
        "uId": Uid,
        "图结构_pass_rate": 0,
        # "字符串_pass_rate": 0,
        "查找算法_pass_rate": 0,
        "树结构_pass_rate": 0,
        "数组_pass_rate": 0,
        "排序算法_pass_rate": 0,
        "数字操作_pass_rate": 0,
        "线性表_pass_rate": 0,
        "图结构_sum_score": 0,
        # "字符串_sum_score": 0,
        "查找算法_sum_score": 0,
        "树结构_sum_score": 0,
        "数组_sum_score": 0,
        "排序算法_sum_score": 0,
        "数字操作_sum_score": 0,
        "线性表_sum_score": 0,
        "图结构_average_score": 0,
        # "字符串_average_score": 0,
        "查找算法_average_score": 0,
        "树结构_average_score": 0,
        "数组_average_score": 0,
        "排序算法_average_score": 0,
        "数字操作_average_score": 0,
        "线性表_average_score": 0
    }
    up_ct = {}
    case_ct = {}
    pass_ct = {}
    sum_score = {}
    for x in ["图结构", "查找算法", "树结构", "数组", "排序算法", "数字操作", "线性表"]:
        up_ct[x] = 0
        case_ct[x] = 0
        pass_ct[x] = 0
        sum_score[x] = 0

    for case in personal_details[Uid]["cases"]:
        case_type = case["case_type"]
        up_times = case["upload_time"]
        final_score = case["final_score"]

        up_ct[case_type] += up_times
        case_ct[case_type] += 1
        if final_score == 100:
            pass_ct[case_type] += 1

    for case in score_list[Uid]["cases"]:
        case_type = case["case_type"]
        sum_score[case_type] += case["score"]

    for x in ["图结构", "查找算法","树结构","数组","排序算法","数字操作","线性表"]:
        resOfCurrU[x+"_sum_score"] = sum_score[x]
        resOfCurrU[x + "_average_score"] = int(100* sum_score[x] / max(1, case_ct[x])) / 100
        resOfCurrU[x + "_pass_rate"] = int(100* pass_ct[x] / max(1, up_ct[x])) / 100

    res[Uid] = resOfCurrU

# 写json
with open("../../../out/analysisOutPut/personal/personal_section_describe.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)