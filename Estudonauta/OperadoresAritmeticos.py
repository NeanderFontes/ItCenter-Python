#Operadores Aritméticos

print('Para Operadores Aritméticos:')
print('+++ Soma +++')
#Soma
num1 = 5
num2 = 2
numSoma = num1+num2
print(f'Resultado de {num1} + {num2} = {numSoma}\n')

print('--- Subtração ---')
#Subtração
numSubtracao = num1-num2
print(f'Resultado de {num1} - {num2} = {numSubtracao}\n')

print('*** Multiplicação ***')
#Multiplicação
numMultiplicacao = num1*num2
print(f'Resultado de {num1} * {num2} = {numMultiplicacao}\n')

print('/// Divisão Normal ///')
#Divisão
numDivisao = num1/num2
print(f'Resultado de {num1} / {num2} = {numDivisao}\n')

print('** Potência**')
#Potência
numPotencia = num1**num2
print(f'Resultado de {num1} elevado à {num2} = {numPotencia}\n')

print('/// Divisão por Inteiro ///')
#Divisão Inteiro
numDivisaoInteiro = num1//num2
print(f'Resultado de {num1} / {num2} = {numDivisaoInteiro}\n')

print('///Resto da Divisão ///')
#Resto da Divisão
numRestoDivisao = num1%num2
print(f'Resultado do resto da divisão {num1} % {num2} = {numRestoDivisao}')

'''
#Ordem de Precedência
1º = () '» Tudo que estiver em parenteses «'
2º = ** '» As Potências «'
3º = * / // % '» Multiplicação, Divisão, Divisão Inteira, Resto Divisão «'
4º = + - '» Soma e Subtração «'
'''
