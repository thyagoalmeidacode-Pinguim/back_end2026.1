def mostrar_idade(ano):
    idade = 2026 - ano
    print(f"Você tem: {idade}")

ano_nascimento = int(input("Informe o ano em que você nasceu: "))

mostrar_idade(ano_nascimento)