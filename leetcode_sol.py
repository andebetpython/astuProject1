matrix=[[1,1,1],[1,0,1],[1,1,1]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]==0:
            while j<=len(matrix)-1:
                matrix[i][j]=0
                j+=1
            i=0
            j=0
        if matrix[i][j] == 0:
            const=j
            while i<=len(matrix)-1:
                matrix[i][j]=0
                i+=1
                j=const
print(matrix)
s={1,3,7,6,5}
s.discard(4)
print(s)