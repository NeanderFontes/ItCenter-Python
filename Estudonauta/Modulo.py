'''
» Em Python, um módulo é um arquivo contendo código Python que pode incluir funções,    classes e variáveis. Módulos são usados para organizar e reutilizar código em programas Python. Eles ajudam a dividir seu código em partes menores e mais gerenciáveis, tornando-o mais modular e mais fácil de entender.

'''

#Declaração de variáveis:
num = int(input('Digite um numero: '))
#Diferente de módulo podemos importar as bibliotecas de Python
#Import de alguma funcionalidade específica da biblioteca:
from math import pi, ceil, sqrt
raiz = sqrt(num)
print(ceil(raiz))
#Import de toda a biblioteca com todas as funcionalidades:
import math
raiz2 = math.sqrt(num)
print(ceil(raiz2))

#Utilização da biblioteca random
import random
numAleatorio = random.randint(1, 10)
print(f'Número sorteado entre 1 - 10: {numAleatorio}')