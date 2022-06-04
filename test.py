def is_isolate(matrix, a, b):
    flag = True
    if matrix[a][b] + matrix[a + 1][b] + matrix[a][b + 1] + matrix[a + 1][b + 1] > 1:
        flag = False
    return flag


def verify(matrix):
    flag = True
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1):
            if matrix[i][j] == 1:
                flag = is_isolate(matrix, i, j)
            if flag == False:
                break
    return flag
