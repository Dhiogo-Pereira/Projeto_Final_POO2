
#================================================
# Este arquivo conterá: Cadastro de clientes e
# gerenciamento(deleção e edição);
#================================================


class Clientes:
    def __init__(self, nome, cpf, historico ):
        self.nome = nome
        self.cpf = cpf
        self.hist = historico

    def cadastro_clt(self):
        print("Registro de Cliente:")