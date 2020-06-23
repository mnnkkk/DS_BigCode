'''
排除出非leetcode题目

输入文件 test_data.json

输出文件 test_data1.json
'''

import json

# 读json
json_data = open('../../out/demoOutPut/leetcodeDifficulty.json', encoding='utf-8').read()
leetcode_problem_list = json.loads(json_data)

json_data1 = open('../../resource/test_data.json', encoding='utf-8').read()
test_data = json.loads(json_data1)


# 遍历leetcode_problem_list
problem_list = []
for k, v in leetcode_problem_list.items():
    problem_list.append(v["name"])
    #print(v["name"])


# 排除出非leetcode题目
res = {}
for k, v in test_data.items():
    new_v = {
        "user_id": v["user_id"],
        "problems": [],
        "cases": [],
    }

    for x in v["cases"]:
        problem_name = x["case_zip"]
        index_of_ = len(problem_name) - 1
        while problem_name[index_of_] != '_':
            index_of_ -= 1
        problem_name = problem_name[57 : index_of_]

        if problem_name in problem_list:
            new_v["cases"].append(x)

            if problem_name not in new_v["problems"]:
                new_v["problems"].append(problem_name)

    new_v["problems"].sort()
    res[k] = new_v

# 写json
with open('../../resource/test_data1.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)

