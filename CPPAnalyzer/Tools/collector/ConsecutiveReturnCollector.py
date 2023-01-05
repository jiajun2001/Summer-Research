# Load json data
import json

nodes = []

def ConsecutiveReturnCollectorHelper(sourceFile, targetFile):
    f = open(sourceFile)
    jsonData = json.load(f)
    nodes.clear()
    for ele in jsonData:
        ConsecutiveReturnCollector(ele["inner"])
    
    with open("{target}".format(target = targetFile), "w") as jsonFile:
        jsonString = json.dumps(nodes)
        jsonFile.write(jsonString)


def ConsecutiveReturnCollector(json):
    for ele in json:
        if ele["inner"] != None:
            curNode = ele["inner"]
            for i in range(len(curNode) - 1):
                if curNode[i]["kind"] == "IfStmt" and curNode[i + 1]["kind"] == "ReturnStmt":
                    nodes.append([curNode[i], curNode[i + 1]])
                if "inner" in curNode[i].keys():
                    ConsecutiveReturnCollector(curNode[i]["inner"])