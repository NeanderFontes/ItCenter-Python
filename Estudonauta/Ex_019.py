#Desafio 019: Interação entre Usuário - Programador
#Fazer um prgrama que sortea um dentro de quatro alunos para "apagar" o quadro. Fazer o programa que faça o sorteio lendo o nome e escrevendo o escolhido.

#Import biblioteca Random
import random

#Declaração de variáveis e entrada de dados:
print('='*22, 'DESAFIO 019', '='*22)
print('Sorteando valores')

#Saída de dados formatados:
aluno1, aluno2, aluno3, aluno4 = input('Insira nome do Aluno 1: '), input('Insira nome do Aluno 2: '), input('Insira nome do Aluno 3: '), input('Insira nome do Aluno 4: ')
sortearAluno = [aluno1, aluno2, aluno3, aluno4]
alunoSorteado = random.choice(sortearAluno)
print(f'O Aluno Sorteado foi o(a) {alunoSorteado}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)