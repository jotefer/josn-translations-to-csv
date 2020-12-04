import os
import json
import pandas as pd

input = './input/data.csv'
output = './output'

csv_file = pd.DataFrame(pd.read_csv(input, sep = ",", index_col = 0, header = 0))
keys = pd.DataFrame(pd.read_csv(input, sep = ",",  usecols = [0]))
json_keys = json.loads(keys.to_json(orient = "split"))

data = csv_file.head()

for col in data.columns:
    csv_column = pd.DataFrame(pd.read_csv(input, sep = ",", usecols = [col]))
    json_csv_column = json.loads(csv_column.to_json(orient = "split"))
    file = {}

    for index in json_keys['index']:
        if(json_csv_column['data'][index][0]):
            file[json_keys['data'][index][0]] = json_csv_column['data'][index][0]

    with open(output + '/' + col, 'w', encoding = 'utf8') as outfile:
        json.dump(file, outfile, ensure_ascii = False)
