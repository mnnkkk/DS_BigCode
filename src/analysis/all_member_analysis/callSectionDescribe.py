'''
分析每个模块的总通过率，总分的特征
'''

import json
import numpy as np
import scipy.stats as st

# 读json
json_data = open("../../../out/analysisOutPut/personal/personal_score.json", encoding="utf-8").read()
personal_score = json.loads(json_data)

section_name_list = ["图结构", "查找算法", "树结构", "数组", "排序算法", "数字操作", "线性表"]
list_map = {}
for name in section_name_list:
    list_map[name + "_pass_rate_list"] = []
    list_map[name + "_score_list"] = []

for k, v in personal_score.items():
    for case in v["cases"]:
        section_name = case["case_type"]
        list_map[section_name + "_pass_rate_list"].append(case["pass_rate"])
        list_map[section_name + "_score_list"].append(case["score"])

res = {}
for pre in section_name_list:
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
with open("../../../out/analysisOutPut/all_member/sectionDescribe.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
