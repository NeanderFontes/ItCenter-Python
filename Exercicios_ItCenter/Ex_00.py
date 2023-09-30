#Criterios de avaliação: projeto 1 : 30% projeto 2 30% teste : 40%
#Inserir notas dos momentos de avialiação e verificar se foi aprovado

projeto1, projeto2, teste = int(input("Insira as projeto1: ")), int(input("Insira as projeto2: ")), int(input("Insira as teste: "))
nota = projeto1*0.3 + projeto2*0.4 + teste*0.4

if nota >= 10 :
    print("Passou")
else:
    print("Reprovado")