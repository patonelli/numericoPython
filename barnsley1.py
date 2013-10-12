import random as rd
from matplotlib import *
import matplotlib.pylab as pl

def IFS(n,x):
    ''' Define o sistema de quatro tranformacoes de R2, n um inteiro entre 1 e 4
    e x um vetor de R2 '''
    if (n==1):
        return [0.85*x[0] +0.04*x[1] , -0.04*x[0] + 0.85*x[1] +1.6]
    elif (n==2):
        return [-0.15*x[0]+0.28*x[1], 0.26*x[0] + 0.24*x[1] + 0.44]
    elif (n==3):
        return [0.20*x[0] -0.26*x[1], 0.23*x[0]+0.22*x[1] + 1.6]
    else:
        return [0,0.16*x[1]]
        
x0=[0,0]

a=[]
b=[]       
for j in range(200000) :
    x0=IFS(rd.randint(1,4), x0)
    a.append(x0[0])
    b.append(x0[1])
  
pl.plot(a,b,'.')
pl.show()