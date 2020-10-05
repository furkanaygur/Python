import json

# *****************************************************************

personString = '{"name":"furkan", "languages":["python","C/C++","C#","html","css"]}'

# JSON string to Dict

j = json.loads(personString)
print(j)

result = j["name"]
print(result)

result = j["languages"][0]
print(result)

# ***************************************************

with open("person.json") as f:
    data = json.load(f)
    result = data["name"]
    print(result)

# ****************************************************

person_dict = {
    "name": "furkan",
    "languages": ["Python", "C/C++", "C#", "Html", "Css"]
}

# Dict To Json String

j = json.dumps(person_dict)

# ***** File version

with open("person.json", "w") as file:
    json.dump(person_dict, file)

#*******************************************************************

personString = '{"name":"furkan", "languages":["python","C/C++","C#","html","css"]}'

person_dict = json.loads(personString)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)

