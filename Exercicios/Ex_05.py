#Pretende-se criar um algoritmo que troque o valor de 2 variáveis.
#Como podemos fazer esta operação?

num1, num2= int(input("Insira num1: ")), int(input("Insira num2: "))

aux = num1
num1 = num2
num2 = aux

print("Invertendo as ordens")
print(f"num1 = {num1} e num2 = {num2}")