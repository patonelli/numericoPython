# ilustra o processo de newton-raphson
def newtonRaphson(f,flinha,x0,eps=0.0001):
    '''executa o procedimento de newton'''
    a=x0
    b= a - (f(a)/flinha(a))
    k=1 #quero contar as iterações
    print("| k | x_k       | |x_k-xk-1|   |")
    print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,abs(b-a)))
  
    while (abs(b-a)>eps):
        a=b
        b= a - (f(a)/flinha(a))
        k+=1
        print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,abs(b-a)))
       
    return b
# função de teste
f = lambda x: x**2-2
flinha = lambda x: 2*x
x0=1.5
newtonRaphson(f,flinha,x0)