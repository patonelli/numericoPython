''' Modelo do terceiro EP por:
    Pedro A Tonelli '''

# Primeiro ler o arquivo de dados
with open("tabela_foguete.txt", "r") as raw_table:
    tabela = []
    for linha in raw_table:
        tabela.append([float(a) for a in linha.strip().split()])

# segundo calcular as interpolações
def interpolador(x,y):
    '''Dadas duas listas x e y retorna a lista dos coeficientes do polinômio interpolador '''
    # Uma versão do método da Lagrange
    L=[]
    for i in range(len(x)):
        l=[1]
        for j in range(len(x)):
            if i != j:
                l=convp(l,[-x[j], 1])
        alfa = y[i]/avalia(l,x[i])
        L.append([alfa*u for u in l])
    
    return [sum([u[i] for u in L]) for i in range(len(L))]
    
    
def avalia(p,x):
    ''' avalia o polinomio p no ponto x '''
    n=len(p)-1
    resultado = p[n]
    while n > 0 :
        n = n-1
        resultado = p[n] + resultado*x
    return resultado
    
def convp(p,q):
    ''' lista com os coeficientes dos produtos de polinomios p e q'''
    # c_k = sum(a_i*b_{k-i}) produto de convolução
    n=len(p)-1
    m=len(q)-1
    resultado = []
    for k in range(m+n+1):
        S=0
        for i in range(k+1):
            if i< len(p) and k-i < len(q):
                S = S + p[i]*q[k-i]
        resultado.append(S)
        #resultado.append(sum([p[i]*q[k-i] for i in range(k+1)]))
    return resultado
    
tempo = [a[0] for a in tabela]
hordes = [a[1] for a in tabela]
verdes = [a[2] for a in tabela]
p1 = interpolador(tempo , hordes)
p2 = interpolador(tempo, verdes)
p3 = interpolador(hordes,verdes)

# Terceiro calcular os dados pedidos e fazer as comparações

T = float(input("Entrar com o tempo (entre 0 e 500s)->"))
xT = avalia(p1,T)
yT = avalia(p2, T)
yX = avalia(p3,T)

#print( " A posição horizontal em {0} é {1}. A posição vertical é {2] ou {3}. ".format(T,xT,yT,yX) )