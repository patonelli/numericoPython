''' iteracao de gauss-seidel '''
from pylab import *

# dou a matriz quadrada de coeficientes e vetor independente

A=matrix('4 2 0.6; 2 5.5 3; 1 0 2.5')
b=matrix('1. ; 3.; 1.')

def iterGS(x, A, b):
    xold=x.copy()
    L=list(x)
    for i in range(len(A)):
        soma = 0.
        for j in range(len(A)):
            if (j != i): soma += -A[i,j]*L[j]
        L[i] = (b[i] + soma)/A[i,i]
    return L

def GaussSeidel(x0,A,b,eps,n):
    IterGauss=0
    dx=10.
    while ((IterGauss<=n)&(dx>eps)):
        xold = x0.copy()
        L=iterGS(x0, A, b)
        for k in range(len(L)) : L[k]=float(L[k])
        x0=matrix(L).T
        IterGauss += 1
        dx = norm(x0-xold)
    return x0 , IterGauss, dx

########## Teste com um exemplo ##############

x0=matrix(' 0; 0; 0 ')

sol = GaussSeidel(x0,A,b,0.0000001, 100)

print sol
