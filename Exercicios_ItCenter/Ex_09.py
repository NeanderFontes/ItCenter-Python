#Construir um programa que recebe 2 numeros inteiros introduzidos pelo utilizador
#Criar funções para executar as seguintes operações:
# 1) Devolver a soma dos dois numeros;
# 2) Devolver a soma de 5 unidades de ambos os valores (a função deverá aceitar 3 agumentos: val1, val2, plus);
# 3) Imprimir os 10 primeiros numeros impares a partir do primeiro valor inserido.


#Função para retornar soma de 2 numeros:
def soma(num1, num2):
    return num1+num2

#Função para retornar a soma de 5 unidade de ambos os numeros:
def soma5(num1, num2, plus):
    return((num1+plus), (num2+plus))

#Função para imprimir 10 valores impares a partir do primeiro valor inserido:
def imprimirValorImpar(num1):
    if num1 % 2 != 0:
        num1 += 1
    else:
        num1 += 2
        #todo "Contuniar implementação de código:"
        #for i in range
    print(num1)


#Entrada de dados:
num1, num2 = int(input('Insira 1º valor: ')), int(input('Insira 2º valor: '))
print(soma(num1, num2))
print(imprimirValorImpar(num1))
print(soma5(num1, num2, 5))