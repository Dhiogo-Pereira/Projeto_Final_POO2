"""
View de Alugueis
════════════════
"""

from datetime import date

LINHA = "─" * 42


class AluguelView:

    @staticmethod
    def prompt_datas() -> tuple[date, date]:
        print("\n─── Período de Reserva ───")
        print("Formato de data: DD/MM/AAAA")
        inicio_str = input("Data de início: ").strip()
        fim_str    = input("Data de saída:  ").strip()
        inicio = date(*reversed([int(p) for p in inicio_str.split("/")]))
        fim    = date(*reversed([int(p) for p in fim_str.split("/")]))
        return inicio, fim

    @staticmethod
    def prompt_tipo_servico() -> str:
        print("\nTipo de serviço:")
        print("  basico       — sem serviços adicionais")
        print("  com_servico  — serviço de quarto incluído (+30%)")
        print("  vip          — serviço completo (+80%)")
        return input("Escolha: ").strip().lower()

    @staticmethod
    def exibir_confirmacao(aluguel) -> None:
        print(f"\n{LINHA}")
        print("  RESUMO DA RESERVA")
        print(LINHA)
        print(f"  Cliente:    {aluguel.cliente.nome}")
        print(f"  Quarto:     {aluguel.quarto.numero} ({aluguel.quarto.tipo})")
        print(f"  Entrada:    {aluguel.data_inicio.strftime('%d/%m/%Y')}")
        print(f"  Saída:      {aluguel.data_fim.strftime('%d/%m/%Y')}")
        print(f"  Duração:    {aluguel.duracao_dias} dia(s)")
        print(f"  Serviço:    {aluguel.tipo_servico}")
        print(f"  Valor:      R$ {aluguel.valor:.2f}")

    @staticmethod
    def listar(alugueis: list) -> None:
        print(f"\n{LINHA}")
        print("  ALUGUEIS")
        print(LINHA)
        if not alugueis:
            print("  Nenhum aluguel registrado.")
            return
        for i, a in enumerate(alugueis, 1):
            print(
                f"  {i:>2}) {a.cliente.nome:<18} "
                f"Qto {a.quarto.numero} | "
                f"{a.data_inicio} → {a.data_fim} | "
                f"R$ {a.valor:.2f}"
            )

    @staticmethod
    def menu_alugueis() -> str:
        print("\n─── Alugueis ───")
        print("  1) Nova reserva")
        print("  2) Listar reservas")
        print("  0) Voltar")
        return input("\n> ").strip()
