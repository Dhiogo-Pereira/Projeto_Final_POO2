"""
Controller de Alugueis
══════════════════════
Orquestra o fluxo de criação de uma reserva:
1. Selecionar cliente
2. Selecionar quarto disponível
3. Definir período e tipo de serviço
4. Calcular valor e confirmar
5. Persistir no repositório
"""

from models.aluguel import Aluguel
from views.aluguel_view import AluguelView
from views.cliente_view import ClienteView
from views.quarto_view import QuartoView
from views.menu_view import MenuView
from views.gui_utils import confirmar


class AluguelController:
    def __init__(self, data_store):
        self.db = data_store

    def nova_reserva(self) -> bool:

        # 1. Selecionar cliente
        clientes = self.db.listar_clientes()
        if not clientes:
            MenuView.erro("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
            return False

        idx_clt = ClienteView.prompt_selecionar(clientes, "reservar para")
        if idx_clt is None:
            return False
        cliente = clientes[idx_clt]

        # 2. Selecionar quarto disponível
        disponiveis = self.db.listar_quartos_disponiveis()
        if not disponiveis:
            MenuView.erro("Não há quartos disponíveis no momento.")
            return False

        idx_qto = QuartoView.prompt_selecionar(disponiveis, "reservar")
        if idx_qto is None:
            return False
        quarto = disponiveis[idx_qto]

        # 3. Período — trata cancelamento (None) e formato inválido (ValueError)
        try:
            inicio, fim = AluguelView.prompt_datas()
        except (ValueError, TypeError):
            MenuView.erro("Data inválida. Use o formato DD/MM/AAAA.")
            return False

        if inicio is None:          # usuário fechou/cancelou o diálogo
            return False

        # 4. Tipo de serviço — trata cancelamento (None)
        tipo_servico = AluguelView.prompt_tipo_servico()
        if tipo_servico is None:
            return False

        if tipo_servico not in Aluguel.TIPOS_SERVICO:
            MenuView.erro(f"Tipo inválido. Escolha: {', '.join(Aluguel.TIPOS_SERVICO)}")
            return False

        # 5. Criar objeto e exibir resumo
        try:
            # Aluguel(...) valida internamente o tipo de serviço e as
            # datas (data_fim > data_inicio) antes de calcular o valor
            # — ver models/aluguel.py. Todos os campos do objeto criado
            # ficam somente-leitura a partir daqui.
            reserva = Aluguel(cliente, quarto, inicio, fim, tipo_servico)
        except ValueError as e:
            MenuView.erro(str(e))
            return False

        AluguelView.exibir_confirmacao(reserva)

        if not confirmar("Confirmar reserva?"):
            MenuView.info("Reserva cancelada.")
            return False

        # 6. Persistir
        quarto.disponivel = False          # passa pelo setter de Quarto.disponivel
        self.db.adicionar_aluguel(reserva)
        # Antes: cliente.historico.append(reserva) — mexia direto na lista
        # interna do Cliente, furando o encapsulamento (ver models/cliente.py).
        # Agora o próprio Cliente controla como seu histórico é alterado.
        cliente.adicionar_reserva(reserva)
        MenuView.sucesso("Reserva registrada com sucesso.")
        return True

    def listar(self) -> None:
        AluguelView.listar(self.db.listar_alugueis())

    def menu_alugueis(self) -> None:
        while True:
            opcao = AluguelView.menu_alugueis()
            if opcao == "1":
                self.nova_reserva()
            elif opcao == "2":
                self.listar()
            elif opcao == "0":
                break
            else:
                MenuView.erro("Opção inválida.")