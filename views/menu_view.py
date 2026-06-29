import tkinter as tk
from tkinter import ttk

from views.gui_utils import get_root, informar, erro


class MenuView:

    @staticmethod
    def cabecalho(titulo):
        informar(titulo)

    @staticmethod
    def info(texto):
        informar(texto)

    @staticmethod
    def erro(texto):
        erro(texto)

    @staticmethod
    def sucesso(texto):
        informar(texto, "Sucesso")

    @staticmethod
    def _criar_janela(titulo="Sistema Hoteleiro", largura=500, altura=450):
        """
        CORREÇÃO: usa Toplevel sobre o root oculto persistente de gui_utils,
        em vez de criar um tk.Tk() novo a cada chamada.

        Criar vários tk.Tk() e destruí-los zera o 'default root' do tkinter,
        o que faz qualquer Toplevel posterior aparecer e sumir imediatamente.
        """
        get_root()          # garante que o root oculto existe
        janela = tk.Toplevel()
        janela.title(titulo)
        janela.geometry(f"{largura}x{altura}")
        janela.resizable(False, False)
        janela.grab_set()   # bloqueia interação com outras janelas enquanto aberta
        return janela

    # ------------------------------------------------------------------
    # Menu Inicial
    # ------------------------------------------------------------------

    @staticmethod
    def menu_inicial():

        janela = MenuView._criar_janela("Sistema Hoteleiro", 450, 350)

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=30)
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text="🏨 Sistema Hoteleiro",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=(10, 25))

        ttk.Label(
            frame,
            text="Bem-vindo",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 30))

        def login():
            retorno["valor"] = "1"
            janela.destroy()

        def sair():
            retorno["valor"] = "0"
            janela.destroy()

        ttk.Button(frame, text="Entrar", command=login).pack(fill="x", ipady=8, pady=8)
        ttk.Button(frame, text="Encerrar Sistema", command=sair).pack(fill="x", ipady=8)

        janela.protocol("WM_DELETE_WINDOW", sair)

        # wait_window() roda o event-loop local até a janela ser destruída,
        # sem precisar de mainloop() — e sem destruir o root oculto ao fechar.
        janela.wait_window()

        return retorno["valor"]

    # ------------------------------------------------------------------
    # Menu Principal
    # ------------------------------------------------------------------

    @staticmethod
    def menu_principal(is_gerente=False):

        janela = MenuView._criar_janela(
            "Menu Principal",
            520,
            500 if is_gerente else 430
        )

        retorno = {"valor": "0"}

        frame = ttk.Frame(janela, padding=25)
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text="🏨 Sistema Hoteleiro",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(0, 20))

        ttk.Label(
            frame,
            text="Menu Principal",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 20))

        def escolher(valor):
            retorno["valor"] = valor
            janela.destroy()

        botoes = [
            ("Cadastrar Cliente",   "1"),
            ("Processar Reserva",   "2"),
            ("Gerenciar Clientes",  "3"),
            ("Gerenciar Quartos",   "4"),
        ]

        if is_gerente:
            botoes.extend([
                ("Cadastrar Funcionário",  "5"),
                ("Gerenciar Funcionários", "6"),
            ])

        for texto, valor in botoes:
            ttk.Button(
                frame,
                text=texto,
                command=lambda v=valor: escolher(v)
            ).pack(fill="x", ipady=8, pady=4)

        ttk.Separator(frame).pack(fill="x", pady=18)

        ttk.Button(
            frame,
            text="Logout",
            command=lambda: escolher("0")
        ).pack(fill="x", ipady=8)

        janela.protocol("WM_DELETE_WINDOW", lambda: escolher("0"))

        janela.wait_window()

        return retorno["valor"]