#Desafio 025: Interação entre Usuário - Programador
#Crie um programa que leia o nome do usuário e identifique se a pessoa tem "Silva" no nome e retorne true ou false.

#Inicio do programa
print('='*22, 'DESAFIO 025', '='*22)
print("Procurando Nome")

#Declaração de variáveis e entrada de dados:
nomeUsuario = str(input('Digite nome qualquer: ')).strip()

#Saída de dados formatados:
print(f'Buscando por nome Silva... {"SILVA" in nomeUsuario.upper()}')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)