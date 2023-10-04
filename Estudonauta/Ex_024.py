#Desafio 024: Interação entre Usuário - Programador
#Criar um programa que leia o nome de cidade do usuário, e dizer se a cidade começa ou não com nome "SANTO" e retorne com true ou false

#Inicio do programa
print('='*22, 'DESAFIO 024', '='*22)

#Declaração de variáveis e entrada de dados:
nomeUsuario, nomeCidade = input('Digite seu nome: '), str(input('Olá, Digite a cidade onde mora: ')).strip()

#Saída de dados formatados:
print(f'{nomeCidade.upper()[:5]}' == "SANTO")


#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)