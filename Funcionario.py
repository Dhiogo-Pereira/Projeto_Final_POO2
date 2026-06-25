
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
    def cadastro_func(self, lista_func, config):
        print("Registro de Funcionário:")

        #======================================================================Nome do funcionario
        try:
            while True:
                nome = str(input("Nome:\n> ").title())

                if nome in lista_func:
                    print("Nome de funcionario ja em uso.") #Procura o nome na lista de funcionarios
                else: break
        except ValueError:
            print("Cancelando")
            return None


        try:
            cpf = str(input("CPF:\n> "))
        except ValueError:
            print("Cancelando")
            return None

        #==========================================================================Senha da conta
        try:
            while True:
                while True:
                    part1 = False
                    senha = str(input("Senha:\n>"))

                    if len(senha) < 8:  #
                        print("Senha muito curta.")  # Check para ver se a senha é longa
                        continue
                    elif senha.lower() == senha or senha.upper() == senha:  # Check para ver se tem
                        print("Pelo menos uma letra maiuscula e minuscula.")  # letras de caixa alta e baixa
                        continue

                    numeral = False
                    simbolo = False
                    for l in senha.lower():
                        if l in "1234567890":  # teste para ver se algum elemento da senha é numero
                            numeral = True
                        if l not in "1234567890" and l not in "abcdefghijklmnopquvwxyz":
                            simbolo = True   # teste para ver se algum elemento da senha
                    if simbolo and numeral:  # não é nem numero e nem letra.
                        break
                    else:
                        print("Coloque pelo menos um numero e simbolo na senha.")

                    # Primeiro While loop, quebra se todas as
                    # especificações de senha forem batidas.
                    #
                # Segundo While loop, só quebra se as senhas baterem.
                #
                senhaDNV = str(input("Digite novamente a senha:\n>"))
                if senhaDNV != senha:
                    print("Senhas diferentes.")
                else:
                    break

        except ValueError:
            print("Cancelando")
            return None
        #========================================================================Tipo de conta
        if config == False: #Se tiver no modo config, faz um gerente sem perguntar
            try:
                tipo = str(input("Tipo:\n(gerente ou funcionario)\n> ").lower())
                while True:
                    if tipo not in ["gerente","funcionario"]:
                        tipo = str(input("Resposta invalida. Tente novamente ou aperte enter.\n>"))
                    else: break
            except ValueError:
                print("Cancelando")
                return None

            if tipo == "gerente":
                nome = Gerente(nome.title(), senha, cpf)
            else:
                nome = Funcionarios(nome.title(), senha, cpf)
        else:
            nome = Gerente(nome.title(), senha, cpf) #Config

        lista_func.append(nome)           # Coloca um dicionario com nome e classe
        print("Funcionario adicionado.")  # na lista de funcionarios a ser retornada
        return lista_func




