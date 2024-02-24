def matrix_rotation_clockwise(matrix):
    tem=[[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j]=matrix[j][i]
    for i in range(len(matrix)//2):
        for j in range(len(matrix)):
            matrix[j][i],matrix[j][len(matrix)-1-i]=matrix[j][len(matrix)-1-i],matrix[j][i]
    return matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(matrix_rotation_clockwise(mat))


