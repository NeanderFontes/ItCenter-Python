#Desafio 012: Interação entre Usuário - Programador
#Fazer um programa que leia o preço de um produto e mostre seu novo preço com a porcentagem de desconto também inserida pelo utilizador

print('='*22, 'DESAFIO 00', '='*22)
print('Descontos:')
precoProduto, valorDesconto = float(input('Qual o valor do produto? ')), float(input('Qual valor de desconto para calcular? '))
valorPorcentagem = (precoProduto*valorDesconto)/100
print(f'O Produto tem valor de €{precoProduto:.2f} com desconto de {valorDesconto:.0f}% = €{(precoProduto-valorPorcentagem):.2f}')
print('='*22, 'FIM DO DESAFIO', '='*22)