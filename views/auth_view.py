import tkinter as tk
from tkinter import ttk

from views.gui_utils import get_root, centralizar, informar, erro


class AuthView:

    @staticmethod
    def prompt_login():
        """Abre um único formulário com usuário + senha."""
        get_root()

        janela = tk.Toplevel()
        janela.title("Login — Sistema Hoteleiro")
        janela.geometry("400x280")
        janela.resizable(False, False)
        janela.grab_set()

        centralizar(janela, 400, 280)

        retorno = {"nome": None, "senha": None}

        frame = ttk.Frame(janela, padding=25)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="🏨 Acesso ao Sistema",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))

        ttk.Label(frame, text="Usuário").pack(anchor="w")
        nome_entry = ttk.Entry(frame)
        nome_entry.pack(fill="x", pady=(2, 12))

        ttk.Label(frame, text="Senha").pack(anchor="w")
        senha_entry = ttk.Entry(frame, show="•")
        senha_entry.pack(fill="x", pady=(2, 20))

        def confirmar():
            retorno["nome"] = nome_entry.get()
            retorno["senha"] = senha_entry.get()
            janela.destroy()

        def cancelar():
            janela.destroy()

        botoes = ttk.Frame(frame)
        botoes.pack(fill="x")

        ttk.Button(botoes, text="Cancelar", command=cancelar).pack(side="right")
        ttk.Button(botoes, text="Entrar", command=confirmar).pack(side="right", padx=5)

        # Tab/Enter navegam entre campos
        nome_entry.bind("<Return>", lambda e: senha_entry.focus())
        senha_entry.bind("<Return>", lambda e: confirmar())

        janela.protocol("WM_DELETE_WINDOW", cancelar)
        nome_entry.focus()
        janela.wait_window()

        return retorno["nome"], retorno["senha"]

    @staticmethod
    def login_sucesso(usuario):
        informar(
            f"Bem-vindo(a), {usuario.nome}!\n"
            f"[{usuario.tipo.capitalize()}]"
        )

    @staticmethod
    def login_falhou():
        erro("Nome ou senha incorretos.")