"""
View de Menus Gerais
════════════════════
Responsabilidade exclusiva: exibir menus e coletar a escolha do
usuário. ZERO lógica de negócio aqui.

┌──────────────────────────────────────────────────────────────┐
│  COMO ADICIONAR INTERFACE GRÁFICA (Tkinter, PyQt, etc.):     │
│                                                              │
│  1. Crie MenuViewGUI com os mesmos métodos desta classe.     │
│  2. Em main.py, passe MenuViewGUI() para os controllers.     │
│  3. Os controllers não precisam saber qual view está ativa.  │
└──────────────────────────────────────────────────────────────┘
"""

LINHA = "─" * 42


class MenuView:

    # ── Helpers visuais ───────────────────────────────────────────
    @staticmethod
    def cabecalho(titulo: str) -> None:
        print(f"\n{LINHA}")
        print(f"  {titulo}")
        print(LINHA)

    @staticmethod
    def info(texto: str) -> None:
        print(f"[INFO] {texto}")

    @staticmethod
    def erro(texto: str) -> None:
        print(f"[ERRO] {texto}")

    @staticmethod
    def sucesso(texto: str) -> None:
        print(f"[ OK ] {texto}")

    # ── Menus de navegação ────────────────────────────────────────
    @staticmethod
    def menu_inicial() -> str:
        MenuView.cabecalho("SISTEMA DE GERENCIAMENTO HOTELEIRO")
        print("  1) Login")
        print("  0) Sair")
        return input("\n> ").strip()

    @staticmethod
    def menu_principal(is_gerente: bool = False) -> str:
        MenuView.cabecalho("MENU PRINCIPAL")
        print("  1) Cadastrar Cliente")
        print("  2) Processar Aluguel")
        print("  3) Gerenciar Clientes")
        print("  4) Gerenciar Quartos")
        if is_gerente:
            print("  5) Cadastrar Funcionário")
            print("  6) Gerenciar Funcionários")
        print("  0) Logout")
        return input("\n> ").strip()
