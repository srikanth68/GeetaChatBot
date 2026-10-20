import json

with open("data/geetachunks.json", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print(data[4])