# Collect all 'if' nodes
import os
import os.path

# Load json data
import json

nodes = []
idSet = set()

def BooleanOperatorCollectorHelper(nodeType, attribute, sourceFile, targetFile):
    f = open(sourceFile)
    jsonData = json.load(f)
    nodes.clear()
    idSet.clear()
    # for ele in jsonData:
    for i in reversed(range(len(jsonData))):
        lineNum = jsonData[i]["range"]["begin"]["line"]
        BooleanOperatorCollector(jsonData[i]["inner"], nodeType, attribute, lineNum)


    # Store function nodes into a new json file
    # Delete temp files
    if os.path.isfile(targetFile):
        os.system("rm {target}".format(target = targetFile))

    with open("{target}".format(target = targetFile), "w") as jsonFile:
        nodes.sort(key = lambda x:x["range"]["begin"]["line"])
        jsonString = json.dumps(nodes)
        jsonFile.write(jsonString)


def BooleanOperatorCollector(json, nodeType, attribute, lineNum):
    for ele in json:
        if ele[attribute] == nodeType and ele["id"] not in idSet:
            if ele["range"]["begin"].get("line") != None:
                lineNum = ele["range"]["begin"]["line"]
            ele["range"]["begin"].update({"line":lineNum})
            nodes.append(ele)
            idSet.add(ele["id"])
        if "inner" in ele.keys():
            BooleanOperatorCollector(ele["inner"], nodeType, attribute, lineNum) 
