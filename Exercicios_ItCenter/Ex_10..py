#Dado o seguinte código e resultado, implementar uma função que imprima:
#*
#**
#***
#****
#*****
#******

#Função para pintar:
def pinta(val, char):
    print(f'{char}' * val)

#Entrada de dados:
numEntrada = int(input('Insira numero de valor da pirâmide: '))
for i in range(1, 11):
    pinta(i, "*")