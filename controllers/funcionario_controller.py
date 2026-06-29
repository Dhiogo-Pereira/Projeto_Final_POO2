"""
Controller de Funcionários
══════════════════════════
Toda a lógica de negócio relacionada a funcionários:
validação de senha, checagem de duplicatas, CRUD.
"""

from models.usuario import Funcionario, Gerente
from views.funcionario_view import FuncionarioView
from views.menu_view import MenuView


class FuncionarioController:
    def __init__(self, data_store):
        self.db = data_store

    # ── Validação de senha (regra de negócio) ─────────────────────
    @staticmethod
    def _validar_senha(senha: str) -> tuple[bool, str]:
        """Retorna (valido, mensagem_de_erro)."""
        if len(senha) < 8:
            return False, "Senha muito curta (mínimo 8 caracteres)."
        if senha.islower() or senha.isupper():
            return False, "Use letras maiúsculas e minúsculas."
        if not any(c.isdigit() for c in senha):
            return False, "Inclua pelo menos um número."
        if all(c.isalnum() for c in senha):
            return False, "Inclua pelo menos um símbolo (ex.: !, @, #)."
        return True, ""

    # ── CRUD ──────────────────────────────────────────────────────
    def cadastrar(self, modo_config: bool = False) -> bool:
        """
        modo_config=True → cria Gerente sem perguntar o tipo.
        Usado apenas na inicialização do sistema.
        Retorna True se o cadastro foi concluído com sucesso.
        """
        nome, cpf = FuncionarioView.prompt_cadastro()

        if not nome:        # usuário cancelou o diálogo
            return False

        if self.db.buscar_funcionario_por_nome(nome):
            MenuView.erro(f"Já existe um funcionário com o nome '{nome}'.")
            return False

        # Loop de senha com validação
        while True:
            senha, confirma = FuncionarioView.prompt_senha()

            if senha is None:   # usuário cancelou
                return False

            if senha != confirma:
                MenuView.erro("As senhas não coincidem.")
                continue

            valido, msg = self._validar_senha(senha)
            if valido:
                break
            MenuView.erro(msg)

        # Tipo de conta
        # O Combobox em prompt_tipo() usa state="readonly", então o valor
        # retornado é sempre válido. O while foi removido para evitar
        # janelas repetidas desnecessárias.
        if modo_config:
            tipo = "gerente"
        else:
            tipo = FuncionarioView.prompt_tipo()
            if tipo not in ("gerente", "funcionario"):
                tipo = "funcionario"    # fallback de segurança

        novo = Gerente(nome, cpf, senha) if tipo == "gerente" else Funcionario(nome, cpf, senha)
        self.db.adicionar_funcionario(novo)
        MenuView.sucesso(f"Funcionário '{nome}' [{tipo}] cadastrado com sucesso.")
        return True

    def listar(self) -> None:
        FuncionarioView.listar(self.db.listar_funcionarios())

    def deletar(self) -> None:
        funcionarios = self.db.listar_funcionarios()
        idx = FuncionarioView.prompt_selecionar(funcionarios, "deletar")
        if idx is not None:
            alvo = funcionarios[idx]
            self.db.remover_funcionario(alvo)
            MenuView.sucesso(f"Funcionário '{alvo.nome}' removido.")

    def editar(self) -> None:
        funcionarios = self.db.listar_funcionarios()
        idx = FuncionarioView.prompt_selecionar(funcionarios, "editar")
        if idx is not None:
            alvo = funcionarios[idx]
            novo_nome = FuncionarioView.prompt_novo_nome(alvo.nome)
            if novo_nome:
                if self.db.buscar_funcionario_por_nome(novo_nome):
                    MenuView.erro("Nome já em uso.")
                    return
                alvo.nome = novo_nome
                self.db.atualizar_funcionario(alvo)
                MenuView.sucesso("Funcionário atualizado.")

    # ── Menu de gerenciamento ─────────────────────────────────────
    def menu_gerenciamento(self) -> None:
        while True:
            opcao = FuncionarioView.menu_gerenciamento()
            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.deletar()
            elif opcao == "3":
                self.editar()
            elif opcao == "0":
                break
            else:
                MenuView.erro("Opção inválida.")