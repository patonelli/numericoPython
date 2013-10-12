def secante(f,x0,x1,eps=0.0001):
    '''Metodo da secante'''
    a=x0
    b=x1
    c = b - f(b)*(b-a)/(f(b)-f(a))
    k=1
    print("| k | x_k       | |x_k-xk-1|   |")
    print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,c,abs(c-b)))
    while abs(c-b) > eps:
        a=b
        b=c
        c = b - f(b)*(b-a)/(f(b)-f(a))
        k+=1
        print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,c,abs(c-b)))
    return c

#Teste
f= lambda x: x**2 - 2
secante(f,1,2)