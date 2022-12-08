import numpy as np

# Define the matrix A
A = np.array([[1,0,1], [1,-1,18], [-2,0,-1], [1,-11,-1]])
print(A)
x = np.array([A[:,0]]).transpose()
I4 = np.eye(4)#Matriz identidade 4x4
e1 = np.array([I4[:,0]]).transpose()
normx = np.linalg.norm(x)
normx=normx*normx
y =  normx * e1
u=y-x
H1 = I4-2*(u*(u.transpose()))/((u.transpose()*u)[0,0])
A2 = np.dot(H1,A)
print(A2)
print(H1)
#next
x = np.array([A2[:,0]]).transpose()
I4 = np.eye(4)#Matriz identidade 4x4
e1 = np.array([I4[:,0]]).transpose()
normx = np.linalg.norm(x)
normx=normx*normx
y =  normx * e1
u=y-x
H2 = I4-2*(u*(u.transpose()))/((u.transpose()*u)[0,0])
A3 = np.dot(H2,A2)
print(A3)
print(H2)
#next
x = np.array([A3[:,0]]).transpose()
I4 = np.eye(4)#Matriz identidade 4x4
e1 = np.array([I4[:,0]]).transpose()
normx = np.linalg.norm(x)
normx=normx*normx
y =  normx * e1
u=y-x
H3 = I4-2*(u*(u.transpose()))/((u.transpose()*u)[0,0])
A4 = np.dot(H3,A3)
print(A4)
print(H3)