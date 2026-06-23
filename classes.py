

# Classe para os diferentes usuarios
class Usuario:
    def __init__(self, nome, senha, email, tipo):
        self.nome = nome    #nome do funcionario
        self.senha = senha  #senha do funcionario
        self.email = email  #email do funcionario
        self.tipo = tipo    #variavel que diferencia gerentes de funcionarios
#================================================


# Classe para os clientes
class Cliente:
    def __init__(self, nome, cpf, email, historico):
        self.nome = nome           #nome do cliente
        self.cpf = cpf             #cpf do cliente
        self.email = email         #email do cliente
        self.historico = historico #lista com toda a história de alugueis do cliente
#================================================

# Classe para os quartos no hotel
class deals:
    def __init__(self, cliente, quarto, tempo, valor, tipo, DataInicio, DataFinal):
        self.cliente = cliente   #Cliente que fez a reserva
        self.quarto = quarto     #Quarto reservado
        self.tempo = tempo       #Tempo da reserva
        self.tipo = tipo         #Se reserva é basica, com serviço de quarto ou com serviço vip
        self.valor = valor       #Valor final da transação
        self.start = DataInicio  #Data da reserva
        self.end = DataFinal     #Data de entrega do quarto
#================================================