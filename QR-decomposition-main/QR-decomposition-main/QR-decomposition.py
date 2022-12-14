# This file proposes implementations of QR-decomposition methods for solving
# quadratic and overdetermined linear systems of algebraic equations

import numpy as np

def givens_rotation(A):
   # """
    #QR-decomposition of rectangular matrix A using the Givens rotation method.
    #"""

    # Initialization of the orthogonal matrix Q and the upper triangular matrix R
    n, m = A.shape
    Q = np.eye(n)
    R = np.copy(A)

    rows, cols = np.tril_indices(n, -1, m)
    for (row, col) in zip(rows, cols):
        # If the subdiagonal element is nonzero, then compute the nonzero 
        # components of the rotation matrix
        if R[row, col] != 0:
            r = np.sqrt(R[col, col]**2 + R[row, col]**2)
            c, s = R[col, col]/r, -R[row, col]/r

            # The rotation matrix is highly discharged, so it makes no sense 
            # to calculate the total matrix product
            R[col], R[row] = R[col]*c + R[row]*(-s), R[col]*s + R[row]*c
            Q[:, col], Q[:, row] = Q[:, col]*c + Q[:, row]*(-s), Q[:, col]*s + Q[:, row]*c

    return Q[:, :m], R[:m]


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


# To check the solutions, we use the standard deviation of SME
def SME(A, b, x):
    return 1/max(b) * np.sqrt(1/len(b) * np.sum(abs(np.dot(A, x) - b) ** 2))



if __name__=='__main__':

    # Consider an example of a square matrix:
    shape = (4, 4)
    A = np.random.normal(0, 1, shape)
    b = np.random.normal(0, 1, shape[0])

#    Q, R = givens_rotation(A)
#    x = np.linalg.solve(R, Q.T @ b)
#    print('Givens: ', SME(A, b, x))

    Q, R = Hausholder(A)
    x = np.linalg.solve(R, Q.T @ b)
    print('Hausholder: ', SME(A, b, x))


    # Now consider an overdetermined system:
#    shape = (4, 3)
#    A = np.random.normal(0, 1, shape)
#    b = np.random.normal(0, 1, shape[0])

#    Q, R = givens_rotation(A)
#    x = np.linalg.solve(R, Q.T @ b)
#   print('Overdetermined Givens: ', SME(A, b, x))

#    Q, R = Hausholder(A)
#    x = np.linalg.solve(R, Q.T @ b)
#    print('Overdetermined Hausholder: ', SME(A, b, x))
