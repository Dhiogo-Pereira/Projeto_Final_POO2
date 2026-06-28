"""
main.py — Ponto de entrada do sistema hoteleiro
════════════════════════════════════════════════
Responsabilidade: criar o DataStore, injetar nos controllers
e iniciar a aplicação. Nada mais.

Para trocar a camada de dados basta alterar a linha do DataStore:
  from repository.sqlite_store import SQLiteDataStore
  store = SQLiteDataStore("hotel.db")
"""

from repository.data_store import DataStore
from controllers.app_controller import AppController


def main():
    store = DataStore()
    app = AppController(store)
    app.run()


if __name__ == "__main__":
    main()
