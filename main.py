"""
main.py — Ponto de entrada do sistema hoteleiro
════════════════════════════════════════════════
Responsabilidade: criar o DataStore, injetar nos controllers
e iniciar a aplicação.
"""

from repository.data_store import SQLiteDataStore
from controllers.app_controller import AppController


def main():
    store = SQLiteDataStore()
    app = AppController(store)
    app.run()


if __name__ == "__main__":
    main()