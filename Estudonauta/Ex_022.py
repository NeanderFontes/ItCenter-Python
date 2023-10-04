#Desafio 022: Interação entre Usuário - Programador
#Criar um programa que leia o nome completo do usuário e mostre em:
#1) Letras maiúsculas
#2) letras minúsculas
#3) Quantas letras ao todo sem considerar espaços
#4) Quantas letras tem o primeiro nome

#Inicio do programa
print('='*22, 'DESAFIO 022', '='*22)

#Declaração de variáveis e entrada de dados:
print("Analisador de textos")
nomeUsuario = str(input('Digite o teu nome: ')).strip()
listaNome = nomeUsuario.split()
print(f'Olá {listaNome[0]}, Seja Bem vindo!!')

#Saída de dados formatados:
#1)Letra maúscula:
print(f'Seu Nome com todas Letras maiúsculas: {nomeUsuario.upper()}')

#2)Letra minúscula:
print(f'Seu Nome com todas Letras minúscula: {nomeUsuario.lower()}')

#3)Quantas letras ao todo sem considerar espaços:
print(f'Ao Total contém {len(nomeUsuario) - nomeUsuario.count(" ")}')

#4)Quantas letras tem o primeiro nome:
nomeDividido = nomeUsuario.split()
print(f'O nome principal é {nomeDividido[0]} e contém {len(nomeDividido[0])} Letras')

#Finalização do programa:
print('='*22, 'FIM DO DESAFIO', '='*22)