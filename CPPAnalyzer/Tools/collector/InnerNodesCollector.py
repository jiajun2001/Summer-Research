# Collect all 'if' nodes
import os
import os.path

# Load json data
import json

nodes = []

def InnerNodesCollectorHelper(nodeType, attribute, sourceFile, targetFile):
    f = open(sourceFile)
    jsonData = json.load(f)
    nodes.clear()
    for ele in jsonData:
        InnerNodesCollector(ele["inner"], nodeType, attribute)

    # Store function nodes into a new json file
    # Delete temp files
    if os.path.isfile(targetFile):
        os.system("rm {target}".format(target = targetFile))

    with open("{target}".format(target = targetFile), "w") as jsonFile:
        jsonString = json.dumps(nodes)
        jsonFile.write(jsonString)


def InnerNodesCollector(json, nodeType, attribute):
    # Depth First Search for 'if' nodes
    for ele in json:
        if ele[attribute] == nodeType:
            nodes.append(ele)
        if "inner" in ele.keys():
            InnerNodesCollector(ele["inner"], nodeType, attribute) 
