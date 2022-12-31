# Collect all 'function' nodes
import os
import json

def FunctionCollector(path):
    # Run command to get json file of AST output
    command = "cp {path} temp/copy.cpp".format(path = path)
    os.system(command)
    command = "clang -Xclang -ast-dump=json -fsyntax-only -fno-color-diagnostics temp/copy.cpp > temp/output.json"
    os.system(command)

    # Load json data
    f = open("temp/output.json")
    jsonData = json.load(f)

    # # Get function nodes
    index = len(jsonData["inner"]) - 1
    functionNodes = []
    while True:
        node = jsonData["inner"][index]
        if node["name"] != "XX_MARKER_XX":
            functionNodes.append(node)
            index -= 1
        else:
            break;

    # Store function nodes into a new json file
    with open("temp/functionNodes.json", "w") as jsonFile:
        jsonString = json.dumps(functionNodes)
        jsonFile.write(jsonString)

    # Delete temp files
    os.system("rm temp/output.json")
    os.system("rm temp/copy.cpp")