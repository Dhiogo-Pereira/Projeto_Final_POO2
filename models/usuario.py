"""
Models de Usuário
─────────────────
Contém as classes de domínio para os tipos de usuário do sistema.
Não possuem lógica de negócio nem acesso a dados — são apenas
representações dos dados.

Para adicionar campos novos (ex.: telefone), basta acrescentá-los
aqui sem mexer em nenhuma outra camada.
"""


class Funcionario:
    """Funcionário padrão do hotel. Acesso restrito às operações básicas."""

    def __init__(self, nome: str, cpf: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.tipo = "funcionario"

    def __repr__(self):
        return f"Funcionario(nome={self.nome!r}, cpf={self.cpf!r})"


class Gerente(Funcionario):
    """Gerente do hotel. Possui acesso total, incluindo gestão de funcionários."""

    def __init__(self, nome: str, cpf: str, senha: str):
        super().__init__(nome, cpf, senha)
        self.tipo = "gerente"

    def __repr__(self):
        return f"Gerente(nome={self.nome!r}, cpf={self.cpf!r})"
