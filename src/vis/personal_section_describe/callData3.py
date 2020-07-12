import json

# 读json
json_data = open('../../../out/analysisOutPut/personal/personal_score.json', encoding='utf-8').read()
personal_score = json.loads(json_data)

key = "8160"
section_name_list = ["图结构", "查找算法", "树结构", "数组", "排序算法", "数字操作", "线性表"]
res = []

for section_name in section_name_list:
    sub_res = {
        "name": section_name,
        "brand": section_name,
        "value": 0,
        "children": []
    }
    res.append(sub_res)

for case in personal_score[key]["cases"]:
    child = {
        "name": case["problem_name"],
        "value": case["score"]
    }
    for section in res:
        if section["name"] == case["case_type"]:
            section["value"] += child["value"]
            section["children"].append(child)

# 写json
with open('data3.json', "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
