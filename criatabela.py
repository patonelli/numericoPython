# construindo o arquivo de tabela
tabela=[]
novoX = input("Digite um valor de X ou branco para sair: ")
if not(novoX == " ") :
    novoY = input("Digite um valor de Y: ")
    if novoY == " ":
       novoY=novoX

while not(novoX == " "):
    tabela.append(novoX+" "+novoY+"\n")
    novoX = input("Digite um valor de X ou branco para sair: ")
    if not(novoX == " ") :
        novoY = input("Digite um valor de Y: ")
        if novoY == " ":
            novoY=novoX

# guardamos a lista tabela num arquivo:

nome = input("digite o nome da tabela: ")
with open(nome, mode="w") as um_arquivo:
    for linha in tabela:
        um_arquivo.write(linha)
    
