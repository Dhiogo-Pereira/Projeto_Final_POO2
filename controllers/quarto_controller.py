"""
Controller de Quartos
═════════════════════
"""

from models.quarto import Quarto
from views.quarto_view import QuartoView
from views.menu_view import MenuView


class QuartoController:
    def __init__(self, data_store):
        self.db = data_store

    def cadastrar(self) -> bool:
        try:
            numero, tipo, preco = QuartoView.prompt_cadastro()
        except ValueError:
            MenuView.erro("Valor inválido. Operação cancelada.")
            return False

        if tipo not in Quarto.TIPOS_VALIDOS:
            MenuView.erro(f"Tipo inválido. Escolha: {', '.join(Quarto.TIPOS_VALIDOS)}")
            return False

        # Verificar número duplicado
        for q in self.db.listar_quartos():
            if q.numero == numero:
                MenuView.erro(f"Quarto {numero} já existe.")
                return False

        novo = Quarto(numero, tipo, preco)
        self.db.adicionar_quarto(novo)
        MenuView.sucesso(f"Quarto {numero} ({tipo}) cadastrado. Diária: R$ {preco:.2f}")
        return True

    def listar(self) -> None:
        QuartoView.listar(self.db.listar_quartos())

    def menu_gerenciamento(self) -> None:
        while True:
            opcao = QuartoView.menu_gerenciamento()
            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.cadastrar()
            elif opcao == "0":
                break
            else:
                MenuView.erro("Opção inválida.")
