"""
Model de Aluguel
────────────────
Representa uma reserva/locação de quarto.
"""

from datetime import date


MULTIPLICADORES = {
    "basico":      1.0,
    "com_servico": 1.3,
    "vip":         1.8,
}


class Aluguel:
    TIPOS_SERVICO = list(MULTIPLICADORES.keys())

    def __init__(
        self,
        cliente,          # instância de Cliente
        quarto,           # instância de Quarto
        data_inicio: date,
        data_fim: date,
        tipo_servico: str = "basico",
    ):
        self._cliente = cliente
        self._quarto = quarto
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._tipo_servico = self._validar_tipo_servico(tipo_servico)
        self._valor = self._calcular_valor()

    # ── Todos os campos são somente-leitura ──────────────────────────
    @property
    def cliente(self):
        return self._cliente

    @property
    def quarto(self):
        return self._quarto

    @property
    def data_inicio(self) -> date:
        return self._data_inicio

    @property
    def data_fim(self) -> date:
        return self._data_fim

    @property
    def tipo_servico(self) -> str:
        return self._tipo_servico

    @property
    def valor(self) -> float:
        return self._valor

    @staticmethod
    def _validar_tipo_servico(tipo: str) -> str:
        if tipo not in MULTIPLICADORES:
            raise ValueError(
                f"Tipo de serviço inválido. Escolha: {', '.join(MULTIPLICADORES.keys())}"
            )
        return tipo

    # ── Lógica de domínio ─────────────────────────────────────────
    def _calcular_valor(self) -> float:
        dias = (self._data_fim - self._data_inicio).days
        if dias <= 0:
            raise ValueError("A data de fim deve ser posterior à data de início.")
        multiplicador = MULTIPLICADORES.get(self._tipo_servico, 1.0)
        return self._quarto.preco_diaria * dias * multiplicador

    @property
    def duracao_dias(self) -> int:
        return (self._data_fim - self._data_inicio).days

    def __repr__(self):
        return (
            f"Aluguel(cliente={self._cliente.nome!r}, "
            f"quarto={self._quarto.numero}, "
            f"valor=R${self._valor:.2f})"
        )