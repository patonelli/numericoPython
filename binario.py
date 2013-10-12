# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

def binario(a):
    # da a representacao binaria do numero a 
    ParteInteira = int(a)
    ParteDecimal = a-int(a)
    # representacao binaria da parte inteira
    # a lista seguinte guarda os dígitos da parte inteira
    ListaDigitos=[]
    while (ParteInteira > 0):
        ListaDigitos.append(ParteInteira%2)
        ParteInteira=ParteInteira/2
    # lista dos digitos depois da virgula
    ListaResto=[]
    k=1
    while ((ParteDecimal!=0)&(k<6)):
        ListaResto.append(int(2*ParteDecimal))
        ParteDecimal=2*ParteDecimal - int(2*ParteDecimal)
        k=k+1
    # produz a string de representacao:
        
    i=len(ListaDigitos)-1
    p1=""
    while (i>=0):
        p1=p1+str(ListaDigitos[i])
        i=i-1
    # Depois disso p1 tem a parte inteira
    l=0
    p2=""
    while (l<len(ListaResto)):
        p2=p2+str(ListaResto[l])
        l=l+1
    
    return p1+"."+p2
    

print binario(21.75)
     
    
        

