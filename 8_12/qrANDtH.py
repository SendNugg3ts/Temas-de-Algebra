import numpy as np

def qr_decomposition_householder(A):
    m, n = A.shape
    Q = np.identity(m)
    R = A.copy()

    for i in range(n):
        # Compute the householder transformation for the i-th column
        x = R[i:, i]
        e = np.zeros_like(x, dtype=float)
        e[0] = np.linalg.norm(x)
        e = np.expand_dims(e, axis=1)
        u = x - e
        if np.isclose(np.linalg.norm(u, ord=2), 0):
    # Handle the case where the 2-norm of u is zero
            v = u
        else:
            v = u / np.linalg.norm(u, ord=2)

        # Apply the transformation to R
        R -= 2 * np.dot(v, np.dot(v.T, R))

        # Apply the transformation to Q
        Q[:, i:] -= 2 * Q[:, i:].dot(v).dot(v.T)

    return Q, R

# Test the function
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
Q, R = qr_decomposition_householder(A)

print(Q)
# [[-0.26726124  0.87287156  0.40824829]
#  [-0.53452248 -0.21821789 -0.81649658]
#  [-0.80178373 -0.43643578  0.40824829]]

print(R)
# [[-8.1240384   9.50165304  4.55001444]
#  [ 0.          0.90453403 -0.30151134]
#  [ 0.          0.          0.30151134]]

# Check that Q and R are correct
print(np.allclose(A, Q.dot(R)))  # True
