import json
import random

# 读json
json_data = open('../../../out/demoOutPut/leetcodeDifficulty.json', encoding='utf-8').read()
difficultys = json.loads(json_data)

d_dic = {
    1: "easy",
    2: "medium",
    3: "hard"
}

pass_rate_ct = {
    "easy": {},
    "medium": {},
    "hard": {}
}

t = 0
while t <= 1.0:
    for d in ["easy", "medium", "hard"]:
        pass_rate_ct[d][str(int(t * 20 + 0.5) / 20)] = 0 # random.randint(0,9)
    t += 0.05

for k, v in difficultys.items():
    t = v["leetcodePassRate"]
    pass_rate_ct[d_dic[v["difficulty"]]][str(int(t * 20 + 0.5) / 20)] += 1



res = []
for d in ["easy", "medium", "hard"]:
    for k, v in pass_rate_ct[d].items():
        res.append({
            "pass_rate": k,
            "difficulty": d,
            "ct": v
        })



# 写json
with open('data.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
