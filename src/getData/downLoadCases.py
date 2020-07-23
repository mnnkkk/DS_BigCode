'''
下载cases
'''
import json
import urllib.parse
import urllib.request

# 读json
# json_data = open('../../resource/test_sample1.json', encoding='utf-8').read()
json_data = open('../../resource/test_data1_group5.json', encoding='utf-8').read()
data = json.loads(json_data)


# 遍历data
key_vector = []
for k, v in data.items():
    key_vector.append(k)
# print(keyVector)


# 获得url并下载
for uid in key_vector:
    for x in data[uid]["cases"]:
        for y in x["upload_records"]:
            print(y['upload_id'])
            # file_name = urllib.parse.unquote(os.path.basename(y['upload_id']))
            file_name = urllib.parse.unquote('../../resource/cases_of_group5/pack/' + str(y['upload_id']) + '.zip')
            print(file_name)
            print(y['code_url'])
            urllib.request.urlretrieve(y['code_url'], file_name)