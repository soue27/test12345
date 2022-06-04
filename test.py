def verify():
    pass


def is_isolate():
    pass

flag = True
for i in range(dlina - 1):
    for j in range(dlina - 1):
        if lst_in[i][j] + lst_in[i+1][j] + lst_in[i][j+1] + lst_in[i+1][j+1] > 1:
            flag = False
            break
        if not flag:
            break
    if not flag:
        break