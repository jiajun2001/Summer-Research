# Collect all 'if' nodes
import os

# Load json data
import json

ifNodes = []

def IfCollectorHelper():
    f = open("temp/functionNodes.json")
    jsonData = json.load(f)

    for ele in jsonData:
        IfCollector(ele["inner"])

    # Store function nodes into a new json file
    # Delete temp files
    os.system("rm temp/ifNodes.json")
    with open("temp/ifNodes.json", "w") as jsonFile:
        jsonString = json.dumps(ifNodes)
        jsonFile.write(jsonString)


def IfCollector(json):
    # Depth First Search for 'if' nodes
    for ele in json:
        if ele["kind"] == "IfStmt":
            ifNodes.append(ele)
        if "inner" in ele.keys():
            IfCollector(ele["inner"]) 
