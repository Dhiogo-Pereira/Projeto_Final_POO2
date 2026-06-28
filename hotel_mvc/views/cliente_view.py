"""
View de Clientes
════════════════
Toda interação visual relacionada ao cadastro e gestão de clientes.
"""

LINHA = "─" * 42


class ClienteView:

    # ── Prompts de entrada ────────────────────────────────────────
    @staticmethod
    def prompt_cadastro() -> tuple[str, str, str]:
        print("\n─── Cadastro de Cliente ───")
        nome  = input("Nome:  ").strip().title()
        cpf   = input("CPF:   ").strip()
        email = input("Email: ").strip()
        return nome, cpf, email

    # ── Listagem ──────────────────────────────────────────────────
    @staticmethod
    def listar(clientes: list) -> None:
        print(f"\n{LINHA}")
        print("  CLIENTES CADASTRADOS")
        print(LINHA)
        if not clientes:
            print("  Nenhum cliente cadastrado.")
            return
        for i, c in enumerate(clientes, 1):
            print(f"  {i:>2}) {c.nome:<20} CPF: {c.cpf:<14} {c.email}")

    @staticmethod
    def prompt_selecionar(clientes: list, acao: str = "selecionar"):
        """Exibe a lista e retorna o índice escolhido (base-0), ou None."""
        ClienteView.listar(clientes)
        if not clientes:
            return None
        try:
            idx = int(input(f"\nNúmero para {acao} (0 = cancelar): ")) - 1
            if 0 <= idx < len(clientes):
                return idx
        except ValueError:
            pass
        return None

    # ── Sub-menus ─────────────────────────────────────────────────
    @staticmethod
    def menu_gerenciamento() -> str:
        print("\n─── Gerenciamento de Clientes ───")
        print("  1) Listar")
        print("  2) Deletar")
        print("  0) Voltar")
        return input("\n> ").strip()
