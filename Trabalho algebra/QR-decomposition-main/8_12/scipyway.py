from scipy.linalg import qr
import numpy as np
from scipy.linalg import lstsq

A = [[1,0,1], [1,-1,18], [-2,0,-1], [1,-11,-1]]#matriz A gerada no SageMath
b = [[-1, -1, 0, 5]]#vetor b gerado no SageMath
Q, R = qr(A)#Factorização QR onde se obtém Matriz ortonormada Q e matriz triangular superior R

print(Q)
print(R)
b=np.transpose(b)#transpor b para ficar 4x1
print(b)
Qtb= np.transpose(Q) @ b #operação Q^T * b
print(Qtb)
x = lstsq(R, Qtb)#Solução final usando a função lstsq que da output da solução dos minimos quadrados para Ax=b,
                 #Neste caso Rx=Q^T * b   

print(x[0])#O output da função são 4 arrays, no caso queremos o primeiro que respresenta a solução de x
