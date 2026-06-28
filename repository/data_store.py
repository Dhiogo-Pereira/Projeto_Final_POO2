"""
Repositório SQLite — Implementação Persistente

O arquivo hotel.db é criado automaticamente na primeira execução.
"""

import sqlite3
import os
from datetime import date

from models.usuario import Funcionario, Gerente
from models.cliente import Cliente
from models.quarto import Quarto
from models.aluguel import Aluguel

# Caminho absoluto para o banco, independente de onde o script é executado
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hotel.db')

class SQLiteDataStore:
    """Implementação persistente usando SQLite3 — arquivo local."""

    def __init__(self):
        self._db_path = db_path
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row          # acesso por nome de coluna
        self._conn.execute("PRAGMA foreign_keys = ON") # integridade referencial
        self._criar_tabelas()

    # ── Criação do esquema ────────────────────────────────────────
    def _criar_tabelas(self) -> None:
        with self._conn:
            self._conn.executescript("""
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id    INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome  TEXT    NOT NULL UNIQUE,
                    cpf   TEXT    NOT NULL,
                    senha TEXT    NOT NULL,
                    tipo  TEXT    NOT NULL DEFAULT 'funcionario'
                );

                CREATE TABLE IF NOT EXISTS clientes (
                    id    INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome  TEXT    NOT NULL,
                    cpf   TEXT    NOT NULL UNIQUE,
                    email TEXT    NOT NULL DEFAULT ''
                );

                CREATE TABLE IF NOT EXISTS quartos (
                    id           INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero       INTEGER NOT NULL UNIQUE,
                    tipo         TEXT    NOT NULL,
                    preco_diaria REAL    NOT NULL,
                    disponivel   INTEGER NOT NULL DEFAULT 1
                );

                CREATE TABLE IF NOT EXISTS alugueis (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_cpf   TEXT    NOT NULL,
                    quarto_numero INTEGER NOT NULL,
                    data_inicio   TEXT    NOT NULL,
                    data_fim      TEXT    NOT NULL,
                    tipo_servico  TEXT    NOT NULL DEFAULT 'basico',
                    valor         REAL    NOT NULL,
                    FOREIGN KEY (cliente_cpf)   REFERENCES clientes(cpf),
                    FOREIGN KEY (quarto_numero) REFERENCES quartos(numero)
                );
            """)

    # ── Conversores privados (row → model) ────────────────────────
    @staticmethod
    def _to_funcionario(row) -> Funcionario:
        cls = Gerente if row["tipo"] == "gerente" else Funcionario
        return cls(row["nome"], row["cpf"], row["senha"])

    @staticmethod
    def _to_cliente(row) -> Cliente:
        return Cliente(row["nome"], row["cpf"], row["email"])

    @staticmethod
    def _to_quarto(row) -> Quarto:
        return Quarto(
            row["numero"],
            row["tipo"],
            row["preco_diaria"],
            bool(row["disponivel"]),
        )

    # ── Funcionários ──────────────────────────────────────────────
    def listar_funcionarios(self) -> list:
        rows = self._conn.execute("SELECT * FROM funcionarios").fetchall()
        return [self._to_funcionario(r) for r in rows]

    def buscar_funcionario_por_nome(self, nome: str):
        row = self._conn.execute(
            "SELECT * FROM funcionarios WHERE nome = ?", (nome,)
        ).fetchone()
        return self._to_funcionario(row) if row else None

    def adicionar_funcionario(self, funcionario) -> None:
        with self._conn:
            self._conn.execute(
                "INSERT INTO funcionarios (nome, cpf, senha, tipo) VALUES (?, ?, ?, ?)",
                (funcionario.nome, funcionario.cpf, funcionario.senha, funcionario.tipo),
            )

    def remover_funcionario(self, funcionario) -> None:
        with self._conn:
            self._conn.execute(
                "DELETE FROM funcionarios WHERE cpf = ?", (funcionario.cpf,)
            )

    def atualizar_funcionario(self, funcionario) -> None:
        """Persiste alterações no funcionário — identifica pelo CPF."""
        with self._conn:
            self._conn.execute(
                "UPDATE funcionarios SET nome = ? WHERE cpf = ?",
                (funcionario.nome, funcionario.cpf),
            )

    # ── Clientes ──────────────────────────────────────────────────
    def listar_clientes(self) -> list:
        rows = self._conn.execute("SELECT * FROM clientes").fetchall()
        return [self._to_cliente(r) for r in rows]

    def buscar_cliente_por_cpf(self, cpf: str):
        row = self._conn.execute(
            "SELECT * FROM clientes WHERE cpf = ?", (cpf,)
        ).fetchone()
        return self._to_cliente(row) if row else None

    def adicionar_cliente(self, cliente) -> None:
        with self._conn:
            self._conn.execute(
                "INSERT INTO clientes (nome, cpf, email) VALUES (?, ?, ?)",
                (cliente.nome, cliente.cpf, cliente.email),
            )

    def remover_cliente(self, cliente) -> None:
        with self._conn:
            self._conn.execute(
                "DELETE FROM clientes WHERE cpf = ?", (cliente.cpf,)
            )

    # ── Quartos ───────────────────────────────────────────────────
    def listar_quartos(self) -> list:
        rows = self._conn.execute("SELECT * FROM quartos").fetchall()
        return [self._to_quarto(r) for r in rows]

    def listar_quartos_disponiveis(self) -> list:
        rows = self._conn.execute(
            "SELECT * FROM quartos WHERE disponivel = 1"
        ).fetchall()
        return [self._to_quarto(r) for r in rows]

    def adicionar_quarto(self, quarto) -> None:
        with self._conn:
            self._conn.execute(
                "INSERT INTO quartos (numero, tipo, preco_diaria, disponivel) VALUES (?, ?, ?, ?)",
                (quarto.numero, quarto.tipo, quarto.preco_diaria, int(quarto.disponivel)),
            )

    # ── Alugueis ──────────────────────────────────────────────────
    def listar_alugueis(self) -> list:
        rows = self._conn.execute("SELECT * FROM alugueis").fetchall()
        result = []
        for r in rows:
            cliente = self.buscar_cliente_por_cpf(r["cliente_cpf"])
            qrow = self._conn.execute(
                "SELECT * FROM quartos WHERE numero = ?", (r["quarto_numero"],)
            ).fetchone()
            if not cliente or not qrow:
                continue  # dado órfão — ignora
            aluguel = Aluguel(
                cliente,
                self._to_quarto(qrow),
                date.fromisoformat(r["data_inicio"]),
                date.fromisoformat(r["data_fim"]),
                r["tipo_servico"],
            )
            result.append(aluguel)
        return result

    def adicionar_aluguel(self, aluguel) -> None:
        with self._conn:
            self._conn.execute(
                """INSERT INTO alugueis
                   (cliente_cpf, quarto_numero, data_inicio, data_fim, tipo_servico, valor)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    aluguel.cliente.cpf,
                    aluguel.quarto.numero,
                    aluguel.data_inicio.isoformat(),
                    aluguel.data_fim.isoformat(),
                    aluguel.tipo_servico,
                    aluguel.valor,
                ),
            )
            # Marca o quarto como ocupado no banco de dados.
            # O AluguelController já faz quarto.disponivel = False no objeto
            # em memória; aqui garantimos que a mudança seja persistida.
            self._conn.execute(
                "UPDATE quartos SET disponivel = 0 WHERE numero = ?",
                (aluguel.quarto.numero,),
            )