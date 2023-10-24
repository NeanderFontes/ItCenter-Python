'''
Manipulação de tratamento de textos em Python.
» Uma cadeia String está sempre entre '' ou ""
» Obs: Uma cadeisa de String em Python é declarada na mémoria do computador como um Array separando por cada palavra, espaço e ou vírgulas dentro da "Frase". Sendo denominada de 'Técnica Fatiamento' ou 'Range' indicando os índices de 0 até contagem final da frase ou sendo declarado na variável o tamanho da lista.
Ex.:
'''
frase = 'Aprendendo Python'
#[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10][11][12][13][14][15][16]
#[A] [P] [R] [E] [N] [D] [E] [N] [D] [O]  [] [P] [Y] [T] [H] [O] [N]
print(f'» Imprimir caracter de indice [9]: {frase[9]}')
print(f'» Imprimir os caracteres entre [11 - 16]: {frase[11:17]}')
print(f'» Imprimir os caracteres entre [11 - 16] "Pulando de 2 em 2": {frase[11:17:2]}')
print(f'» Imprimir os caracteres do Inicio até index marcado: {frase[:10]}')


#Analise de uma String:
print(f'» Imprimir o Tamanho da frase: {len(frase)}')
print(f'» Imprimir o Tamanho da frase: {len(frase.strip())}')
print(f'» Imprimir a Quantidade de letras "A": {frase.upper().count("A",0,17)}')
print(f'» Imprimir a ordem da palavra "END": {frase.upper().find("END",0,17)}')
print(f'Existe Palavra "Android" na frase? {"ANDROID" in frase.upper()}')
print(f'replace() = Trocar Frase "Python" por "Android" = {frase.replace("Python", "Android")}')
print(f'replace() não atribui novo valor à variável "frase" por tanto, frase = {frase}')
