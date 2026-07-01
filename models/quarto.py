"""
Model de Quarto
"""


class Quarto:
    TIPOS_VALIDOS = ["simples", "duplo", "suite"]

    def __init__(self, numero: int, tipo: str, preco_diaria: float, disponivel: bool = True):
        self._numero = self._validar_numero(numero)   # sem setter — identidade fixa
        self.tipo = tipo                                # passa pelo setter (valida)
        self.preco_diaria = preco_diaria                # passa pelo setter (valida)
        self.disponivel = disponivel                    # passa pelo setter (normaliza p/ bool)

    # ── numero: identidade do quarto, imutável após a criação ───────
    @property
    def numero(self) -> int:
        return self._numero

    @staticmethod
    def _validar_numero(numero: int) -> int:
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Número do quarto deve ser um inteiro positivo.")
        return numero

    # ── tipo: mutável, restrito à lista de tipos válidos ─────────────
    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, valor: str):
        if valor not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Escolha: {', '.join(self.TIPOS_VALIDOS)}")
        self._tipo = valor

    # ── preco_diaria: mutável, deve ser positivo ─────────────────────
    @property
    def preco_diaria(self) -> float:
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor: float):
        if valor is None or valor <= 0:
            raise ValueError("Preço da diária deve ser maior que zero.")
        self._preco_diaria = float(valor)

    # ── disponivel: mutável, sempre normalizado para bool ────────────
    @property
    def disponivel(self) -> bool:
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor: bool):
        self._disponivel = bool(valor)

    def __repr__(self):
        status = "Disponível" if self._disponivel else "Ocupado"
        return f"Quarto({self._numero} | {self._tipo} | R${self._preco_diaria:.2f} | {status})"