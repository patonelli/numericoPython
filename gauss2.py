# gauss elimination as seen in the classroom
import numpy as np


# A is type array from numpy
# remember: A[0.0] is the first element
# Elementary row operations:

def  troca_linha(A,i,j):
    '''Troca as linhas i e j da matriz A'''
    buffer = A[i].copy()
    A[i] = A[j]
    A[j] = buffer
    return A

def mult_linha(A,i,alfa):
    '''Multiplica por alfa a linha i'''
    A[i] = alfa*A[i]
    return A

def subs_linha(A,i,k,alfa):
    '''soma a linha i com um multiplo da linha k'''
    A[i] = A[i] + alfa*A[k]
    return A

# step k of gauss elimination:
def gauss_step(A,k):
    '''O k-esimo passo na eliminacao de gauss'''
    L=range(len(A))
    for j in L[k+1:]:
        m=-A[j,k]/A[k,k]
        A=subs_linha(A,j,k,m)
        A[j,k]=-m # Aproveitamos a matriz A pra guardar o multiplicador
    return A

# triangle form, without care and pivoting
def triangle_form(A):
    '''Retorna a matriz escalonada, 
    com os multiplicadores na parte triangular inferior'''
    L=len(A)
    for k in range(L-1):
        p=pivo(A,k)
        troca_linha(A,k,p)
        gauss_step(A,k)
     
    return A
    
def pivo(A,n):
    ''' retorna o indice de pivotacao da matriz A na coluna n, 
    a partir da linha n'''
    l=len(A) # numero de linhas de A
    c=len(A[0]) # numero de colunas
    if (l<=n) or (c<=n):
        raise ValueError("n deve ser menor que dimensao de A")
    p=n # inicio o pivo como n, e vou aumentando
    for k in range(n,l):
        if abs(A[k,n]) > abs(A[p,n]):
            p=k
    return p

# roda um teste

A=np.array([[1,2,3],
	 [2,-1,9],
	 [3.,0., 2.]])
B=triangle_form(A)
