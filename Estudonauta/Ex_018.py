#Desafio 018: Interação entre Usuário - Programador
#Faça um programa que leia um ângulo de valor qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Import Biblioteca math
import math

#Declaração de variáveis e entrada de dados:
print('='*22, 'DESAFIO 018', '='*22)
print('Seno / Cossseno / Tangente')
valorAngulo = float(input('Insira um ângulo qualquer para obter sen, cos, tan: '))

#Saída de dados formatados:
print(f'Valores Correspondetes:\nCos = {(math.cos(math.radians(valorAngulo))):.2f}\nSen = {(math.sin(math.radians(valorAngulo))):.2f}\nTan = {(math.tan(math.radians(valorAngulo))):.2f}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)