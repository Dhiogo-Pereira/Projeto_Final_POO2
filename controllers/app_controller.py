"""
Controller Principal — AppController
══════════════════════════════════════
Orquestra todos os controllers e define o fluxo da aplicação.
É o único arquivo que conhece todos os outros controllers.

Fluxo:
  run()
    └─ _garantir_gerente()       # Modo config se não houver gerente
    └─ loop: menu_inicial()
         └─ login()
              └─ _menu_principal(usuario)
"""

from models.usuario import Gerente
from controllers.auth_controller import AuthController
from controllers.funcionario_controller import FuncionarioController
from controllers.cliente_controller import ClienteController
from controllers.quarto_controller import QuartoController
from controllers.aluguel_controller import AluguelController
from views.menu_view import MenuView


class AppController:
    def __init__(self, data_store):
        self.db = data_store
        # Instancia todos os controllers passando o mesmo data_store
        self.auth     = AuthController(data_store)
        self.func     = FuncionarioController(data_store)
        self.cliente  = ClienteController(data_store)
        self.quarto   = QuartoController(data_store)
        self.aluguel  = AluguelController(data_store)

    # ── Inicialização ─────────────────────────────────────────────
    def _garantir_gerente(self) -> None:
        """
        Verifica se há pelo menos um gerente cadastrado.
        Se não houver, entra em modo de configuração inicial e
        força o cadastro de um gerente antes de continuar.
        """
        tem_gerente = any(
            isinstance(f, Gerente)
            for f in self.db.listar_funcionarios()
        )
        if not tem_gerente:
            MenuView.cabecalho("CONFIGURAÇÃO INICIAL DO SISTEMA")
            MenuView.info("Nenhum gerente encontrado.")
            MenuView.info("Crie uma conta de gerente para continuar.\n")
            while not self.func.cadastrar(modo_config=True):
                MenuView.erro("Tente novamente.")

    # ── Menu principal pós-login ──────────────────────────────────
    def _menu_principal(self, usuario) -> None:
        is_gerente = isinstance(usuario, Gerente) # Ele retorna se o objeto usuario é instância da classe Gerente
        while True:
            opcao = MenuView.menu_principal(is_gerente) # Chama o menu passando como parâmetro o valor bool obtido acima

            if opcao == "1":
                self.cliente.cadastrar()
            elif opcao == "2":
                self.aluguel.menu_alugueis()
            elif opcao == "3":
                self.cliente.menu_gerenciamento()
            elif opcao == "4":
                self.quarto.menu_gerenciamento()
            elif opcao == "5" and is_gerente:
                self.func.cadastrar()
            elif opcao == "6" and is_gerente:
                self.func.menu_gerenciamento()
            elif opcao == "0":
                MenuView.info(f"Logout. Até logo, {usuario.nome}!")
                break
            else:
                MenuView.erro("Opção inválida.")

    # ── Entry point ───────────────────────────────────────────────
    def run(self) -> None:
        self._garantir_gerente()
        while True:
            opcao = MenuView.menu_inicial()
            if opcao == "1":
                usuario = self.auth.login()
                if usuario:
                    self._menu_principal(usuario)
            elif opcao == "0":
                MenuView.info("Encerrando sistema. Até logo!")
                break
            else:
                MenuView.erro("Opção inválida.")
