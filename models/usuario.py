"""
Models de Usuário
─────────────────
Contém as classes de domínio para os tipos de usuário do sistema.

Segurança de senha
───────────────────
As senhas NUNCA são armazenadas em texto puro. Usamos PBKDF2-HMAC-SHA256
(função padrão da biblioteca `hashlib`, recomendada pelo NIST) com um
salt aleatório gerado individualmente para cada usuário.
"""

import hashlib
import hmac
import os

_ALGORITMO = "sha256"
_ITERACOES = 100_000
_TAMANHO_SALT_BYTES = 16


def gerar_hash_senha(senha_texto: str) -> str:
    """
    Recebe a senha em texto puro (digitada pelo usuário) e devolve
    uma string segura para armazenar no banco, no formato:

        "<salt_em_hex>$<hash_em_hex>"

    Esta função deve ser chamada SEMPRE que uma senha nova for
    definida (cadastro ou troca de senha) — nunca grave o retorno
    de input()/Entry.get() diretamente no banco.
    """
    salt = os.urandom(_TAMANHO_SALT_BYTES)
    hash_bytes = hashlib.pbkdf2_hmac(
        _ALGORITMO,
        senha_texto.encode("utf-8"),
        salt,
        _ITERACOES,
    )
    return f"{salt.hex()}${hash_bytes.hex()}"


def verificar_senha(senha_texto: str, senha_hash_armazenado: str) -> bool:
    """
    Confere se `senha_texto` (o que o usuário digitou agora, no login)
    corresponde ao hash salvo no banco.
    """
    try:
        salt_hex, hash_hex = senha_hash_armazenado.split("$")
    except (ValueError, AttributeError):
        # Hash malformado ou None — trata como senha incorreta,
        # em vez de deixar a exceção quebrar o login.
        return False

    salt = bytes.fromhex(salt_hex)
    hash_esperado = bytes.fromhex(hash_hex)

    hash_calculado = hashlib.pbkdf2_hmac(
        _ALGORITMO,
        senha_texto.encode("utf-8"),
        salt,
        _ITERACOES,
    )

    return hmac.compare_digest(hash_calculado, hash_esperado)


class Funcionario:
    """Funcionário padrão do hotel. Acesso restrito às operações básicas."""

    def __init__(self, nome: str, cpf: str, senha_hash: str):
        """
        IMPORTANTE: o parâmetro `senha_hash` espera o hash JÁ GERADO
        (formato "salt$hash"), não a senha em texto puro.

        O construtor é usado tanto para criar um funcionário novo
        quanto para reconstruir um funcionário a partir de uma linha
        do banco (onde só existe o hash). Para cadastrar a partir de
        uma senha digitada pelo usuário, use `Funcionario.criar(...)`.
        """
        self.nome = nome                        # passa pelo setter (valida)
        self._cpf = self._validar_cpf(cpf)       # sem setter público — identidade fixa
        self._senha_hash = senha_hash
        self._tipo = "funcionario"

    # ── nome: mutável, mas validado ────────────────────────────────
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome do funcionário não pode ser vazio.")
        self._nome = valor.strip()

    # ── cpf: identidade do registro, imutável após a criação ───────
    @property
    def cpf(self) -> str:
        return self._cpf

    @staticmethod
    def _validar_cpf(cpf: str) -> str:
        if not cpf or not cpf.strip():
            raise ValueError("CPF do funcionário não pode ser vazio.")
        return cpf.strip()

    # ── senha: só leitura direta; escrita só via redefinir_senha ───
    @property
    def senha_hash(self) -> str:
        return self._senha_hash

    def redefinir_senha(self, senha_texto: str) -> None:
        """
        Única forma permitida de trocar a senha de fora da classe.
        Garante que o que fica armazenado é sempre um hash — nunca
        é possível, por engano, atribuir texto puro a `senha_hash`
        porque esse atributo não tem setter público.
        """
        self._senha_hash = gerar_hash_senha(senha_texto)

    def verificar_senha(self, senha_texto: str) -> bool:
        """Confere a senha digitada no login contra o hash armazenado."""
        return verificar_senha(senha_texto, self._senha_hash)

    # ── tipo: só leitura ─────────────────────────────────────────────
    @property
    def tipo(self) -> str:
        return self._tipo

    @classmethod
    def criar(cls, nome: str, cpf: str, senha_texto: str):
        """
        Fábrica para uso no CADASTRO: recebe a senha em texto puro
        (o que vem do formulário), gera o hash internamente e
        devolve a instância já pronta para ser persistida.

        Graças ao uso de `cls` (em vez de `Funcionario` fixo), esta
        mesma implementação funciona corretamente para a subclasse
        Gerente também — `Gerente.criar(...)` devolve um Gerente.
        """
        return cls(nome, cpf, gerar_hash_senha(senha_texto))

    def __repr__(self):
        return f"Funcionario(nome={self._nome!r}, cpf={self._cpf!r})"


class Gerente(Funcionario):
    """Gerente do hotel. Possui acesso total, incluindo gestão de funcionários."""

    def __init__(self, nome: str, cpf: str, senha_hash: str):
        super().__init__(nome, cpf, senha_hash)
        self._tipo = "gerente"

    def __repr__(self):
        return f"Gerente(nome={self._nome!r}, cpf={self._cpf!r})"