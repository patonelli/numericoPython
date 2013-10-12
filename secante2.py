# Uma nova definição da secante usando o pseudo codigo Kincaid
def secante(f,x0,x1,eps=0.0001):
    
    '''Metodo da secante'''
    a=x0
    b=x1
    u = f(a)
    v = f(b)
    if abs(v) > abs(u):
        a,b=b,a
        u,v=v,u
    c = b - v*(b-a)/(v-u)
    k=1
    print("| k | x_k       | f(xk)   |")
    print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,a,u))
    print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,v))
    while abs(c-b) > eps:
        a=b
        b=c
        u=f(a)
        v=f(b)
        c = b - v*(b-a)/(v-u)
        k+=1
        print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,v))
    return c

#Teste
f= lambda x: x**2 - 2
secante(f,1,2)