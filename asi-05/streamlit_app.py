import streamlit as st
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from pathlib import Path
import requests


# Załadowanie kontekstu Kedro
project_path = Path.cwd()
bootstrap_project(project_path)

FASTAPI_ENDPOINT = "http://localhost:8000/predict"

with KedroSession.create(project_path) as session:
    st.title('Aplikacja Streamlit do Uruchamiania Potoków Kedro')

    if st.button('Uruchom Potok Kedro'):
        session.run(pipeline_name="__default__")
        st.success('Potok został uruchomiony!')

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