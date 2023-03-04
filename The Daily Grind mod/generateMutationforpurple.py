import json,os
mutations = []
string = ""
stringList = ""
mutationList = {}
for file in os.listdir("../../../current/data/json/mutations"):
    with open("../../../current/data/json/mutations/"+file) as f:
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
    string += "	{\"type\": \"effect_on_condition\",\n\
    \"id\": \"EOC_purple_orb_mut_"+mut+"\",\n\
	\"condition\":{\"not\":{\"u_has_trait\":\""+mut+"\"}},\n\
	\"effect\":[\n\
    {\"u_message\":\"Shell Upgrade - "+mutationList[mut]+"\"},\n\
    {\"u_add_trait\":\""+mut+"\"}\n\
	],\n\
	\"false_effect\":[{\"run_eocs\":[\"EOC_purple_orb\"]}]},\n\n"
    stringList += "[ \"EOC_purple_orb_mut_"+mut+"\", {\"const\":45} ],\n"
print(string)