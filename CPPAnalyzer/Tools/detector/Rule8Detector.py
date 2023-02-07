# Documentation for Rule 8 Detector

# We will collect all if statements
# 1) Check if the compound statement of 'if' statements is empty
# 2) Collect all binary operator nodes, check if there is any self-assignment

# Load json data
import json
from Tools.collector import InnerNodesCollector

def Rule8Detector(filename):
    # Check if the compound statement of 'if' statements is empty
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
    processStmt(f, filename)

    # Check if there is any self-assignment
    InnerNodesCollector.InnerNodesCollectorHelper(
        "BinaryOperator", 
        "kind", 
        "temp/functionNodes.json", 
        "temp/binaryOperatorNodes.json"
    )
    f = open("temp/binaryOperatorNodes.json")
    processBinaryOperator(f, filename)


# Check if the statement is empty or not
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


def processBinaryOperator(f, filename):
    jsonData = json.load(f)
    # Check each binary operator node
    for ele in jsonData:
        # Check if the binary operator is '='
        if ele["opcode"] == "=":
            leftName = ele["inner"][0]["referencedDecl"]["name"]
            # Check if is a self-assignment structure
            if ele["inner"][1]["kind"] == "ImplicitCastExpr":
                rightName = ele["inner"][1]["inner"][0]["referencedDecl"]["name"]
                # Detect self-assignment
                if leftName == rightName:
                    printSelfAssignment(ele, filename, rightName)


def printerForEmptyStatementsA(json, filename, lineNum):
    print("{filename}:{row}:{col}: RRE008A: Detected empty statement".format(filename = filename, row = lineNum, col = json["range"]["begin"]["col"]))


def printerForEmptyStatementsB(json, filename):
    print("{filename}:{row}:{col}: RRE008A: Detected empty statement".format(filename = filename, row = json["range"]["end"]["line"] - 1, col = json["range"]["begin"]["col"]))

def printSelfAssignment(json, filename, variableName):
    print("{filename}:{row}:{col}: RRE008C: Detected self-assignment for the variable '{var}' ".format(filename = filename, row = json["range"]["begin"]["line"], col = json["range"]["begin"]["col"], var = variableName)) 