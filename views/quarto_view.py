import tkinter as tk
from tkinter import ttk

from views.gui_utils import informar


class QuartoView:

    # ==========================================================
    # CADASTRO
    # ==========================================================

    @staticmethod
    def prompt_cadastro():

        janela = tk.Toplevel()
        janela.title("Cadastro de Quarto")
        janela.geometry("520x360")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"numero": None, "tipo": None, "preco": None}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Cadastro de Quarto",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=(0, 20))

        # BUG CORRIGIDO: todos os labels agora têm .pack()
        ttk.Label(frame, text="Número do quarto").pack(anchor="w")
        numero = ttk.Entry(frame)
        numero.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="Tipo").pack(anchor="w")
        tipo = ttk.Combobox(
            frame,
            state="readonly",
            values=["simples", "duplo", "suite"]
        )
        tipo.current(0)
        tipo.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="Preço da diária").pack(anchor="w")
        preco = ttk.Entry(frame)
        preco.pack(fill="x", pady=(2, 20))

        def salvar():
            try:
                retorno["numero"] = int(numero.get())
                retorno["tipo"]   = tipo.get()
                retorno["preco"]  = float(preco.get().replace(",", "."))
                janela.destroy()
            except ValueError:
                informar("Número ou preço inválido.", "Erro")

        def cancelar():
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Salvar",   command=salvar).pack(side="right", padx=5)

        numero.focus()
        janela.wait_window()

        return retorno["numero"], retorno["tipo"], retorno["preco"]

    # ==========================================================
    # LISTAGEM
    # ==========================================================

    @staticmethod
    def listar(quartos):

        if not quartos:
            informar("Nenhum quarto cadastrado.")
            return

        janela = tk.Toplevel()
        janela.title("Quartos")
        janela.geometry("760x420")
        janela.grab_set()

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Quartos Cadastrados",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("numero", "tipo", "preco", "status"),
            show="headings"
        )

        tabela.heading("numero", text="Número")
        tabela.heading("tipo",   text="Tipo")
        tabela.heading("preco",  text="Diária")
        tabela.heading("status", text="Situação")

        tabela.column("numero", width=100, anchor="center")
        tabela.column("tipo",   width=150, anchor="center")
        tabela.column("preco",  width=140, anchor="center")
        tabela.column("status", width=150, anchor="center")

        tabela.tag_configure("livre",   foreground="green")
        tabela.tag_configure("ocupado", foreground="red")

        for quarto in quartos:
            status = "🟢 Disponível" if quarto.disponivel else "🔴 Ocupado"
            tag    = "livre"         if quarto.disponivel else "ocupado"
            tabela.insert("", tk.END,
                          values=(quarto.numero, quarto.tipo.capitalize(),
                                  f"R$ {quarto.preco_diaria:.2f}", status),
                          tags=(tag,))

        tabela.pack(fill="both", expand=True)

        ttk.Button(frame, text="Fechar", command=janela.destroy).pack(pady=10)

        janela.wait_window()

    # ==========================================================
    # SELEÇÃO
    # ==========================================================

    @staticmethod
    def prompt_selecionar(quartos, acao="selecionar"):

        if not quartos:
            informar("Nenhum quarto disponível.")
            return None

        janela = tk.Toplevel()
        janela.title("Selecionar Quarto")
        janela.geometry("760x430")
        janela.grab_set()

        retorno = {"indice": None}

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=f"Escolha um quarto para {acao}",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("numero", "tipo", "preco", "status"),
            show="headings"
        )

        tabela.heading("numero", text="Número")
        tabela.heading("tipo",   text="Tipo")
        tabela.heading("preco",  text="Diária")
        tabela.heading("status", text="Situação")

        tabela.column("numero", width=100, anchor="center")
        tabela.column("tipo",   width=150, anchor="center")
        tabela.column("preco",  width=140, anchor="center")
        tabela.column("status", width=150, anchor="center")

        for i, quarto in enumerate(quartos):
            tabela.insert("", tk.END, iid=str(i),
                          values=(quarto.numero, quarto.tipo.capitalize(),
                                  f"R$ {quarto.preco_diaria:.2f}",
                                  "Disponível" if quarto.disponivel else "Ocupado"))

        tabela.pack(fill="both", expand=True)

        def selecionar():
            item = tabela.selection()
            if item:
                retorno["indice"] = int(item[0])
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x", pady=10)

        ttk.Button(botoes, text="Cancelar",   command=janela.destroy).pack(side="right")
        ttk.Button(botoes, text="Selecionar", command=selecionar).pack(side="right", padx=5)

        janela.wait_window()

        return retorno["indice"]

    # ==========================================================
    # MENU
    # ==========================================================

    @staticmethod
    def menu_gerenciamento():

        janela = tk.Toplevel()
        janela.title("Gerenciamento de Quartos")
        janela.geometry("420x280")
        janela.grab_set()

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Gerenciamento de Quartos",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 20))

        def escolher(valor):
            retorno["valor"] = valor
            janela.destroy()

        ttk.Button(frame, text="📋 Listar Quartos",
                   command=lambda: escolher("1")).pack(fill="x", ipady=7, pady=5)
        ttk.Button(frame, text="➕ Cadastrar Quarto",
                   command=lambda: escolher("2")).pack(fill="x", ipady=7, pady=5)

        ttk.Separator(frame).pack(fill="x", pady=15)

        ttk.Button(frame, text="Voltar",
                   command=lambda: escolher("0")).pack(fill="x", ipady=7)

        janela.wait_window()

        return retorno["valor"]