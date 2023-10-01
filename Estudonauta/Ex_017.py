#Desafio 017: Interação entre Usuário - Programador
#Faça um programa que leia o comprimento do cateto oposto e adjacente de um triângulo retangular, e calcule sua hipotenusa.

#Import biblioteca math
import math

#Declaração de variáveis e entrada de dados:
print('='*22, 'DESAFIO 017', '='*22)
print('Calcular Hipotenusa do triângulo')
catetoOposto, catetoAdj = float(input('Insira o valor do cateto oposto: ')), float(input('Insira o valor do cateto adjacente: '))

#Saída de dados formatados:
#Forma matemática:
hipotenusa = (catetoOposto**2 + catetoAdj**2) ** (1/2)
print(f'Valor da Hipotenusa = {hipotenusa:.2f}')

#Forma do import math
print(f'Hipotenusa² = {catetoOposto}² + {catetoAdj}²\nHipotenusa = {math.hypot(catetoOposto, catetoAdj):.2f}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)