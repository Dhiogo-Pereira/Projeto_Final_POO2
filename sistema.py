from classes import *

# Sistema de gerenciamento de hotelaria

class Sistema_ctrl:

    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.quartos = []
        self.alugueis = []

    def login(self):
        nome = str(input("Dgite o nome:\n>"))
        senha = str(input("Dgite o senha:\n>"))
        #================================================
        # Sistema de checar o usuario no banco de dados
        #================================================
        
    def register(self):
        print("Registrando Usuario\n:")

        nome = str(input("Nome:\n>"))
        #================================================
        #check para saber se o nome esta nos arquivos***
        #================================================

        cpf = str(input("Digite o CPF:\n[XXXXXXXXX-XX]\n>"))
        while len(cpf) != 12 and cpf[9:11] != '-':
            cpf = str(input("Use o formato [XXXXXXXXX-XX]\n>"))
        #================================================
        while True:
            part1,part2 = False
            senha = str(input("Senha:\n>"))

            if len(senha) < 8:              #
                print("Senha muito curta.") # Check para ver se a senha é longa
                pass
            elif senha.lower() == senha or senha.upper() == senha:  # Check para ver se tem
                print("Pelo menos uma letra maiuscula e minuscula.")# letras de caixa alta e baixa
                pass
            else:
                part1 == True

            for l in senha:
                if l in "1234567890": # teste para ver se algum elemento da senha é numero
                    numeral = True
                if l not in "1234567890" and l not in "abcdefghijklmnopquvwxyz":
                    simbolo = True    # teste para ver se algum elemento da senha
            if simbolo and numeral:   # não é nem numero e nem letra.
                part2 == True
            else:
                print("Coloque pelo menos um numero e simbolo na senha.")
                pass
            if part1 and part2: # Caso todos os testes dem
                break           # positivo quebra o loop.

            while True:
                senhaRPT = str(input("Digite novamente a senha:\n>"))
                if senhaRPT != senha:
                    print ("Senhas diferentes.")
                else: break
            #================================================
            email = str(input("Email:\n>"))
            while "@gmail.com" not in email or "@hotmail.com" not in email or "@protonmail.com" not in email:
                email = str(input("Digite um email valido:\n>"))
            #================================================
            tipo = str(input("Nivel de acesso do funcionario:\n>"))
            while tipo not in ["gerente","funcionario"]:
                tipo = str(input("Escolha uma posição valida.\n[Gerente/Funcionario]\n>"))

            Cliente(nome,nome,cpf,email,[]) #cria instancia de cliente

    def Menu1(self):
        while True:
            try:
                #Interface temporaria:
                print("1) Login;")
                print("2) Register;")
                print("3) End program;")

                option =str(input("Enter your option: ").lower())
                if option in ["1","login"]:
                    check = Sistema_ctrl.login() #Recebe se o login vai funcionar ou não
                    if check == "sucesso":
                        Sistema_ctrl.Menu2()
                    else: print("Informações invalidas.")

                elif option in ["2","register"]:
                    Sistema_ctrl.register()

                elif option in ["3","end program","end"]:
                    return "stop"
            except ValueError:
                print("Erro de entrada, retornando ao menu.")



    def Menu2(self):
        pass
