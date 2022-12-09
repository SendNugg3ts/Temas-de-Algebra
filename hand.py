import numpy as np

# Define the matrix A
A = np.array([[1,0,1], [1,-1,18], [-2,0,-1], [1,-11,-1]])
print(A)
x = np.array([A[:,0]])
I4 = np.eye(4)#Matriz identidade 4x4
e1 = np.array([I4[:,0]])
normx = np.linalg.norm(x)
mu=1
y =  mu*normx * e1
u=x+y
H1 = I4-((2 * np.matmul(np.transpose(u), u)) / np.matmul(u, np.transpose(u)))
A2 = np.dot(H1,A)
print(A2.round())
print(H1)
#next
x2 = np.array([A2[1:,1]])
I3 = np.eye(3)#Matriz identidade 4x4
e2 = np.array([I3[:,0]])
normx2 = np.linalg.norm(x2)
y2 = normx2 * e2
u2=x2+y2
H2 = I3-((2 * np.matmul(np.transpose(u2), u2)) / np.matmul(u2, np.transpose(u2)))
A2sub=np.array([A2[1:4,1:4]])
A3 = np.dot(H2,A2sub)
#next

