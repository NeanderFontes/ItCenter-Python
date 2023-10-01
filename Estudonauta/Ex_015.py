#Desafio 015: Interação entre Usuário - Programador
#Faça um programa que de acordo com quantidade de diárias e a quantidade de quilômetros percorridos,sendo que o carro é igual a 60/dia e a distância percorrida é de 0.15/km, de acordo com os valores calcular total da empresa de locação

print('='*22, 'DESAFIO 00', '='*22)
print('Empresa de locação de carros:')
diariaCarro, kmPercorrido = int(input('Insira a quantidade de diaria do Carro: ')), float(input('Distância total em Km: '))
valorTotal = (diariaCarro*60) + (kmPercorrido*0.15)
print(f'De acordo com o(s) valor(es)\nDiária(s) Carro: {diariaCarro:.0f} = R${(diariaCarro*60):.2f}\nKm pecorrido: {(kmPercorrido):.1f} = R${(kmPercorrido*0.15):.2f}\nValor Total = {(valorTotal):.2f}')
print('='*22, 'FIM DO DESAFIO', '='*22)