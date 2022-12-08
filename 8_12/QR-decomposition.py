import numpy as np

def Hausholder(A):
  #  """
   # QR-decomposition of a rectangular matrix A using the Householder reflection method.
    #"""
    print(A)
    # Initialization of the orthogonal matrix Q and the upper triangular matrix R
    n, m = A.shape
    Q = np.eye(n)
    R = np.copy(A)
    print(Q)
    print(R)
    for k in range(m):
        v = np.copy(R[k:, k]).reshape((n-k, 1))
        print(v)
        v[0] = v[0] + np.sign(v[0]) * np.linalg.norm(v)
        v = v / np.linalg.norm(v)
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

