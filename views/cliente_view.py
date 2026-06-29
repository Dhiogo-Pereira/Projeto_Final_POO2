import tkinter as tk
from tkinter import ttk

from views.gui_utils import informar


class ClienteView:

    # ---------------------------------------------------------
    # Cadastro
    # ---------------------------------------------------------

    @staticmethod
    def prompt_cadastro():

        janela = tk.Toplevel()
        janela.title("Cadastro de Cliente")
        janela.geometry("500x340")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"nome": None, "cpf": None, "email": None}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Cadastro de Cliente",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=(0, 20))

        # BUG CORRIGIDO: todos os labels agora têm .pack()
        ttk.Label(frame, text="Nome").pack(anchor="w")
        nome = ttk.Entry(frame)
        nome.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="CPF").pack(anchor="w")
        cpf = ttk.Entry(frame)
        cpf.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="E-mail").pack(anchor="w")
        email = ttk.Entry(frame)
        email.pack(fill="x", pady=(2, 20))

        def cancelar():
            janela.destroy()

        def salvar():
            retorno["nome"]  = nome.get().strip()
            retorno["cpf"]   = cpf.get().strip()
            retorno["email"] = email.get().strip()
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Salvar",   command=salvar).pack(side="right", padx=5)

        nome.focus()
        janela.wait_window()

        return retorno["nome"], retorno["cpf"], retorno["email"]

    # ---------------------------------------------------------
    # Listagem
    # ---------------------------------------------------------

    @staticmethod
    def listar(clientes):

        if not clientes:
            informar("Nenhum cliente cadastrado.")
            return

        janela = tk.Toplevel()
        janela.title("Clientes")
        janela.geometry("700x400")
        janela.grab_set()

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Clientes Cadastrados",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("nome", "cpf", "email"),
            show="headings"
        )

        tabela.heading("nome",  text="Nome")
        tabela.heading("cpf",   text="CPF")
        tabela.heading("email", text="E-mail")

        tabela.column("nome",  width=220)
        tabela.column("cpf",   width=160)
        tabela.column("email", width=250)

        for cliente in clientes:
            tabela.insert("", tk.END, values=(cliente.nome, cliente.cpf, cliente.email))

        tabela.pack(fill="both", expand=True)

        ttk.Button(frame, text="Fechar", command=janela.destroy).pack(pady=10)

        janela.wait_window()

    # ---------------------------------------------------------
    # Seleção
    # ---------------------------------------------------------

    @staticmethod
    def prompt_selecionar(clientes, acao="selecionar"):

        if not clientes:
            informar("Nenhum cliente cadastrado.")
            return None

        janela = tk.Toplevel()
        janela.title(f"{acao.capitalize()} Cliente")
        janela.geometry("700x420")
        janela.grab_set()

        retorno = {"indice": None}

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=f"Escolha um cliente para {acao}",
            font=("Segoe UI", 13, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("nome", "cpf", "email"),
            show="headings"
        )

        tabela.heading("nome",  text="Nome")
        tabela.heading("cpf",   text="CPF")
        tabela.heading("email", text="E-mail")

        tabela.column("nome",  width=220)
        tabela.column("cpf",   width=160)
        tabela.column("email", width=250)

        for i, cliente in enumerate(clientes):
            tabela.insert("", tk.END, iid=str(i),
                          values=(cliente.nome, cliente.cpf, cliente.email))

        tabela.pack(fill="both", expand=True)

        def confirmar():
            selecionado = tabela.selection()
            if selecionado:
                retorno["indice"] = int(selecionado[0])
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x", pady=10)

        ttk.Button(botoes, text="Cancelar",   command=janela.destroy).pack(side="right")
        ttk.Button(botoes, text="Selecionar", command=confirmar).pack(side="right", padx=5)

        janela.wait_window()

        return retorno["indice"]

    # ---------------------------------------------------------
    # Menu
    # ---------------------------------------------------------

    @staticmethod
    def menu_gerenciamento():

        janela = tk.Toplevel()
        janela.title("Gerenciamento de Clientes")
        janela.geometry("400x300")
        janela.grab_set()

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Gerenciamento",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 20))

        def escolher(valor):
            retorno["valor"] = valor
            janela.destroy()

        ttk.Button(frame, text="Listar Clientes",
                   command=lambda: escolher("1")).pack(fill="x", ipady=6, pady=5)
        ttk.Button(frame, text="Excluir Cliente",
                   command=lambda: escolher("2")).pack(fill="x", ipady=6, pady=5)

        ttk.Separator(frame).pack(fill="x", pady=15)

        ttk.Button(frame, text="Voltar",
                   command=lambda: escolher("0")).pack(fill="x", ipady=6)

        janela.wait_window()

        return retorno["valor"]