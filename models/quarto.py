"""
Model de Quarto
───────────────
Representa um quarto físico do hotel.
`disponivel` será gerenciado pelo AluguelController.
"""


class Quarto:
    TIPOS_VALIDOS = ["simples", "duplo", "suite"]

    def __init__(self, numero: int, tipo: str, preco_diaria: float, disponivel: bool = True):
        self.numero = numero
        self.tipo = tipo                    # simples | duplo | suite
        self.preco_diaria = preco_diaria
        self.disponivel = disponivel

    def __repr__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto({self.numero} | {self.tipo} | R${self.preco_diaria:.2f} | {status})"
