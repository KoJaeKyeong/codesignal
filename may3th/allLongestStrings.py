def allLongestStrings(inputArray):
    max_L=''
    ls=[]
    inputArray.sort(key=len,reverse=True)
    for i in range(len(inputArray)):
        if len(inputArray[i])>=len(max_L):
            max_L=inputArray[i]
            ls.append(max_L)
    
    return ls
