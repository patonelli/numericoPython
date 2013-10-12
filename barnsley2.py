import random as rd
from matplotlib import *
#Escolhemos (ou fixamos) tres pontos
A=[-1,-1.]
B=[0,2] 
C=[2,0]

def Jogo(n,x):
    ''' Escolhe um ponto e anda ate a metade do caminho deste ponto'''
    if (n==1):
        return [0.5*x[0]+0.5*A[0], 0.5*x[1]+0.5*A[1]]
    elif (n==2):
        return [0.5*x[0] +0.5*B[0], 0.5*x[1] +0.5*B[1]]
    else:
        return [0.5*x[0] + 0.5*C[0], 0.5*x[1] + 0.5*C[1]]
P=[0,0]      
a=[0]
b=[0]
for j in range(20000):
    P = Jogo(rd.randint(1,3),P)
    a.append(P[0])
    b.append(P[1])
pylab.plot(a,b,'.')
pylab.show()