'''
分析总体的总通过率，总分的特征
'''

import json
import numpy as np
import scipy.stats as st

# 读json
json_data = open("../../../out/analysisOutPut/personal/personal_score.json", encoding="utf-8").read()
personal_score = json.loads(json_data)

res = {}

list_map = {
    "overall_pass_rate_list" : [],
    "easy_pass_rate_list" : [],
    "medium_pass_rate_list" : [],
    "hard_pass_rate_list" : [],
    "overall_score_list" : [],
    "easy_score_list" : [],
    "medium_score_list" : [],
    "hard_score_list" : []
}

for k, v in personal_score.items():
    list_map["overall_pass_rate_list"].append(v["overall_pass_rate"])
    list_map["easy_pass_rate_list"].append(v["easy_pass_rate"])
    list_map["medium_pass_rate_list"].append(v["medium_pass_rate"])
    list_map["hard_pass_rate_list"].append(v["hard_pass_rate"])
    list_map["overall_score_list"].append(v["overall_sum_score"])
    list_map["easy_score_list"].append(v["easy_sum_score"])
    list_map["medium_score_list"].append(v["medium_sum_score"])
    list_map["hard_score_list"].append(v["hard_sum_score"])


for pre in ["overall", "easy", "medium", "hard"]:
    res[pre] = {}
    for cat in ["pass_rate", "score"]:
        v = list_map[pre + "_" + cat + "_list"]
        res[pre][cat + "_mean"] = int(100 * np.mean(v)) / 100
        res[pre][cat + "_rate_var"] = int(100 * np.var(v)) / 100
        res[pre][cat + "_rate_std"] = int(100 * np.std(v)) / 100
        res[pre][cat + "_rate_1/4_quantile"] = int(100 * np.quantile(v, 0.25)) / 100
        res[pre][cat + "_rate_1/2_quantile"] = int(100 * np.quantile(v, 0.5)) / 100
        res[pre][cat + "_rate_3/4_quantile"] = int(100 * np.quantile(v, 0.75)) / 100
        res[pre][cat + "_rate_skew"] = int(100 * st.skew(v)) / 100
        res[pre][cat + "_rate_kurtosis"] = int(100 * st.kurtosis(v)) / 100

res["detail"] = list_map



# 写json
with open("../../../out/analysisOutPut/all_member/entire_describe.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
