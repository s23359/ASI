import streamlit as st
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from kedro.config import ConfigLoader
from pathlib import Path
import requests
import pandas as pd
import psycopg2
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
from sdv.metadata import SingleTableMetadata

# Załadowanie kontekstu Kedro
project_path = Path.cwd()
bootstrap_project(project_path)

FASTAPI_ENDPOINT = "http://localhost:8000/predict"
SYNTHETIC_DATA_SCRIPT = "main.py"

conf_loader = ConfigLoader(conf_source=str(Path.cwd() / 'conf'))


with KedroSession.create(project_path) as session:
    st.title('Aplikacja Streamlit do Uruchamiania Potoków Kedro')

    if st.button('Uruchom Potok Kedro'):
        session.run(pipeline_name="__default__")
        st.success('Potok został uruchomiony!')

    if st.button('Wygeneruj dane syntetyczne'):
        metadata = SingleTableMetadata()

        st.write(metadata)

        # odczytanie credentials
        conf_loader = ConfigLoader(conf_source=str(Path.cwd() / 'conf'))
        credentials = conf_loader.get("local/credentials", "credentials.yml")
        # Parametry połączenia z bazą danych
        db_username = credentials["postgres"]["username"]
        db_password = credentials["postgres"]["password"]
        db_host = credentials["postgres"]["host"]
        db_port = credentials["postgres"]["port"]
        db_name = credentials["postgres"]["name"]

        # Łączenie z bazą danych
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port
        )

        # Wczytywanie danych z bazy danych do DataFrame
        query = "SELECT * FROM exoplanets"
        real_data = pd.read_sql(query, connection)

        # Zamykanie połączenia
        connection.close()

        meta_data = metadata.detect_from_dataframe(real_data)

        synthesizer = SingleTablePreset(metadata, name='FAST_ML')
        synthesizer.fit(data=real_data)

        synthetic_data = synthesizer.sample(num_rows=500)
        st.dataframe(real_data)

        st.write('Informacje o danych syntetycznych:')
        st.dataframe(synthetic_data)

    with st.form(key='predict_form'):
        name = st.text_input('name', value="")
        distance = st.text_input('distance', value="")
        stellar_magnitude = st.text_input('stellar_magnitude', value="")
        discovery_year = st.text_input('discovery_year', value="")
        mass_multiplier = st.text_input('mass_multiplier', value="")
        mass_wrt = st.text_input('mass_wrt', value="")
        radius_multiplier = st.text_input('radius_multiplier', value="")
        radius_wrt = st.text_input('radius_wrt', value="")
        orbital_radius = st.text_input('orbital_radius', value="")
        orbital_period = st.text_input('orbital_period', value="")
        eccentricity = st.text_input('eccentricity', value="")
        detection_method = st.text_input('detection_method', value="")
        submit_button = st.form_submit_button('Wykonaj Predykcję')

    if submit_button:

        # Przygotowanie danych do predykcji
        data_to_predict = {
            'name': name,
            'distance': distance,
            'stellar_magnitude': stellar_magnitude,
            'discovery_year': discovery_year,
            'mass_multiplier': mass_multiplier,
            'mass_wrt': mass_wrt,
            'radius_multiplier': radius_multiplier,
            'radius_wrt': radius_wrt,
            'orbital_radius': orbital_radius,
            'orbital_period': orbital_period,
            'eccentricity': eccentricity,
            'detection_method': detection_method
        }
        print(data_to_predict)

        # Wysyłanie żądania do FastAPI
        response = requests.post(FASTAPI_ENDPOINT, json=data_to_predict)

        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Wynik Predykcji: {prediction}")
        else:
            st.error("Błąd podczas wykonywania predykcji")