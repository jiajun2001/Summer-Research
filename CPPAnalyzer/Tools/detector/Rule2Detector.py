from Tools.collector import ConsecutiveReturnCollector

# Load json data
import json

def Rule2Detector(filename):
    ConsecutiveReturnCollector.ConsecutiveReturnCollectorHelper(
        "temp/functionNodes.json", 
        "temp/consecutiveReturnNodes.json"
    )

    f = open("temp/consecutiveReturnNodes.json")
    jsonData = json.load(f)

    for ele in jsonData:
        ifStmt = ele[0]
        lastChildOfIfStmt = ifStmt["inner"][len(ifStmt["inner"]) - 1]

        if lastChildOfIfStmt["kind"] == "ReturnStmt":
            printer(ele[0], filename)
        elif lastChildOfIfStmt["kind"] == "CompoundStmt" and len(lastChildOfIfStmt["inner"]) == 1 and lastChildOfIfStmt["inner"][0]["kind"] == "ReturnStmt":
            printer(ele[0], filename)


def printer(json, filename):
    # print(json)
    print("{filename}:{row}:{col}: RRE002: Explicitly returning true and false after checking boolean with condition (Simplify Boolean Return)".format(filename = filename, row = json["range"]["begin"]["line"], col = json["range"]["begin"]["col"]))
            
