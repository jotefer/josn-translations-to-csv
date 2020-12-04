import os
import json
import pandas as pd

input = './input'
output = './output'
temp = './temp'
collection = {}

for filename in os.listdir(input):
    if filename.endswith('.json'):
      with open(input + '/' + filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
        collection[filename] = data
      continue
    else:
      continue

with open(temp + './temp.json', 'w', encoding='utf8') as outfile:
    json.dump(collection, outfile, ensure_ascii=False)

df1 = pd.read_json(temp + './temp.json')
df1.to_csv(output + '/result.csv', index=True, encoding='utf-8-sig')
