"""
View de Funcionários
════════════════════
Toda interação visual relacionada ao cadastro e gestão de funcionários.
"""

LINHA = "─" * 42


class FuncionarioView:

    # ── Prompts de entrada ────────────────────────────────────────
    @staticmethod
    def prompt_cadastro() -> tuple[str, str]:
        print("\n─── Cadastro de Funcionário ───")
        nome = input("Nome:  ").strip().title()
        cpf  = input("CPF:   ").strip()
        return nome, cpf

    @staticmethod
    def prompt_senha() -> tuple[str, str]:
        """Retorna (senha, confirmacao) — validação fica no controller."""
        senha    = input("Senha:          ").strip()
        confirma = input("Confirme senha: ").strip()
        return senha, confirma

    @staticmethod
    def prompt_tipo() -> str:
        """Solicita o tipo de conta. Retorna string bruta — validação no controller."""
        return input("Tipo (gerente/funcionario): ").strip().lower()

    @staticmethod
    def prompt_novo_nome(nome_atual: str) -> str:
        return input(f"Novo nome [{nome_atual}] (Enter = manter): ").strip().title()

    # ── Listagem ──────────────────────────────────────────────────
    @staticmethod
    def listar(funcionarios: list) -> None:
        print(f"\n{LINHA}")
        print("  FUNCIONÁRIOS CADASTRADOS")
        print(LINHA)
        if not funcionarios:
            print("  Nenhum funcionário cadastrado.")
            return
        for i, f in enumerate(funcionarios, 1):
            print(f"  {i:>2}) {f.nome:<20} CPF: {f.cpf:<14} [{f.tipo}]")

    @staticmethod
    def prompt_selecionar(funcionarios: list, acao: str = "selecionar"):
        """Exibe a lista e retorna o índice escolhido (base-0), ou None."""
        FuncionarioView.listar(funcionarios)
        if not funcionarios:
            return None
        try:
            idx = int(input(f"\nNúmero para {acao} (0 = cancelar): ")) - 1
            if 0 <= idx < len(funcionarios):
                return idx
        except ValueError:
            pass
        return None

    # ── Sub-menus ─────────────────────────────────────────────────
    @staticmethod
    def menu_gerenciamento() -> str:
        print("\n─── Gerenciamento de Funcionários ───")
        print("  1) Listar")
        print("  2) Deletar")
        print("  3) Editar nome")
        print("  0) Voltar")
        return input("\n> ").strip()
