# Cpp file preprocessing
import os

def HeaderPreprocessor(path):
    # Absolute path of a file
    old_name = path
    new_name = path
    new_name = new_name.replace(new_name[len(new_name) - 3 : ], "txt")

    # Renaming the file
    os.rename(old_name, new_name)
    contents = []
    with open(new_name, "r") as configFile:
        contents = configFile.readlines()   

    # Collect all header file and namespace declaration
    headers = []
    for i in reversed(range(len(contents))):
        statement = contents[i]
        if "#include" in statement or "using namespace" in statement:
            contents.pop(i)
            headers.append(statement)
            
    # Append XX_MARKER_XX into file     
    # headers.append("int XX_MARKER_XX;\n")

    # Append all headers and namespace declaration at the start of the file
    with open(new_name, "w") as configFile:
        headers = "".join(headers)
        configFile.write(headers)         
        contents = "".join(contents)
        configFile.write(contents)         
                
    os.rename(new_name, old_name) 
    configFile.close()