import json


def getIssueNum(s: str) -> int:
    if s.startswith("File won't"):
        return 10
    end = 7
    while s[end] != ' ':
        end += 1
    return int(s[6:end])


res = {}

f = open("../../resource/sonarLog.txt", "r", encoding="utf-8")
fileLineNum = 102

for i in range((int)(fileLineNum / 3)):
    f.readline()
    # 提交时间标记
    s = f.readline()
    uptime = s[17:30]

    # issue数
    s = f.readline()
    issueNum = getIssueNum(s)
    print(issueNum)

    res[uptime] = issueNum

# 写json
with open("../../out/demoOutPut/sonarRes.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False)
