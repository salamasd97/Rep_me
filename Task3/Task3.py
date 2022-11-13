import json
import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]


with open(file_name1) as f:
    templates = json.load(f)

with open(file_name2) as f:
    templates_2 = json.load(f)


newDictJson = {}

for dictValue in templates_2["values"]:
    newDictJson[dictValue["id"]] = dictValue["value"]

def print_nested(d):
    if isinstance(d, dict):
        for k, v in d.items():
            print_nested(v)
    elif hasattr(d, '__iter__') and not isinstance(d, str):
        for item in d:
            print_nested(item)
            if "value" in item:
                item["value"] = newDictJson[item["id"]]

print_nested(templates)

with open('report.json', 'w') as f:
    f.write(json.dumps(templates,indent=4))

print(templates)










