def first_row(mat, i, j, n):
    for i in range(n):
        mat[i][j] = 4
    print(i, j)
    j=i
    
    for i in range(n):
        mat[i][j] = 4
    return mat
    

n = 7
no = 4
mat = [[0]*n for i in range(n)]

mat = first_row(mat, 0, 0, n)
print(mat)
