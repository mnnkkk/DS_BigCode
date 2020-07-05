'''
获得个人能力详情
'''

import json

# 读json
json_data = open("../../../resource/test_data1_group5.json", encoding="utf-8").read()
raw_info = json.loads(json_data)

json_data = open("../../../out/demoOutPut/sonarRes_group5.json", encoding="utf-8").read()
sonar_res = json.loads(json_data)

json_data = open("../../../out/demoOutPut/lizardRes_group5.json", encoding="utf-8").read()
lizard_res = json.loads(json_data)

json_data = open("../../../out/demoOutPut/time_cost_of_test1_group5.json", encoding="utf-8").read()
timecost_list = json.loads(json_data)


# 遍历data
keyVector = []
for k, v in raw_info.items():
    keyVector.append(k)

# 整理信息
res = {}
for Uid in keyVector:
    resOfCurrU = {
        "uId": Uid,
        "problem_solved_num": 0,
        "cases": []
    }

    for case in raw_info[Uid]["cases"]:
        if case["final_score"] == 100:
            resOfCurrU["problem_solved_num"] += 1
        problem_name = case["case_zip"]
        index_of_ = len(problem_name) - 1
        while problem_name[index_of_] != '_':
            index_of_ -= 1
        problem_name = problem_name[57: index_of_]
        curr_case = {
            "case_id": case["case_id"],
            "problem_name": problem_name,
            "case_type": case["case_type"],
            "final_score": case["final_score"],
            "upload_time": 0,
            "CNN": 0,
            "sonar_issue_num": 0,
            "is_python": 1,
            "uploads": []
        }

        for record in case["upload_records"]:
            curr_case["upload_time"] += 1
            # print(record["code_url"])
            url_len = len(record["code_url"])
            up_time = int(record["code_url"][url_len-17:url_len-4])
            # curr_case["CNN"] = lizard_res[str(up_time)]

            record_CNN = 10.0
            record_sonar_issue_num = 0

            for i in range(200):
                if str(up_time-i) in sonar_res:
                    record_sonar_issue_num = sonar_res[str(up_time-i)]
                    break
            for i in range(200):
                if str(up_time-i) in lizard_res:
                    record_CNN = lizard_res[str(up_time-i)]["AvgCCN"]
                    curr_case["is_python"] = lizard_res[str(up_time - i)]["isLizard"]
                    break

            sub_upload = {
                "upload_time": record["upload_time"],
                "score": record["score"],
                "CNN": record_CNN,
                "sonar_issue_num": record_sonar_issue_num
            }
            curr_case["uploads"].append(sub_upload)
            curr_case["CNN"] = record_CNN
            curr_case["sonar_issue_num"] += record_sonar_issue_num


        resOfCurrU["cases"].append(curr_case)

    res[Uid] = resOfCurrU

# 写json
with open("../../../out/analysisOutPut/personal/personal_detail.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)