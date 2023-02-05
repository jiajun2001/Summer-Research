# Documentation for Rule 8 Detector
# We will collect all if statements
# 1) Check if the compound statement of 'if' statements is empty
# 2) If it is not empty, check if there is any self-assignment

# Load json data
import json
from Tools.collector import InnerNodesCollector

def Rule8Detector(filename):
    # Process If Nodes
    f = open("temp/ifNodes.json")
    processStmt(f, filename);

    # Process While Nodes
    InnerNodesCollector.InnerNodesCollectorHelper(
        "WhileStmt", 
        "kind", 
        "temp/functionNodes.json", 
        "temp/whileStatementNodes.json"
    )
    f = open("temp/whileStatementNodes.json")
    processStmt(f, filename);

    # Process For Nodes
    InnerNodesCollector.InnerNodesCollectorHelper(
        "ForStmt", 
        "kind", 
        "temp/functionNodes.json", 
        "temp/forStatementNodes.json"
    )
    f = open("temp/forStatementNodes.json")
    processStmt(f, filename);


def processStmt(f, filename):
    jsonData = json.load(f)

    # Check the compound statements
    for ele in jsonData:
        # Store the line number of if statement in case it only has one empty compound statement
        lineNum = ele["range"]["begin"]["line"]
        # Count the number of compound statements
        numOfCompoundStmt = 0
        for childEle in ele["inner"]:
            if childEle.get("kind") == None:
                continue
            if childEle["kind"] == "CompoundStmt":
                numOfCompoundStmt += 1
        # Check if compound statement is empty
        for childEle in ele["inner"]:
            if childEle.get("kind") == None:
                continue
            if childEle["kind"] == "CompoundStmt":
                if childEle.get("inner") == None:
                    if numOfCompoundStmt == 1:
                        printerForEmptyStatementsA(childEle, filename, lineNum)
                    else:
                        printerForEmptyStatementsB(childEle, filename)

         # Check if there is any self-assignment


def printerForEmptyStatementsA(json, filename, lineNum):
    print("{filename}:{row}:{col}: RRE008A: Detected empty statement".format(filename = filename, row = lineNum, col = json["range"]["begin"]["col"]))


def printerForEmptyStatementsB(json, filename):
    print("{filename}:{row}:{col}: RRE008A: Detected empty statement".format(filename = filename, row = json["range"]["end"]["line"] - 1, col = json["range"]["begin"]["col"]))