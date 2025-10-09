import json,os
proficiency = []
string = ""
stringList = ""
mutations = []
mutationList = {}
proficiencyList = {}
for file in os.listdir("../../../game0/data/json/mutations"):
    with open("../../../game0/data/json/mutations/"+file) as f:
        content = f.read()
        jsonContent = json.loads(content)
        for mut in jsonContent:
            if mut["type"] == "mutation":
                try:
                    mutationList[mut["id"]] = mut["name"]["str"]
                except TypeError as e:
                    pass
with open("../mutations.json") as f:
    content = f.read()
    jsonContent = json.loads(content)
    for mut in jsonContent:
        mutations.append(mut)
for mut in mutations:
    if mut not in mutationList:
        raise ValueError(mut+" non existant")
	
