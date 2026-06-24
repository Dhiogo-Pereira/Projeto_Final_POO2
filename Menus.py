
from Cliente import Clientes as Cfile
from Funcionario import Funcionarios as Ffile
from Login import login

#Banco de dados temporario




class Stm_Menus:
    def __init__(self):
        self.funcionarios = []
        self.clientes = []
        self.quartos = []


    def menu_funcionario(self):

        print("Menu Temporario 1:")
        print("1) Login")
        print("2) Cadastro de pessoa")
        print("0) Sair")

        option = str(input(">"))
        if option == "1":
            login(None)

        elif option == "2":
            Ffile.cadastro_func(None, self.clientes)

        elif option == "3":
            return


    def menu_programa(self):
        pass