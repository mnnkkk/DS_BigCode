'''
解析sonar结果
'''
import json


def get_issue_num(s: str) -> int:
    if s.startswith("File won't"):
        return 10
    end = 7
    while s[end] != ' ':
        end += 1
    return int(s[6:end])


res = {}

# f = open("../../resource/sonarLog.txt", "r", encoding="utf-8")
f = open("../../resource/sonarLog_group5.txt", "r", encoding="utf-8")
# file_line_num = 102
file_line_num = 14403

for i in range((int)(file_line_num / 3)):
    f.readline()
    # 提交时间标记
    s = f.readline()
    up_time = s[17:30]

    # issue数
    s = f.readline()
    issue_num = get_issue_num(s)
    print(issue_num)

    res[up_time] = issue_num

# 写json
# with open("../../out/demoOutPut/sonarRes.json", "w", encoding="utf-8") as f:
with open("../../out/demoOutPut/sonarRes_group5.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
