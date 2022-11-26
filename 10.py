def f(lul):
    n = []
    for i in lul:
        if i not in n and i[0] is not None:
            n.append(i)
    return n


# можно оптимизировать
def trans(matrix):
    trans_matrix = [[0 for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def main(matrix):
    matrix = f(matrix)
    trans_matrix = trans(matrix)
    trans_matrix = f(trans_matrix)
    matrix = trans(trans_matrix)
    for i in matrix:
        i[0] = i[0].replace('/', '-')
        i[0] = i[0].replace('да', 'true')
        i[0] = i[0].replace('нет', 'false')
        i.insert(0, i[0].split('#')[1])
        i[1] = i[1].split('#')[0]
        for j in range(2, len(i)):
            i[j] = i[j][3:13] + i[j][14:]
    return trans(matrix)


if __name__ == '__main__':
    print(main(
        [['02/11/2001#да', '+7 715 968-27-55', '+7 715 968-27-55'],
         ['02/11/2001#да', '+7 715 968-27-55', '+7 715 968-27-55'],
         ['23/03/1999#нет', '+7 459 999-71-72', '+7 459 999-71-72'],
         ['19/02/2001#нет', '+7 039 296-33-77', '+7 039 296-33-77'],
         ['20/09/2001#нет', '+7 900 335-50-39', '+7 900 335-50-39'],
         ['02/11/2001#да', '+7 715 968-27-55', '+7 715 968-27-55']]
    ))
