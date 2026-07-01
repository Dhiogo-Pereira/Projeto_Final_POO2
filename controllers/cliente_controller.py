"""
Controller de Clientes
══════════════════════
Lógica de negócio: validação de CPF duplicado, CRUD de clientes.
"""

from models.cliente import Cliente
from views.cliente_view import ClienteView
from views.menu_view import MenuView


class ClienteController:
    def __init__(self, data_store):
        self.db = data_store

    # ── CRUD ──────────────────────────────────────────────────────
    def cadastrar(self) -> bool:
        nome, cpf, email = ClienteView.prompt_cadastro()

        if self.db.buscar_cliente_por_cpf(cpf):
            MenuView.erro(f"Já existe um cliente com o CPF '{cpf}'.")
            return False

        try:
            # Cliente(...) agora valida nome/cpf/email nos seus próprios
            # setters (ver models/cliente.py). Se algo vier inválido —
            # nome vazio, e-mail sem "@" etc. — a classe levanta
            # ValueError em vez de aceitar um estado inconsistente.
            novo = Cliente(nome, cpf, email)
        except ValueError as e:
            MenuView.erro(str(e))
            return False

        self.db.adicionar_cliente(novo)
        MenuView.sucesso(f"Cliente '{nome}' cadastrado com sucesso.")
        return True

    def listar(self) -> None:
        ClienteView.listar(self.db.listar_clientes())

    def deletar(self) -> None:
        clientes = self.db.listar_clientes()
        idx = ClienteView.prompt_selecionar(clientes, "deletar")
        if idx is not None:
            alvo = clientes[idx]
            self.db.remover_cliente(alvo)
            MenuView.sucesso(f"Cliente '{alvo.nome}' removido.")

    # ── Menu de gerenciamento ─────────────────────────────────────
    def menu_gerenciamento(self) -> None:
        while True:
            opcao = ClienteView.menu_gerenciamento()
            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.deletar()
            elif opcao == "0":
                break
            else:
                MenuView.erro("Opção inválida.")