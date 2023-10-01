#Desafio 021: Interação entre Usuário - Programador
#Utilizar biblioteca para apresentar em ordem aleatória os nomes declarados.

#Inicio do programa
print('='*22, 'DESAFIO 021', '='*22)
import random

#Declaração de variáveis e entrada de dados:
print('Sorteando valores')

#Saída de dados formatados:
aluno1, aluno2, aluno3, aluno4 = input('Insira nome do Aluno 1: '), input('Insira nome do Aluno 2: '), input('Insira nome do Aluno 3: '), input('Insira nome do Aluno 4: ')
sortearAluno = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sortearAluno)
print(f'A ordem será: {sortearAluno}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)