# Lista para armazenar os formandos
formandos = []

# Função para registrar um novo formando
def registrar_formando():
    nome = input("Digite o nome do formando: ")
    sexo = input("Digite o sexo do formando (M/F): ")
    idade = int(input("Digite a idade do formando: "))
    morada = input("Digite a morada do formando: ")
    curso = input("Digite o curso em que o formando se inscreveu: ")

    # Criando um dicionário com os dados do formando
    formando = {
        "Nome": nome,
        "Sexo": sexo,
        "Idade": idade,
        "Morada": morada,
        "Curso": curso
    }

    # Adicionando o dicionário à lista de formandos
    formandos.append(formando)
    print("Formando registrado com sucesso!\n")

# Função para exibir todos os formandos registrados
def mostrar_formandos():
    if not formandos:
        print("Nenhum formando registrado ainda.\n")
    else:
        print("Lista de Formandos:")
        for index, formando in enumerate(formandos, start=1):
            print(f"{index}. Nome: {formando['Nome']}, Sexo: {formando['Sexo']}, Idade: {formando['Idade']}, Morada: {formando['Morada']}, Curso: {formando['Curso']}")
        print()

# Loop principal do programa
while True:
    print("Menu:")
    print("1. Registrar novo formando")
    print("2. Mostrar formandos registrados")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        registrar_formando()
    elif escolha == "2":
        mostrar_formandos()
    elif escolha == "3":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")
