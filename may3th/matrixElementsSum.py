def matrixElementsSum(matrix):
    s=0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i+1][j]=0
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s += matrix[i][j]

    return s
