"""
Model de Aluguel
────────────────
Representa uma reserva/locação de quarto.
O cálculo de valor fica aqui porque é uma regra de negócio
intrínseca ao dado — não depende de entrada do usuário nem de
persistência, apenas dos atributos do próprio objeto.
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
        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo_servico = tipo_servico
        self.valor = self._calcular_valor()

    # ── Lógica de domínio ─────────────────────────────────────────
    def _calcular_valor(self) -> float:
        dias = (self.data_fim - self.data_inicio).days
        if dias <= 0:
            raise ValueError("A data de fim deve ser posterior à data de início.")
        multiplicador = MULTIPLICADORES.get(self.tipo_servico, 1.0)
        return self.quarto.preco_diaria * dias * multiplicador

    @property
    def duracao_dias(self) -> int:
        return (self.data_fim - self.data_inicio).days

    def __repr__(self):
        return (
            f"Aluguel(cliente={self.cliente.nome!r}, "
            f"quarto={self.quarto.numero}, "
            f"valor=R${self.valor:.2f})"
        )
