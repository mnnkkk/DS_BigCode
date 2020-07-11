'''
格式化个人总分、总均分、尝试过的题目数
'''

import json

# 读json
json_data = open('../../../out/analysisOutPut/personal/personal_score.json', encoding='utf-8').read()
personal_score = json.loads(json_data)

res = []
for k, v in personal_score.items():
    subRes = {
        "continent": "g5",
        "Uid": k,
        "overall_average_score": v["overall_average_score"],  # 总平均分
        "overall_sum_score": v["overall_sum_score"],  # 总分
        "tried_num": len(v["cases"])  # 尝试过的题目数
    }
    res.append(subRes)

# 写json
with open('data.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
