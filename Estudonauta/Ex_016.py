#Desafio 016: Interação entre Usuário - Programador
#Criar um programa que ler um numero real qualquer pelo utilizador e imprima no console somente sua parte inteira.

#Import biblioteca math
from math import trunc

#Inicio do programa
print('='*22, 'DESAFIO 016', '='*22)
print('Parte inteira de um numero real/ponto flutuante')

#Declaração de variáveis e entrada de dados:
numEntrada = float(input('Insira um valor com casas decimais: '))

#Saída de dados formatados:
#Utilização import math
print(f'Valor de {numEntrada}\nValor Inteiro = {trunc(numEntrada)}')

#Utilização de castInt
print()
print(f'Valor de {numEntrada}\nValorInteiro = {int(numEntrada)}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)