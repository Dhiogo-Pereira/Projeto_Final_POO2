"""
Repositório de Dados — Camada de Persistência
══════════════════════════════════════════════
Esta classe é o único ponto de acesso aos dados do sistema.
Todo controller deve obtê-la por injeção de dependência (receber
no __init__), NUNCA importar dados diretamente.

┌──────────────────────────────────────────────────────────────┐
│  COMO ADICIONAR UM BANCO DE DADOS:                           │
│                                                              │
│  1. Crie uma subclasse (ex.: SQLiteDataStore(DataStore))     │
│  2. Sobrescreva cada método usando seu ORM/driver favorito   │
│  3. Em main.py, troque DataStore() por SQLiteDataStore()     │
│  4. Nenhum controller ou view precisa ser alterado.          │
└──────────────────────────────────────────────────────────────┘
"""


class DataStore:
    """Implementação em memória — padrão para desenvolvimento."""

    def __init__(self):
        self._funcionarios: list = []
        self._clientes: list = []
        self._quartos: list = []
        self._alugueis: list = []

    # ── Funcionários ──────────────────────────────────────────────
    def listar_funcionarios(self) -> list:
        return list(self._funcionarios)

    def buscar_funcionario_por_nome(self, nome: str):
        for f in self._funcionarios:
            if f.nome == nome:
                return f
        return None

    def adicionar_funcionario(self, funcionario) -> None:
        self._funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario) -> None:
        self._funcionarios.remove(funcionario)

    def atualizar_funcionario(self, funcionario) -> None:
        pass  # Em memória: o objeto já está atualizado por referência.
              # Em um BD, aqui seria: UPDATE funcionarios SET ... WHERE id = ...

    # ── Clientes ──────────────────────────────────────────────────
    def listar_clientes(self) -> list:
        return list(self._clientes)

    def buscar_cliente_por_cpf(self, cpf: str):
        for c in self._clientes:
            if c.cpf == cpf:
                return c
        return None

    def adicionar_cliente(self, cliente) -> None:
        self._clientes.append(cliente)

    def remover_cliente(self, cliente) -> None:
        self._clientes.remove(cliente)

    # ── Quartos ───────────────────────────────────────────────────
    def listar_quartos(self) -> list:
        return list(self._quartos)

    def listar_quartos_disponiveis(self) -> list:
        return [q for q in self._quartos if q.disponivel]

    def adicionar_quarto(self, quarto) -> None:
        self._quartos.append(quarto)

    # ── Alugueis ──────────────────────────────────────────────────
    def listar_alugueis(self) -> list:
        return list(self._alugueis)

    def adicionar_aluguel(self, aluguel) -> None:
        self._alugueis.append(aluguel)
