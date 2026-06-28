"""
Model de Cliente
────────────────
Representa um hóspede do hotel.
O campo `historico` armazena referências a objetos Aluguel;
quando houver banco de dados, substituir por IDs/chaves estrangeiras.
"""


class Cliente:
    def __init__(self, nome: str, cpf: str, email: str = "", historico=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.historico: list = historico if historico is not None else []

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, cpf={self.cpf!r})"
