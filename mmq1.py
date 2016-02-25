# interpolação de uma reta por uma tabela
# 1. Leitura da tabela de um arquivo
with open('tabela.txt') as arquivo:
    tabela =[]
    for linha in arquivo:
        tabela.append(linha.strip())

# 2. Construção da tabela como lista de pontos
tab =[]
for treco in tabela:
    a = treco.split()
    tab.append([float(a[0]),float(a[1])])

# 3. Construção e resolução do sistema normal
k= len(tab)
a11= sum([tab[i][0]**2 for i in range(k)])
a12 = sum([tab[i][0] for i in range(k)])
b1 = sum([tab[i][1]*tab[i][0] for i in range(k)])
b2 = sum([tab[i][1] for i in range(k)])

A = (b1*k - b2*a12)/(a11*k-a12**2)
B= (a11*b2-a12*b1)/(a11*k - a12**2)

# 4. plotar os pontos da tabela e a reta ajustada

import pylab as pl

X = [tab[i][0] for i in range(k)]
Y = [tab[i][1] for i in range(k)]
r = lambda x: A*x + B
x = pl.linspace(0,10,100)
pl.plot(X,Y,'ro')
pl.plot(x,r(x))
pl.grid()
pl.show()
