import json
with open('menu.json') as f:
    data = json.loads(f.read())
    print(data)