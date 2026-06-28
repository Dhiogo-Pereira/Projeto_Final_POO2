"""
View de Autenticação
════════════════════
Coleta credenciais e exibe resultado do login.
"""


class AuthView:

    @staticmethod
    def prompt_login() -> tuple[str, str]:
        print("\n─── Login ───")
        nome = input("Nome:  ").strip().title()
        senha = input("Senha: ").strip()
        return nome, senha

    @staticmethod
    def login_sucesso(usuario) -> None:
        print(f"\nBem-vindo(a), {usuario.nome}! [{usuario.tipo.capitalize()}]")

    @staticmethod
    def login_falhou() -> None:
        print("[ERRO] Nome ou senha incorretos.")
