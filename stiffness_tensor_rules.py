import numpy as np

def TensorTermsCombinations():
    independent_variables = np.array([[0,0,0,0], [0,0,1,1], [0,0,2,2], [0,0,1,2], [0,0,0,2], [0,0,0,1], [1,1,1,1],
                                      [1,1,2,2], [1,1,1,2], [1,1,0,2], [1,1,0,1], [2,2,2,2], [2,2,1,2], [2,2,0,2],
                                      [2,2,0,1], [1,2,1,2], [1,2,0,2], [1,2,0,1], [0,2,0,2], [0,2,0,1], [0,1,0,1]])

    r = 0
    v = np.empty(shape=[21,8])
    for a in range(21):
        i, j, k, l = [independent_variables[a][b] for b in range(4)]
        i+=1
        j+=1
        k += 1
        l += 1
        v[a][0] = str(str(i) + str(j) + str(k) + str(l))
        v[a][1] = str(str(i) + str(j) + str(l) + str(k))
        v[a][2] = str(str(j) + str(i) + str(k) + str(l))
        v[a][3] = str(str(j) + str(i) + str(l) + str(k))
        v[a][4] = str(str(k) + str(l) + str(j) + str(i))
        v[a][5] = str(str(k) + str(l) + str(i) + str(j))
        v[a][6] = str(str(l) + str(k) + str(i) + str(j))
        v[a][7] = str(str(l) + str(k) + str(j) + str(i))
        r = r + len(np.unique(v[a]))
        print(a,'   ',np.unique(v[a]))
    print('\nTotal Terms = ', r)
