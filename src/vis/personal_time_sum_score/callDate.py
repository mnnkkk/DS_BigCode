import json

# 读json
json_data = open('../../../out/analysisOutPut/personal/personal_time_score.json', encoding='utf-8').read()
personal_time_score = json.loads(json_data)

res = {}
for k, v in personal_time_score.items():
    subRes = []
    for k2, v2 in v.items():
        subRes.append({
            "value": v2["overall_sum_score"],
            "uid": k2
        })
    res[k] = subRes

# 写json
with open('data.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
