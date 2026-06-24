from Banco_dados import BDC, BDF, BDQ

# ================================================
# Este arquivo conterá: Cadastro de funcionarios
# e gerenciamento(deleção e edição);
# ================================================


class Funcionarios:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf

class Gerente(Funcionarios):
    def cadastro_func(self, lista_func):
        print("Registro de Funcionário:")
        try:
            nome = str(input("Nome:\n> "))
        except ValueError:
            print("Cancelando")
            return

        try:
            cpf = str(input("CPF:\n> "))
        except ValueError:
            print("Cancelando")
            return

        try:
            senha = str(input("Senha:\n> "))
        except ValueError:
            print("Cancelando")
            return

        try:
            tipo = str(input("Tipo:\n(gerente ou funcionario)\n> ").lower())
            while True:
                if tipo not in ["gerente","funcionario"]:
                    tipo = str(input("Resposta invalida. Tente novamente ou aperte enter.\n>"))
                else: break
        except ValueError:
            print("Cancelando")
            return

        if tipo == "gerente":
            nome = Gerente(nome,senha,cpf)
        else:
            nome = Funcionarios(nome,cpf,senha)






