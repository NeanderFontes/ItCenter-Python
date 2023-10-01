#Desafio 014: Interação entre Usuário - Programador
#Fazer um programa que simule a conversão de temperaturas de ºC para ºF

print('='*22, 'DESAFIO 014', '='*22)
print('Conversor de ºC para ºF')
valorTemperatura = float(input('Insira o valor da temperatura em ºC: '))
print(f'{(valorTemperatura):.1f}ºC = {(((valorTemperatura*9)/5)+32):.1f}ºF')
print('='*22, 'FIM DO DESAFIO', '='*22)