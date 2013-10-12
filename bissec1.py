#define a funcao bisseccao

def bissec(f, a, b, eps=0.0001):
    ''' Uma funcao que executa a biseccao do intervalo (a,b), não testa se tem zero '''
    x0=a
    x1=b
    k=0
    print("|  k  | x0       | x1       | xmid     |f(x0)*f(xmid)|")
    while (x1-x0)/2 > eps :
        xmid = (x1+x0)/2
        # incluir print para debug e o contador
        print("| {0:<2}  | {1:1.6f} | {2:<1.6f} | {3:<1.6f} | {4:<+2.8f} |".format(k,x0,x1,xmid,f(xmid)*f(x0)))
        if f(xmid)*f(x0)>0:
            x0,x1=xmid,x1
        else : x0,x1 = x0,xmid
        k+=1
    return (x0+x1)/2
    
#Rodando um teste
f = lambda x: x**2-2
a,b = 0,2
bissec(f,a,b)