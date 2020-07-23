'''
分析每道题得分的样本数，平均数、方差、标准差、中位数、偏度、峰度
'''

import json
import numpy as np
import scipy.stats as st

# 读json
json_data = open("../../../out/analysisOutPut/personal/personal_score.json", encoding="utf-8").read()
personal_score = json.loads(json_data)

json_data = open("../../../resource/test_data1_group5_problem_list.json", encoding="utf-8").read()
res = json.loads(json_data)

score_list_map = {}
for k, v in res.items():
    score_list_map[k] = []

for k, v in personal_score.items():
    for case in v["cases"]:
        score_list_map[case["problem_name"]].append(case["score"])

for k, v in score_list_map.items():
    res[k]["score_num"] = len(v)
    res[k]["score_mean"] = int(100 * np.mean(v)) / 100
    res[k]["score_var"] = int(100 * np.var(v)) / 100
    res[k]["score_std"] = int(100 * np.std(v)) / 100
    res[k]["score_1/4_quantile"] = int(100 * np.quantile(v, 0.25)) / 100
    res[k]["score_1/2_quantile"] = int(100 * np.quantile(v, 0.5)) / 100
    res[k]["score_3/4_quantile"] = int(100 * np.quantile(v, 0.75)) / 100
    res[k]["score_skew"] = int(100 * st.skew(v)) / 100
    res[k]["score_kurtosis"] = int(100 * st.kurtosis(v)) / 100


# 写json
with open("../../../out/analysisOutPut/allMember/single_problem_describe.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
