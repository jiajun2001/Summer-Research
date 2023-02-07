# Documentation for Rule 3 Detector

# 

# Load json data
import json

def Rule3Detector(filename):
    f = open("temp/ifNodes.json")
    jsonData = json.load(f)

    for ele in jsonData:
        lastChildOfIfStmt = ele["inner"][len(ele["inner"]) - 1]
        if lastChildOfIfStmt.get("inner") == None:
            continue
        if lastChildOfIfStmt["kind"] == "IfStmt":
            printer(ele, filename)
        elif lastChildOfIfStmt["kind"] == "CompoundStmt" and len(lastChildOfIfStmt["inner"]) == 1 and lastChildOfIfStmt["inner"][0]["kind"] == "IfStmt":
            printer(ele, filename)


def printer(json, filename):
    # print(json)
    print("{filename}:{row}:{col}: RRE003: Avoiding deep nested ifs by using and (&&) operator".format(filename = filename, row = json["range"]["begin"]["line"], col = json["range"]["begin"]["col"]))