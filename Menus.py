
from Cliente import Clientes as C
from Funcionario import Funcionarios as F
from Funcionario import Gerente as G
from Login import login

#====================================================================================
Juan = G("Juan", "NUMERO", "123Mamaco^^")
Dhiogo = G("Dhiogo", "NUMERO", "Biruleibe12!")

Joselina = C("Joelina", "NUMERO", [])

# Banco de dados temporario
c = {"clientes": [Joselina]}
q = {"quartos": []}
a = {"alugueis": []}
f = {"funcionarios": [Juan, Dhiogo]}
#=====================================================================================
# Informação do banco de dados
#=====================================================================================

def SalvaBanco(nome, lista_especifica, dados):
    nome = {lista_especifica:dados}



class Stm_Menus:
    def menu_funcionario(self):
        funcionarios = f.get("funcionarios")

        while True:
            mode = None                    # Ve se a lista tem um gerente
            for l in funcionarios:         #
                if type(l) == G:           # Se não tiver, entra no modo
                    mode = "tem gerente"   # configuração de sistema.

            if mode != "tem gerente":
                print("\n\nEntrando no modo configuração:")
                Func_com_gerente = Stm_Menus.config(None,funcionarios)
                f["funcionarios"] = Func_com_gerente
            else: break
        #--------------------------------------------------------------
        while True: # Loop do menu de login
            try:
                print("\nMenu Temporario 1:")
                print("1) Login")
                print("0) Sair")

                option = str(input(">"))
                if option == "1":
                    loginfo = login(funcionarios)
                    if loginfo != None:
                        Stm_Menus.menu_programa(loginfo)

                elif option == "0":
                    return None
                else: raise ValueError

            except ValueError:
                print("Valor invalido\n\n")

    # ==============================================================================================
    def config(self, funcionarios):             # Gera uma conta gerente para se fazer login
        print("\nCriando conta gerente:")       # (Pois apenas gerentes podem criar funcionarios novos)
        while True:
            lista_func = G.cadastro_func(None, funcionarios, True)
            if lista_func != None:
                return lista_func

    # ==============================================================================================
    def menu_programa(self):
        funcionarios = f.get("funcionarios")

        while True:

            print("\n\nMenu Temporario 2:")
            print("1) Cadastro de cliente")
            print("2) Processar aluguel")
            print("3) Gerenciamento de clientes")
            if type(self) == G:
                print("4) Cadastro de funcionario")
                print("5) Gerenciamento de funcionários")
            print("0) Retornar")

            option = str(input(">"))

            if option == "1":
                pass
            # -------------------------------------------------------------------------------
            elif option == "2":
                pass
            # -------------------------------------------------------------------------------
            elif option == "3":
                pass
            # -------------------------------------------------------------------------------
            elif option == "4" and type(self) == G:
                func_temporario = G.cadastro_func(None,funcionarios,False)
                if func_temporario != None:
                    funcionarios = func_temporario

                    print(funcionarios)
                    f["funcionarios"] = funcionarios
            # -------------------------------------------------------------------------------
            elif option == "5" and type(self) == G:
                print("Gerenciamento de funcionarios:")
                print("1) Deletar")
                print("2) Editar")

                try:
                    option = str(input(">"))

                    #Continuar esta parte

                except ValueError:
                    return None
            #-------------------------------------------------------------------------------
            elif option == "0":
                return None

