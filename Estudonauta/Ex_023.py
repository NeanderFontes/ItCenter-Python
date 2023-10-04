#Desafio 023: Interação entre Usuário - Programador
#Faça um programa que leia um numero qualquer inteiro e mostre no console os digitos separados
#Ex.: Numero = 1834
#Milhar = 1
#Centena = 8
#Dezena = 3
#Unidade = 4

#Inicio do programa
print('='*22, 'DESAFIO 023', '='*22)

#Declaração de variáveis e entrada de dados:
numEntrada = int(input('Insira um valor inteiro qualquer:'))
numUnidade = numEntrada // 1 % 10
numDezena = numEntrada // 10 % 10
numCentena = numEntrada // 100 % 10
numMilhar = numEntrada // 1000 % 10

#Saída de dados formatados:
print(f'Parte Milhar = {numMilhar}')
print(f'Parte Centena = {numCentena}')
print(f'Parte Dezena = {numDezena}')
print(f'Parte Unidade = {numUnidade}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)