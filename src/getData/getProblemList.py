import json


# 根据url获取题目名
def get_problem_name(url: str) -> str:
    problem_name = url
    index_of_ = len(problem_name) - 1
    while problem_name[index_of_] != '_':
        index_of_ -= 1
    problem_name = problem_name[57: index_of_]
    # print(problem_name)
    return problem_name


# 读json
# json_data = open('../../resource/test_data1.json', encoding='utf-8').read()
json_data = open('../../resource/test_data1_group5.json', encoding='utf-8').read()
data = json.loads(json_data)

json_data = open('../../out/demoOutPut/leetcodeDifficulty.json', encoding='utf-8').read()
all_problem_list = json.loads(json_data)

case_type_map = {}

# 遍历data
curr_problem_list = set([])
for k, v in data.items():
    for case in v["cases"]:
        problem_name = get_problem_name(case["case_zip"])
        # print(problem_name)
        curr_problem_list.add(problem_name)
        case_type_map[problem_name] = case["case_type"]

res = {}
ct = 1
for x in curr_problem_list:
    for k, v in all_problem_list.items():
        if v["name"] == x:
            res[x] = v
            res[x]["case_type"] = case_type_map[v["name"]]
            break
    ct += 1

# 写json
# with open("../../resource/test_data1_problem_list.json", "w", encoding="utf-8") as f:
with open("../../resource/test_data1_group5_problem_list.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)