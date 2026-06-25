
def login(lista_func):
    print("\nLogin:")
    try:
        nome = str(input("Nome:").title())
    except ValueError:
        return None
    try:
        senha = str(input("Senha:"))
    except ValueError:
        return None

    for l in lista_func:
        if l.nome == nome and l.senha == senha:
            return l

    print("Nenhum cadastro encontrado.")
    return None
