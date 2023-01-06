from Tools.collector import InnerNodesCollector
from Tools.collector import BooleanOperatorCollector

# Load json data
import json

def Rule1Detector(filename):
    InnerNodesCollector.InnerNodesCollectorHelper(
        "IfStmt", 
        "kind", 
        "temp/functionNodes.json", 
        "temp/ifNodes.json"
    )
    BooleanOperatorCollector.BooleanOperatorCollectorHelper(
        "BinaryOperator", 
        "kind", 
        "temp/ifNodes.json", 
        "temp/booleanOperatorNodes.json"
    )
    
    f = open("temp/booleanOperatorNodes.json")
    jsonData = json.load(f)
    
    for ele in jsonData:
        if (ele["opcode"] == "=="):
            if getLValueType(ele["inner"]):
                printer(ele, filename)


def getLValueType(json):
    for ele in json:
        if ele["valueCategory"] == "lvalue" and ele["type"]["qualType"] == "bool":
                return True
        if "inner" in ele.keys():
            if ele.get("inner") != None:
                return getLValueType(ele["inner"]) 
    return False


def printer(json, filename):
    print("{filename}:{row}:{col}: RRE001: No need to check if Boolean variable or expression is equal to true or false (Simplify Boolean Expression)".format(filename = filename, row = json["range"]["begin"]["line"], col = json["range"]["begin"]["col"]))