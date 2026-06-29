import tkinter as tk
from tkinter import ttk
from datetime import datetime

from views.gui_utils import get_root, informar


class AluguelView:

    # ==========================================================
    # Datas
    # ==========================================================

    @staticmethod
    def prompt_datas():
        """
        Retorna (date, date) ou (None, None) se o usuário cancelar.
        Levanta ValueError se o formato de data for inválido
        (o controller trata esse caso).
        """
        get_root()

        janela = tk.Toplevel()
        janela.title("Período da Reserva")
        janela.geometry("420x250")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"inicio": None, "fim": None, "confirmado": False}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Período da Reserva",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 15))

        ttk.Label(frame, text="Data de entrada  (DD/MM/AAAA)").pack(anchor="w")
        entrada = ttk.Entry(frame)
        entrada.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="Data de saída  (DD/MM/AAAA)").pack(anchor="w")
        saida = ttk.Entry(frame)
        saida.pack(fill="x", pady=(2, 20))

        def salvar():
            # Pode levantar ValueError — capturado pelo controller
            retorno["inicio"] = datetime.strptime(
                entrada.get().strip(), "%d/%m/%Y"
            ).date()
            retorno["fim"] = datetime.strptime(
                saida.get().strip(), "%d/%m/%Y"
            ).date()
            retorno["confirmado"] = True
            janela.destroy()

        def cancelar():
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Confirmar", command=salvar).pack(side="right", padx=5)

        entrada.focus()
        saida.bind("<Return>", lambda e: salvar())
        janela.protocol("WM_DELETE_WINDOW", cancelar)
        janela.wait_window()

        return retorno["inicio"], retorno["fim"]

    # ==========================================================
    # Tipo de serviço
    # ==========================================================

    @staticmethod
    def prompt_tipo_servico():
        """Retorna a string do tipo ou None se cancelado."""
        get_root()

        janela = tk.Toplevel()
        janela.title("Tipo de Serviço")
        janela.geometry("380x210")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"tipo": None}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Tipo de Serviço",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 8))

        ttk.Label(
            frame,
            text="básico · com_servico (+30%) · vip (+80%)",
            foreground="gray"
        ).pack(pady=(0, 15))

        combo = ttk.Combobox(
            frame,
            values=["basico", "com_servico", "vip"],
            state="readonly"
        )
        combo.current(0)
        combo.pack(fill="x", pady=(0, 20))

        def confirmar():
            retorno["tipo"] = combo.get()
            janela.destroy()

        def cancelar():
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Confirmar", command=confirmar).pack(side="right", padx=5)

        janela.protocol("WM_DELETE_WINDOW", cancelar)
        janela.wait_window()

        return retorno["tipo"]

    # ==========================================================
    # Confirmação de reserva
    # ==========================================================

    @staticmethod
    def exibir_confirmacao(aluguel):
        informar(
            f"Cliente : {aluguel.cliente.nome}\n"
            f"Quarto  : {aluguel.quarto.numero}\n"
            f"Entrada : {aluguel.data_inicio.strftime('%d/%m/%Y')}\n"
            f"Saída   : {aluguel.data_fim.strftime('%d/%m/%Y')}\n"
            f"Duração : {aluguel.duracao_dias} dia(s)\n"
            f"Serviço : {aluguel.tipo_servico}\n"
            f"Valor   : R$ {aluguel.valor:.2f}",
            "Resumo da Reserva"
        )

    # ==========================================================
    # Listagem
    # ==========================================================

    @staticmethod
    def listar(alugueis):

        if not alugueis:
            informar("Nenhum aluguel registrado.")
            return

        janela = tk.Toplevel()
        janela.title("Reservas")
        janela.geometry("820x420")
        janela.grab_set()

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Reservas Registradas",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 10))

        colunas = ("cliente", "quarto", "entrada", "saida", "servico", "valor")

        tabela = ttk.Treeview(frame, columns=colunas, show="headings")

        tabela.heading("cliente",  text="Cliente")
        tabela.heading("quarto",   text="Quarto")
        tabela.heading("entrada",  text="Entrada")
        tabela.heading("saida",    text="Saída")
        tabela.heading("servico",  text="Serviço")
        tabela.heading("valor",    text="Valor")

        tabela.column("cliente",  width=200)
        tabela.column("quarto",   width=70,  anchor="center")
        tabela.column("entrada",  width=100, anchor="center")
        tabela.column("saida",    width=100, anchor="center")
        tabela.column("servico",  width=110, anchor="center")
        tabela.column("valor",    width=110, anchor="center")

        for a in alugueis:
            tabela.insert(
                "",
                tk.END,
                values=(
                    a.cliente.nome,
                    a.quarto.numero,
                    a.data_inicio.strftime("%d/%m/%Y"),
                    a.data_fim.strftime("%d/%m/%Y"),
                    a.tipo_servico,
                    f"R$ {a.valor:.2f}",
                )
            )

        tabela.pack(fill="both", expand=True)

        ttk.Button(
            frame,
            text="Fechar",
            command=janela.destroy
        ).pack(pady=10)

        janela.wait_window()

    # ==========================================================
    # Menu
    # ==========================================================

    @staticmethod
    def menu_alugueis():

        get_root()

        janela = tk.Toplevel()
        janela.title("Reservas")
        janela.geometry("400x260")
        janela.grab_set()

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Gerenciamento de Reservas",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 20))

        def escolher(valor):
            retorno["valor"] = valor
            janela.destroy()

        ttk.Button(
            frame,
            text="➕ Nova Reserva",
            command=lambda: escolher("1")
        ).pack(fill="x", ipady=7, pady=5)

        ttk.Button(
            frame,
            text="📋 Listar Reservas",
            command=lambda: escolher("2")
        ).pack(fill="x", ipady=7, pady=5)

        ttk.Separator(frame).pack(fill="x", pady=15)

        ttk.Button(
            frame,
            text="Voltar",
            command=lambda: escolher("0")
        ).pack(fill="x", ipady=7)

        janela.wait_window()

        return retorno["valor"]