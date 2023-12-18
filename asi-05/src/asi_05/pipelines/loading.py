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


