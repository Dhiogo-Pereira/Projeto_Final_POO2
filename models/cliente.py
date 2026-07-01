"""
Model de Cliente
────────────────
Representa um hóspede do hotel.
"""


class Cliente:
    def __init__(self, nome: str, cpf: str, email: str = "", historico=None):
        self.nome = nome                          # passa pelo setter (valida)
        self._cpf = self._validar_cpf(cpf)          # sem setter — identidade fixa
        self.email = email                          # passa pelo setter (valida)
        self._historico: list = list(historico) if historico is not None else []

    # ── nome: mutável, validado ─────────────────────────────────────
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome do cliente não pode ser vazio.")
        self._nome = valor.strip()

    # ── cpf: identidade do registro, imutável após a criação ────────
    @property
    def cpf(self) -> str:
        return self._cpf

    @staticmethod
    def _validar_cpf(cpf: str) -> str:
        if not cpf or not cpf.strip():
            raise ValueError("CPF do cliente não pode ser vazio.")
        return cpf.strip()

    # ── email: mutável, validação simples de formato ─────────────────
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        valor = (valor or "").strip()
        if valor and "@" not in valor:
            raise ValueError("E-mail inválido.")
        self._email = valor

    @property
    def historico(self) -> tuple:
        """Retorna uma cópia imutável — protege a lista interna de mutação externa."""
        return tuple(self._historico)

    def adicionar_reserva(self, aluguel) -> None:
        """Único ponto de entrada para registrar uma reserva no histórico do cliente."""
        self._historico.append(aluguel)

    def __repr__(self):
        return f"Cliente(nome={self._nome!r}, cpf={self._cpf!r})"