# Load json data
import json

nodes = []

def ConsecutiveReturnCollectorHelper(sourceFile, targetFile):
    f = open(sourceFile)
    jsonData = json.load(f)
    nodes.clear()
    # for ele in jsonData:
    #     ConsecutiveReturnCollector(ele["inner"])
    ConsecutiveReturnCollector(jsonData[1]["inner"])
    
    with open("{target}".format(target = targetFile), "w") as jsonFile:
        jsonString = json.dumps(nodes)
        jsonFile.write(jsonString)


def ConsecutiveReturnCollector(json):
    for ele in json:
        if "inner" in ele:
            curNode = ele["inner"]
            for i in range(len(curNode)):
                if i < len(curNode) - 1 and curNode[i]["kind"] == "IfStmt" and curNode[i + 1]["kind"] == "ReturnStmt":
                    nodes.append([curNode[i], curNode[i + 1]])
                ConsecutiveReturnCollector([curNode[i]])