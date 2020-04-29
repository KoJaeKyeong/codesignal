def adjacentElementsProduct(inputArray):
    multiplyArray = [i*j for i,j in zip(inputArray[:],inputArray[1:])]
    return max(multiplyArray)
