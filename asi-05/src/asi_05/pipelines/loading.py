


# from kedro.config import ConfigLoader
# from kedro.framework.hooks import _create_hook_manager
# from kedro.extras.datasets.pandas import SQLTableDataSet
#
# config_loader = ConfigLoader(conf_source="conf")
# credentials = config_loader.get("catalog.yml")["example_data_source"]["credentials"]
#
#
# def loadData():
#     # Inicjalizuj połączenie z bazą danych
#     data_source = SQLTableDataSet(
#         table_name="exoplanets_asi",
#         credentials=credentials
#     )
#
#     # Wczytaj dane
#     data = data_source.load()
#
#     # Wyświetl pierwsze wiersze danych
#     print(data.head())
#
# if __name__ == "__main__":
#     loadData()





# from kedro.extras.datasets.pandas import SQLTableDataSet
#
# # Poprawne dane dostępowe do bazy danych
# credentials = {
#     "driver": "postgresql",
#     "host": "localhost",
#     "port": 5432,
#     "database": "asi",
#     "username": "postgres",
#     "password": "admin"
# }
#
# # Poprawne użycie SQLTableDataSet
# dataset = SQLTableDataSet(table_name="exoplanets_asi", credentials=credentials)
# data = dataset.load()


# import psycopg2
# from sqlalchemy import create_engine
#
# def loadData():
#
# # Dane dostępowe do bazy danych
#     database_credentials = {
#         "host": "localhost",
#         "port": 5432,
#         "database": "asi",
#         "user": "postgres",
#         "password": "admin",
#     }
#
# # Generuj ciąg połączeniowy SQLAlchemy
#     connection_string = (
#         f"postgresql://{database_credentials['user']}:{database_credentials['password']}"
#         f"@{database_credentials['host']}:{database_credentials['port']}/{database_credentials['database']}"
#     )
#
# # Utwórz połączenie za pomocą psycopg2
#     connection = psycopg2.connect(
#         host=database_credentials["host"],
#         port=database_credentials["port"],
#         database=database_credentials["database"],
#         user=database_credentials["user"],
#         password=database_credentials["password"],
#     )
#
# # Alternatywnie, utwórz połączenie za pomocą SQLAlchemy
#     engine = create_engine(connection_string)
#     connection_sqlalchemy = engine.connect()
#
# # Tutaj możesz wykonywać operacje na bazie danych za pomocą połączenia "connection" lub "connection_sqlalchemy"
# # ...
#
# # Nie zapomnij zamknąć połączeń, gdy już nie są potrzebne
#     connection.close()
#     connection_sqlalchemy.close()
#
# if __name__ == "__main__":
#     loadData()



# from kedro.extras.datasets.pandas import SQLTableDataSet
# import pandas as pd
#
# def loadData():
#     # Wczytaj konfigurację zestawu danych z pliku catalog.yml
#     catalog = context.catalog
#     dataset = catalog.load("example_data_source")  # Zmień na odpowiednią nazwę źródła danych z catalog.yml
#
#     # Wczytaj dane z bazy danych PostgreSQL
#     data = dataset.load()
#
#     # Zwróć wczytane dane
#     return data
#
# # Poniższy blok kodu uruchomi funkcję loadData() w przypadku bezpośredniego uruchamiania tego pliku
# if __name__ == "__main__":
#     # Załaduj dane
#     loaded_data = loadData()
#
#     # Wyświetl wczytane dane
#     print(loaded_data.head())



# import psycopg2
#
# # Dane dostępowe do bazy danych
# database_credentials = {
#     "host": "localhost",
#     "port": 5432,
#     "database": "asi",
#     "user": "postgres",
#     "password": "admin",
# }
#
# # Generuj ciąg połączeniowy
# connection_string = (
#     f"postgresql://{database_credentials['user']}:{database_credentials['password']}"
#     f"@{database_credentials['host']}:{database_credentials['port']}/{database_credentials['database']}"
# )
#
# try:
#     # Próba połączenia
#     connection = psycopg2.connect(
#         host=database_credentials["host"],
#         port=database_credentials["port"],
#         database=database_credentials["database"],
#         user=database_credentials["user"],
#         password=database_credentials["password"],
#     )
#
#     print("Połączenie z bazą danych udane.")
#
#     # Zamknięcie połączenia
#     connection.close()
#
# except Exception as e:
#     print(f"Błąd połączenia z bazą danych: {e}")


# import psycopg2
# import pandas as pd
#
# def loadData():
#     # Dane dostępowe do bazy danych
#     database_credentials = {
#         "host": "localhost",
#         "port": 5432,
#         "database": "asi",
#         "user": "postgres",
#         "password": "admin",
#     }
#
#     # Generuj ciąg połączeniowy
#     connection_string = (
#         f"postgresql://{database_credentials['user']}:{database_credentials['password']}"
#         f"@{database_credentials['host']}:{database_credentials['port']}/{database_credentials['database']}"
#     )
#
#     try:
#         # Próba połączenia
#         connection = psycopg2.connect(
#             host=database_credentials["host"],
#             port=database_credentials["port"],
#             database=database_credentials["database"],
#             user=database_credentials["user"],
#             password=database_credentials["password"],
#         )
#
#         print("Połączenie z bazą danych udane.")
#
#         # Wykonaj zapytanie SQL i wczytaj wyniki do DataFrame
#         query = "SELECT * FROM exoplanets_asi"  # Zastąp 'your_table_name' odpowiednią nazwą tabeli
#         data = pd.read_sql_query(query, connection)
#         print(data)
#
#         # Zamknięcie połączenia
#         connection.close()
#
#         # Zwróć wczytane dane
#         return data
#
#     except Exception as e:
#         print(f"Błąd połączenia z bazą danych: {e}")
#
# # Przykład użycia
# loaded_data = loadData()
# print(loaded_data.head())


import psycopg2
import pandas as pd
import yaml
from kedro.config import ConfigLoader
from pathlib import Path

def loadData():

    conf_loader = ConfigLoader(conf_source=str(Path.cwd() / 'conf'))
    credentials = conf_loader.get("local/credentials", "credentials.yml")
    # Parametry połączenia z bazą danych
    db_username = credentials["postgres"]["username"]
    db_password = credentials["postgres"]["password"]
    db_host = credentials["postgres"]["host"]
    db_port = credentials["postgres"]["port"]
    db_name = credentials["postgres"]["name"]

    # Generuj ciąg połączeniowy
    connection_string = (
        f"postgresql://{db_username}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port
        )

        print("Połączenie z bazą danych udane.")

        # Wykonaj zapytanie SQL i wczytaj wyniki do DataFrame
        query = "SELECT * FROM exoplanets_asi"  # Zastąp 'your_table_name' odpowiednią nazwą tabeli
        data = pd.read_sql_query(query, connection)

        # Zamknięcie połączenia
        connection.close()

        # Zwróć wczytane dane
        return data

    except Exception as e:
        print(f"Błąd połączenia z bazą danych: {e}")


