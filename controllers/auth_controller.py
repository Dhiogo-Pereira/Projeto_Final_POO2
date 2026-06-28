"""
Controller de Autenticação
══════════════════════════
Regras de negócio do login. Usa a view para I/O e o repositório
para consultar dados — nunca acessa dados diretamente.
"""

from views.auth_view import AuthView


class AuthController:
    def __init__(self, data_store, view: AuthView = None):
        self.db = data_store
        self.view = view or AuthView()

    def login(self):
        """
        Solicita credenciais, valida contra o repositório.
        Retorna o objeto Funcionario/Gerente se autenticado, ou None.
        """
        nome, senha = AuthView.prompt_login()

        for funcionario in self.db.listar_funcionarios():
            if funcionario.nome == nome and funcionario.senha == senha:
                AuthView.login_sucesso(funcionario)
                return funcionario

        AuthView.login_falhou()
        return None
