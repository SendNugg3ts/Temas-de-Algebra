import numpy as np

def Hausholder(A):
    n, m = A.shape#linhas (n) colunas(m)
    Q = np.eye(n) #Matriz identidade do tamanho das linhas
    R = np.copy(A) #R é uma copia da matriz A que posteriormente será a triangular superior

    for k in range(m):#fazer transformações para todas as colunas de A
        v = np.copy(R[k:, k]).reshape((n-k, 1))
        print(v)#v será a primeira coluna de A na primeira transformação e posteriormente será as outras colunas mas diminuindo sempre o tamanho para deixar R uma triangular superior.
        v[0] = v[0] + np.sign(v[0]) * np.linalg.norm(v)
        print(v)#v[0] passará a ser o primeiro elemento mais a norma de v
        v = v / np.linalg.norm(v)
        print(v)
        R[k:, k:] = R[k:, k:] - 2 * v @ v.T @ R[k:, k:]
        Q[k:] = Q[k:] - 2 * v @ v.T @ Q[k:]

    return Q[:m].T, R[:m]

shape = (4, 3)
A = np.array([[1,0,1],
[1,-1,18],
[-2,0,-1],
[1,-11,-1]])
b = np.array([-1,-1,0,5])

Q, R = Hausholder(A)
print(Q)
print(R)

