def makeArrayConsecutive2(statues):
    count=0
    statues.sort()
    for i in range(1,len(statues)):
        count+=statues[-i]-statues[-i-1]-1


    return count
