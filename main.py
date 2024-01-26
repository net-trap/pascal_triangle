thisString = []
lastString = []
finalString = ""
countOfStrings = int(input("Введите кол-во желаемых строк: "))

for string in range(countOfStrings):
    if string == 0:
        for i in range(countOfStrings - (string + 1)):
            thisString.append("0")
        thisString.append("1")
        for i in range(countOfStrings - 1):
            thisString.append("0")
    elif string == 1:
        for i in range(countOfStrings - (string + 1)):
            thisString.append("0")
        thisString.append("1")
        thisString.append("0")
        thisString.append("1")
        for i in range(countOfStrings - (string + 1)):
            thisString.append("0")
    else:
        thisString = ["0"] * len(lastString)
        for el in range(len(lastString)):
            if el in [0, len(lastString)-1]:
                if string + 1 == countOfStrings:
                    thisString[el] = "1"
                else:
                    thisString[el] = "0"
            else:
                thisString[el] = str(int(lastString[el-1]) + int(lastString[el+1]))
    lastString = thisString.copy()
    for i in range(len(thisString)):
        if thisString[i] == '0':
            thisString[i] = ' '
    for i in range(len(thisString)):
        finalString += str(thisString[i])
    print(finalString)
    finalString = ""
    thisString = []
