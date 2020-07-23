'''
计算全体人员题目通过率

输入文件 testSample1.json

输出文件 passRate.json
'''

import json

# 读json
json_data = open('../../resource/testSample1.json', encoding='utf-8').read()
data = json.loads(json_data)


# 遍历data
key_vector = []
for k, v in data.items():
    key_vector.append(k)
# print(keyVector)


# 清洗data
res = {}
for uid in key_vector:
    res_of_curr_u = {"uId": uid}
    all_ans_num = 0
    correct_ans_num = 0

    for x in data[uid]["cases"]:
        for y in x["upload_records"]:
            all_ans_num += 1
            if y["score"] == 100.0:
                correct_ans_num += 1

    res_of_curr_u["overallPassRate"] = correct_ans_num / all_ans_num
    res[uid] = res_of_curr_u

# 写json
with open('../../out/demoOutPut/passRate.json', 'w') as f:
    json.dump(res, f)
