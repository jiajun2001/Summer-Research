# %%
# This is our Pylint Filter File

# %%
# Generate the pylint configuration file
# ------------------------Guide---------------------------
# 1. Go to the directory storing all of the python files to be evaluated using Pylint
# 2. Run the command "Pylint --generate-rcfile > .pylintrc". A pylint configuration file named ".pylintrc" should have been generated

# %%
print("----------------------------------README----------------------------------")
print("Format: python PylintFilter.py -disable=G1,G2,G3,S3 File.py")
print("-G1,G2,G3: These are the error message groups that we want to be disabled")
print("Please note that the group names should be declared incrementally. This means that we should start with G0, and the next group should be called G1. The next group after G1 should be called G2, so on and so forth.")
print("-S3: This is the severity level that we can choose to define. Eg: If we pass in S3, error messages that are in the groups that we declared with severity level below 3 (1, 2) will be disabled")
print("Please note that it is optional to provide a severity level. If none is provided, all error messages in the groups we declared will be disabled.")
print("Please note that only ONE severity level should be provided")
print("Press Enter to continue...")
input()
# %%
# Construct the contents groups that specified in the PylintFilter.txt file
pylintGroupsSpecification = open("PylintFilter.txt")
lines = []
while True:
    line = pylintGroupsSpecification.readline()
    lines.append(line)
    if ("" == line):
        print("File Finished Processing!")
        break
pylintGroupsSpecification.close()
lines[len(lines) - 1] = "--"

# Further Processing
groups = []
group = []
for line in lines:
    if line[0:2] == "--":
        groups.append(group)
        group = []
    group.append(line)
groups.pop(0)

# Get the result
groupErrorArray = []
for singleGroup in groups:
    groupName = singleGroup[0][2:].strip()
    singleGroup.pop(0)
    
    curGroupErrorArray = []
    for singleGroupError in singleGroup:
        curLine = singleGroupError.split(" ")
        errorName = curLine[0]
        severity = int(curLine[1].strip())
        curDictionary = dict({errorName: severity})
        curGroupErrorArray.append(curDictionary)    
    groupErrorArray.append(dict({groupName: curGroupErrorArray}))

# %%
import sys

# %%
# Read in command line arguments and construct the filters
myFilter = set()

def checkArguments(argv):
    if argv[0] == 'S': return True
    if argv[0] != 'G': 
        print("Invalid Argument: " + argv + ". Please make sure group names start with 'G'")
        return False
    if not argv[1:].isdigit(): 
        print("Invalid Argument: " + argv + ". Please make sure group numbers are valid")
        return False
    if argv[1] == '0' and len(argv) != 2:
        print("Invalid Argument: " + argv + ". Please make sure group numbers do not contain any trailing zeroes")
    return True

# Define serverity
if sys.argv[1][-2] == 'S':
    serverityCode = int(sys.argv[1][-1])
else:
    serverityCode = 10
    
# Check the argument format
if sys.argv[1][0:10] != "--disable=":
    print("Invalid argument: " + sys.argv[1] + ". " + "Correct argument format should be '--disable=G1,G2,G3...S3'")
else:
    errorMessageGroups = sys.argv[1][10:]
    errorMessageGroups = errorMessageGroups.split(",")
    
    for errorMessage in errorMessageGroups:
        
        if not checkArguments(errorMessage):
            sys.exit()
        else: 
            if errorMessage[0] != 'S':
                for severityDict in groupErrorArray[int(errorMessage[1:])][errorMessage]:
                    for key, val in severityDict.items():
                        if val < serverityCode:
                            myFilter.add(key)
print("Error Messages to be disabled: ")
print(myFilter)

# %%
# # Find the location to modify
with open(".pylintrc", "r") as configFile:
    contents = configFile.readlines()
 
word = "disable"

for line in contents:
    if line[0] != '#' and line[0 : len(word)] == word:
        disableLine = contents.index(line)
    
configFile.close()

# %%
# # Get the default filter
defaultFilter = []
while contents[disableLine].strip() :
    defaultFilter.append(contents[disableLine].strip(','))
    contents[disableLine] = ""
    disableLine += 1
    if contents[disableLine].startswith("#"):
        break
defaultFilter[len(defaultFilter) - 1] = defaultFilter[len(defaultFilter) - 1].strip('\n')
defaultFilter[len(defaultFilter) - 1] += ",\n"
defaultFilter[len(defaultFilter) - 1] = defaultFilter[len(defaultFilter) - 1].strip('\n')
defaultFilter[len(defaultFilter) - 1] = defaultFilter[len(defaultFilter) - 1].strip(',')

# %%
# # Adding new error codes to disable
newFilter = list(defaultFilter)

# Add a comma to the current last error message
newFilter[len(newFilter) - 1] = newFilter[len(newFilter) - 1].strip('\n')
newFilter[len(newFilter) - 1] += ",\n"
newFilter.append("#Default Filters Above")
newFilter.append('\n')

# Add user defined filters
for oneFilter in myFilter:
    newFilter.append("        " + oneFilter + ",\n")
    
# Remove the last comma
newFilter[len(newFilter) - 1] = newFilter[len(newFilter) - 1].strip('\n').strip(',')
newFilter[len(newFilter) - 1] += "\n"
newFilter

# %%
configFile = open(".pylintrc", "w") 

with open(".pylintrc", "w") as configFile:
    contents = "".join(contents)
    configFile.write(contents)
    filters = "".join(newFilter)
    configFile.write('\n')
    configFile.write(filters)
    configFile.write('\n')
contents
configFile.close()

# %%
import os
fileName = sys.argv[2]
print(fileName)
command = "Pylint " + fileName
os.system(command)
