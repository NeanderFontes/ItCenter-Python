#Tipos primitivos em Python
''' 
int = numeros inteiros
float = numeros reais
bool = (True ou False)
str = 'String'

Para imprimir os valores precisa fazer Cast do tipo na variável.
'''

#Fomat para resultado de variáveis
print('Insira numeros a seguir:')
num1, num2 = int(input('Insira primeiro numero: ')), int(input('Insira o segundo numero: '))
soma = num1+num2
print('Soma dos valores = {}' .format(soma))
print(f'Soma entre {num1} + {num2} = {soma}')
