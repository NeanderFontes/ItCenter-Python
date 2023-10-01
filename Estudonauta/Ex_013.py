#Desafio 013: Interação entre Usuário - Programador
#Faça um algoritmo que leia o salário do funcionário e retorne valor com 15% de aumento

print('='*22, 'DESAFIO 013', '='*22)
print('Aumento de Salário do Funcionário em 15%.')
nomeFuncionario, salarioFuncionario = input('Qual nome do funcionário? '), float(input(f'Qual o salário atual deste funcionário? €'))
valorPocentagem = (salarioFuncionario*15)/100
print(f'O Funcionário {nomeFuncionario} terá aumento de {valorPocentagem:.0f}, referente à 15% do seu salário\nSalario Atual = €{(salarioFuncionario+valorPocentagem):.2f}')
print('='*22, 'FIM DO DESAFIO', '='*22)