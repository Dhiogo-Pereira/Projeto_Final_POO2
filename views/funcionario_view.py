import tkinter as tk
from tkinter import ttk

from views.gui_utils import informar, perguntar


class FuncionarioView:

    # ==========================================================
    # Cadastro
    # ==========================================================

    @staticmethod
    def prompt_cadastro():

        janela = tk.Toplevel()
        janela.title("Cadastro de Funcionário")
        janela.geometry("500x280")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"nome": None, "cpf": None}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Cadastro de Funcionário",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=(0, 20))

        # BUG CORRIGIDO: labels agora têm .pack()
        ttk.Label(frame, text="Nome").pack(anchor="w")
        nome = ttk.Entry(frame)
        nome.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="CPF").pack(anchor="w")
        cpf = ttk.Entry(frame)
        cpf.pack(fill="x", pady=(2, 20))

        def salvar():
            retorno["nome"] = nome.get().strip()
            retorno["cpf"] = cpf.get().strip()
            janela.destroy()

        def cancelar():
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Próximo", command=salvar).pack(side="right", padx=5)

        nome.focus()
        janela.wait_window()

        return retorno["nome"], retorno["cpf"]

    # ==========================================================
    # Senha
    # ==========================================================

    @staticmethod
    def prompt_senha():

        janela = tk.Toplevel()
        janela.title("Definir Senha")
        janela.geometry("500x290")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"senha": None, "confirma": None}
        mostrar = tk.BooleanVar(value=False)

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Defina a senha",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 15))

        # BUG CORRIGIDO: labels agora têm .pack()
        ttk.Label(frame, text="Senha").pack(anchor="w")
        senha = ttk.Entry(frame, show="•")
        senha.pack(fill="x", pady=(2, 10))

        ttk.Label(frame, text="Confirmar senha").pack(anchor="w")
        confirma = ttk.Entry(frame, show="•")
        confirma.pack(fill="x", pady=(2, 10))

        def alternar():
            char = "" if mostrar.get() else "•"
            senha.configure(show=char)
            confirma.configure(show=char)

        ttk.Checkbutton(
            frame,
            text="Mostrar senha",
            variable=mostrar,
            command=alternar
        ).pack(anchor="w", pady=(5, 15))

        def salvar():
            retorno["senha"] = senha.get()
            retorno["confirma"] = confirma.get()
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=janela.destroy).pack(side="right")
        ttk.Button(botoes, text="Salvar", command=salvar).pack(side="right", padx=5)

        senha.focus()
        janela.wait_window()

        return retorno["senha"], retorno["confirma"]

    # ==========================================================
    # Tipo
    # ==========================================================

    @staticmethod
    def prompt_tipo():

        janela = tk.Toplevel()
        janela.title("Tipo de Conta")
        janela.geometry("420x200")
        janela.resizable(False, False)
        janela.grab_set()

        retorno = {"tipo": "funcionario"}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Tipo de Funcionário",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 15))

        combo = ttk.Combobox(
            frame,
            values=["funcionario", "gerente"],
            state="readonly"
        )
        combo.current(0)
        combo.pack(fill="x")

        def confirmar():
            retorno["tipo"] = combo.get()
            janela.destroy()

        ttk.Button(frame, text="Confirmar", command=confirmar).pack(pady=20)

        janela.wait_window()

        return retorno["tipo"]

    # ==========================================================
    # Editar nome
    # ==========================================================

    @staticmethod
    def prompt_novo_nome(nome_atual):
        return perguntar(f"Novo nome [{nome_atual}]:")

    # ==========================================================
    # Listagem
    # ==========================================================

    @staticmethod
    def listar(funcionarios):

        if not funcionarios:
            informar("Nenhum funcionário cadastrado.")
            return

        janela = tk.Toplevel()
        janela.title("Funcionários")
        janela.geometry("660x420")
        janela.grab_set()

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Funcionários Cadastrados",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("nome", "cpf", "tipo"),
            show="headings"
        )

        tabela.heading("nome", text="Nome")
        tabela.heading("cpf", text="CPF")
        tabela.heading("tipo", text="Tipo")

        tabela.column("nome", width=260)
        tabela.column("cpf", width=180)
        tabela.column("tipo", width=140, anchor="center")

        for func in funcionarios:
            tabela.insert(
                "",
                tk.END,
                values=(func.nome, func.cpf, func.tipo.capitalize())
            )

        tabela.pack(fill="both", expand=True)

        ttk.Button(
            frame,
            text="Fechar",
            command=janela.destroy
        ).pack(pady=10)

        janela.wait_window()

    # ==========================================================
    # Seleção  ← CORRIGIDO: usa Treeview igual a cliente_view
    # ==========================================================

    @staticmethod
    def prompt_selecionar(funcionarios, acao="selecionar"):

        if not funcionarios:
            informar("Nenhum funcionário cadastrado.")
            return None

        janela = tk.Toplevel()
        janela.title(f"{acao.capitalize()} Funcionário")
        janela.geometry("660x420")
        janela.grab_set()

        retorno = {"indice": None}

        frame = ttk.Frame(janela, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=f"Escolha um funcionário para {acao}",
            font=("Segoe UI", 13, "bold")
        ).pack(pady=(0, 10))

        tabela = ttk.Treeview(
            frame,
            columns=("nome", "cpf", "tipo"),
            show="headings"
        )

        tabela.heading("nome", text="Nome")
        tabela.heading("cpf", text="CPF")
        tabela.heading("tipo", text="Tipo")

        tabela.column("nome", width=260)
        tabela.column("cpf", width=180)
        tabela.column("tipo", width=140, anchor="center")

        for i, func in enumerate(funcionarios):
            tabela.insert(
                "",
                tk.END,
                iid=str(i),
                values=(func.nome, func.cpf, func.tipo.capitalize())
            )

        tabela.pack(fill="both", expand=True)

        def confirmar():
            selecionado = tabela.selection()
            if selecionado:
                retorno["indice"] = int(selecionado[0])
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x", pady=10)

        ttk.Button(botoes, text="Cancelar", command=janela.destroy).pack(side="right")
        ttk.Button(botoes, text="Selecionar", command=confirmar).pack(side="right", padx=5)

        janela.wait_window()

        return retorno["indice"]

    # ==========================================================
    # Menu
    # ==========================================================

    @staticmethod
    def menu_gerenciamento():

        janela = tk.Toplevel()
        janela.title("Gerenciamento de Funcionários")
        janela.geometry("430x320")
        janela.grab_set()

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Funcionários",
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(0, 20))

        def escolher(valor):
            retorno["valor"] = valor
            janela.destroy()

        ttk.Button(
            frame,
            text="📋 Listar Funcionários",
            command=lambda: escolher("1")
        ).pack(fill="x", ipady=7, pady=5)

        ttk.Button(
            frame,
            text="🗑 Excluir Funcionário",
            command=lambda: escolher("2")
        ).pack(fill="x", ipady=7, pady=5)

        ttk.Button(
            frame,
            text="✏ Editar Nome",
            command=lambda: escolher("3")
        ).pack(fill="x", ipady=7, pady=5)

        ttk.Separator(frame).pack(fill="x", pady=15)

        ttk.Button(
            frame,
            text="Voltar",
            command=lambda: escolher("0")
        ).pack(fill="x", ipady=7)

        janela.wait_window()

        return retorno["valor"]