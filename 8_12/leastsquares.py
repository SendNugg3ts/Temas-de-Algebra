import numpy as np

# define matrices Q and R and vector b
Q = np.array([[-0.2,-0.4,-0.88],
 [-0.4,0.86666667,-0.29333333],
 [ 0.8,0.26666667,-0.21333333],
 [-0.4,-0.13333333,0.30666667]])

R = np.array([[-2,4,-7],
 [0,3,-5],
 [0,0,15]])



b = np.array([-1, -1, 0, 5])

# calculate the inverse of Q
Q_transpose = np.transpose(Q)

# calculate the solution vector x using y = QT * b and x = Ry
y = Q_transpose @ b
print(y)
R = np.array([[-2,4, -7,y[0]],
              [0,3,-5,y[1]],
              [0,0,15,y[2]],
              ])
print(R)
x = y @ R

# print the solution vector x
print(x)
