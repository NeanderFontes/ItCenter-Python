#Desafio 010: Interação entre Usuário - Programador
#Crie um programa que leia quanto de dinheiro uma pessoa tem e faça a conversão em dolar/euro.
# €1 = R$5.34 (na data de 01 de outubro de 2023).
# $1 = R$5.04 (na data de 01 de outubro de 2023).
print('='*22, 'DESAFIO 00', '='*22)
print('Câmbio de Real(R$) para conversão em Dolar$ e Euro€')
valorEntrada = float(input('Qual valor deseja Utilizar no Câmbio? '))
print(f'O Valor R${valorEntrada} corresponde à:\nDólar = US${valorEntrada*5.04} \nEuro = €{valorEntrada*5.34}')
print('='*22, 'FIM DO DESAFIO', '='*22)