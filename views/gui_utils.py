import tkinter as tk
from tkinter import ttk, messagebox

_root = None


# -------------------------------------------------------------------
# Inicialização
# -------------------------------------------------------------------

def get_root():
    global _root

    if _root is None:
        _root = tk.Tk()
        _root.withdraw()

        try:
            style = ttk.Style()
            style.theme_use("clam")
        except:
            pass

    return _root


# -------------------------------------------------------------------
# Utilidades
# -------------------------------------------------------------------

def centralizar(janela, largura, altura):

    janela.update_idletasks()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


# -------------------------------------------------------------------
# Entrada personalizada
# -------------------------------------------------------------------

def perguntar(texto, titulo="Sistema"):

    get_root()

    dialogo = tk.Toplevel()

    dialogo.title(titulo)
    dialogo.resizable(False, False)

    centralizar(dialogo, 420, 180)

    dialogo.grab_set()

    frame = ttk.Frame(dialogo, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(
        frame,
        text=texto,
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(0, 10))

    entrada = ttk.Entry(
        frame,
        font=("Segoe UI", 11),
        width=35
    )

    # Esconde automaticamente quando o texto parecer senha
    texto_lower = texto.lower()

    if "senha" in texto_lower:
        entrada.configure(show="•")

    entrada.pack(fill="x", pady=(0, 15))

    retorno = {
        "valor": None
    }

    def confirmar():

        retorno["valor"] = entrada.get()

        dialogo.destroy()

    def cancelar():

        retorno["valor"] = None

        dialogo.destroy()

    botoes = ttk.Frame(frame)
    botoes.pack(fill="x")

    ttk.Button(
        botoes,
        text="Cancelar",
        command=cancelar
    ).pack(side="right")

    ttk.Button(
        botoes,
        text="OK",
        command=confirmar
    ).pack(side="right", padx=5)

    entrada.focus()

    entrada.bind(
        "<Return>",
        lambda e: confirmar()
    )

    dialogo.protocol(
        "WM_DELETE_WINDOW",
        cancelar
    )

    dialogo.wait_window()

    return retorno["valor"]


# -------------------------------------------------------------------
# Mensagens
# -------------------------------------------------------------------

def informar(texto, titulo="Sistema"):

    get_root()

    messagebox.showinfo(
        titulo,
        texto
    )


def erro(texto, titulo="Erro"):

    get_root()

    messagebox.showerror(
        titulo,
        texto
    )


def confirmar(texto, titulo="Confirmação"):

    get_root()

    return messagebox.askyesno(
        titulo,
        texto
    )