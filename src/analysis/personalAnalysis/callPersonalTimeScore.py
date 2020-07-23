'''
获得个人（分数 *时间）详情
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

json_data = open("../../../resource/test_data1_group5_problem_list.json", encoding="utf-8").read()
problem_list = json.loads(json_data)

# 遍历data
key_vector = []
for k, v in raw_info.items():
    key_vector.append(k)


# 获得某个时间点前的描述
def get_detail_before(time_line: int):
    ans = {}
    for uid in key_vector:
        res_of_curr_u = {
            "uId": uid,
            "problem_solved_num": 0,
            "cases": []
        }

        for case in raw_info[uid]["cases"]:
            final_score = 0
            vaild_upload = 0
            for record in case["upload_records"]:
                if record["upload_time"] <= time_line:
                    vaild_upload += 1
                    final_score = max(final_score, record["score"])
            if vaild_upload == 0:
                continue

            if final_score == 100:
                res_of_curr_u["problem_solved_num"] += 1

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
                if record["upload_time"] > time_line:
                    continue
                curr_case["upload_time"] += 1
                # print(record["code_url"])
                url_len = len(record["code_url"])
                up_time = int(record["code_url"][url_len - 17:url_len - 4])
                # curr_case["CNN"] = lizard_res[str(up_time)]

                record_CNN = 10.0
                record_sonar_issue_num = 0

                for i in range(200):
                    if str(up_time - i) in sonar_res:
                        record_sonar_issue_num = sonar_res[str(up_time - i)]
                        break
                for i in range(200):
                    if str(up_time - i) in lizard_res:
                        record_CNN = lizard_res[str(up_time - i)]["AvgCCN"]
                        curr_case["is_python"] = lizard_res[str(up_time - i)]["isLizard"]
                        break

                sub_upload = {
                    "upload_time": record["upload_time"],
                    "time_cost": timecost_list[uid]["cases"][curr_case["upload_time"] - 1]["timeCost"],
                    "score": record["score"],
                    "CNN": record_CNN,
                    "sonar_issue_num": record_sonar_issue_num
                }
                curr_case["uploads"].append(sub_upload)
                curr_case["CNN"] = record_CNN
                curr_case["sonar_issue_num"] += record_sonar_issue_num

            res_of_curr_u["cases"].append(curr_case)

        ans[uid] = res_of_curr_u
    return ans


# 获得分数
def get_scores_before(personal_details):
    ans = {}
    for uid in key_vector:
        res_of_curr_u = {
            "uId": uid,
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

        for case in personal_details[uid]["cases"]:
            problem_name = case["problem_name"]
            difficulty = problem_list[problem_name]["difficulty"]
            score = float(case["final_score"])
            final_score = case["final_score"]
            up_times = case["upload_time"]
            pass_times = 0
            for upload in case["uploads"]:
                if upload["score"] == 100.0:
                    pass_times += 1

            score *= difficulty
            score *= max(1, 16 - case["upload_time"]) / 15
            score *= max(1, 40 - case["sonar_issue_num"]) / 40
            score *= max(1, 20 - case["CNN"]) / 20
            score = int(score)

            res_of_curr_u["overall_sum_score"] += score
            all_ct += 1
            all_up_time += up_times
            if final_score == 100:
                all_pass += 1
            if difficulty == 1:
                res_of_curr_u["easy_sum_score"] += score
                easy_ct += 1
                easy_up_time += up_times
                if final_score == 100:
                    easy_pass += 1
            elif difficulty == 2:
                res_of_curr_u["medium_sum_score"] += score
                medium_ct += 1
                medium_up_time += 1
                if final_score == 100:
                    medium_pass += 1
            else:
                res_of_curr_u["hard_sum_score"] += score
                hard_ct += 1
                hard_up_time += 1
                if final_score == 100:
                    hard_pass += 1
            res_of_curr_u["overall_average_score"] = int(res_of_curr_u["overall_sum_score"] / max(1, all_ct))
            res_of_curr_u["easy_average_score"] = int(res_of_curr_u["easy_sum_score"] / max(1, easy_ct))
            res_of_curr_u["medium_average_score"] = int(res_of_curr_u["medium_sum_score"] / max(1, medium_ct))
            res_of_curr_u["hard_average_score"] = int(res_of_curr_u["hard_sum_score"] / max(1, hard_ct))
            res_of_curr_u["overall_pass_rate"] = int(100 * all_pass / max(1, all_ct)) / 100
            res_of_curr_u["easy_pass_rate"] = int(100 * easy_pass / max(1, easy_ct)) / 100
            res_of_curr_u["medium_pass_rate"] = int(100 * medium_pass / max(1, medium_ct)) / 100
            res_of_curr_u["hard_pass_rate"] = int(100 * hard_pass / max(1, hard_ct)) / 100

        ans[uid] = res_of_curr_u
    return ans


res = {}
ct = 0
time_line = 1581955199999  # 2020-02-17 23:59:59 ms
while time_line <= 1585670399999:  # 2020-03-31 23:59:59
    ct += 1
    personal_details = get_detail_before(time_line)
    res[ct] = get_scores_before(personal_details)
    time_line += 86400000

# 写json
with open("../../../out/analysisOutPut/personal/personal_time_score.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
