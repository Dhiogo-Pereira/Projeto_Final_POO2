"""
View de Quartos
═══════════════
"""

LINHA = "─" * 42


class QuartoView:

    @staticmethod
    def prompt_cadastro() -> tuple[int, str, float]:
        print("\n─── Cadastro de Quarto ───")
        numero = int(input("Número do quarto: ").strip())
        print("Tipos disponíveis: simples | duplo | suite")
        tipo = input("Tipo: ").strip().lower()
        preco = float(input("Preço por diária (R$): ").strip().replace(",", "."))
        return numero, tipo, preco

    @staticmethod
    def listar(quartos: list) -> None:
        print(f"\n{LINHA}")
        print("  QUARTOS")
        print(LINHA)
        if not quartos:
            print("  Nenhum quarto cadastrado.")
            return
        for i, q in enumerate(quartos, 1):
            status = "Disponível" if q.disponivel else "Ocupado   "
            print(f"  {i:>2}) Nº {q.numero:<4} | {q.tipo:<8} | R${q.preco_diaria:>8.2f} | {status}")

    @staticmethod
    def prompt_selecionar(quartos: list, acao: str = "selecionar"):
        QuartoView.listar(quartos)
        if not quartos:
            return None
        try:
            idx = int(input(f"\nNúmero para {acao} (0 = cancelar): ")) - 1
            if 0 <= idx < len(quartos):
                return idx
        except ValueError:
            pass
        return None

    @staticmethod
    def menu_gerenciamento() -> str:
        print("\n─── Gerenciamento de Quartos ───")
        print("  1) Listar quartos")
        print("  2) Cadastrar quarto")
        print("  0) Voltar")
        return input("\n> ").strip()
