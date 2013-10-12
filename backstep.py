# Alagoritmo de Baixo para cima
import numpy as np

def backstep(A,b):
    ''' resolve Ax=b se A é triangular superior'''
    n=len(A)
    x=list(range(0,n))
    for i in range(n-1,-1,-1):
        l=[x[j]*A[i,j] for j in range(i+1,n)]
        x[i] = (b[i] - sum(l))/A[i,i]
    return x
            
