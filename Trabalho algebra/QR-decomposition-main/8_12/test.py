import numpy as np

# Define the matrix A
A = np.array([[1,0,1], [1,-1,18], [-2,0,-1], [1,-11,-1]])
print(A)

# Apply the first Householder transformation to A
x = np.array([A[:,0]]).transpose()
I4 = np.eye(4) # 4x4 identity matrix
e1 = np.array([I4[:,0]]).transpose()
normx = np.linalg.norm(x)
normx = normx*normx
y = normx * e1
u = y - x
H1 = I4 - 2*(u*(u.transpose()))/((u.transpose()*u)[0,0])
A2 = np.dot(H1,A)



