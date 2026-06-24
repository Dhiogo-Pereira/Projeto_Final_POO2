
from Cliente import Clientes as C
from Funcionario import Funcionarios as F
from Funcionario import Gerente as G
from Login import login

class Stm_Menus:

    def menu_funcionario(self):
        #====================================================================================
        Juan = G("Juan", "NUMERO", "123Mamaco^^")

        # Banco de dados temporario
        clientes = {"Joselina": {"Nome": "Joselina", "CPF": "NUMERO", "Historico": []}}
        quartos = {}
        alugueis = {}
        funcionarios = [{"Juan": Juan}]
        #=====================================================================================
        # Informação do banco de dados
        #=====================================================================================

        while True:
            mode = None                    #
            for l in funcionarios:         # Ve se a lista tem um gerente
                value = list(l.values())   #
                for k in value:
                    if type(k) == G:           # Se não tiver, entra no modo
                        mode = "tem gerente"   # configuração de sistema.

            if mode != "tem gerente":
                print("\n\nEntrando no modo configuração:")
                Func_com_gerente = Stm_Menus.config(None,funcionarios)
                funcionarios = Func_com_gerente
            else: break
        #--------------------------------------------------------------
        print("Menu Temporario 1:")
        print("1) Login")
        print("0) Sair")

        option = str(input(">"))
        if option == "1":
            login(funcionarios)
        elif option == "0":
            return

    # ==============================================================================================
    def config(self, funcionarios):             # Gera uma conta gerente para se fazer login
        print("\nCriando conta gerente:")       # (Pois apenas gerentes podem criar funcionarios novos)
        while True:
            lista_func = G.cadastro_func(None, funcionarios, True)
            if lista_func != None:
                return lista_func

    # ==============================================================================================
    def menu_programa(self):
        pass
