import os
import json
import urllib.parse
import urllib.request

# 读json
json_data = open('../../resource/testSample1.json', encoding='utf-8').read()
data = json.loads(json_data)


# 遍历data
keyVector = []
for k, v in data.items():
    keyVector.append(k)
# print(keyVector)


# 获得url并下载
for Uid in keyVector:
    for x in data[Uid]["cases"]:
        for y in x["upload_records"]:
            print(y['upload_id'])
            #filename = urllib.parse.unquote(os.path.basename(y['upload_id']))
            filename = urllib.parse.unquote('../../resource/cases/pack/'+str(y['upload_id'])+'.zip')
            print(filename)
            print(y['code_url'])
            urllib.request.urlretrieve(y['code_url'], filename)