#Desafio 011: Interação entre Usuário - Programador
#Fazer um programa que ler a largura e altura de uma parede em metros, calcular a área e quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2

print('='*22, 'DESAFIO 00', '='*22)
print('Parede em Metros quadrados:')
altura, base = int(input('Qual valor da altura em metros? ')), int(input('Qual valor da largura em metros? '))
print(f'A área da parede = {altura*base}m2\n1L de tinta pinta 2m2 logo...')
print(f'{(altura*base)/2}L correspondem ao total de litros de tintas necessário para pintar a parede')
print('='*22, 'FIM DO DESAFIO', '='*22)