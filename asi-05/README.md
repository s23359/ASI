# asi-05 (Baza danych, kedro, autogluon, streamlit, fastapi)

## Zaktualizuj plik credentials.yml (w katalogu conf/local) danymi do swojej bazy danych postgres

```
postgres:
  username: <username>
  password: <password>
  host: <host>
  port: <port>
  name: <name>
```

## Jak utworzyć środowisko?

Aby uruchomić projekt należy utworzyć środowisko w conda

```
conda env create -f python39.yaml
```

a następnie uruchomić środowisko za pomocą

```
conda activate python39
```

## Jak uruchomić streamlit a następnie fastapi? 

Aby uruchomić streamlit i fastapi należy wykonać komendy 

```
streamlit run streamlit_app.py
```

po uruchomieniu i wykonaniu potoku w streamlit należy wykonać 

```
uvicorn app:app
```

## Jeżeli twoja baza danych nie zawiera tabeli exoplanets wykonaj skrypt create_table.sql lub tabela jest pusta

Utworzenie tabeli
```
psql -h <host> -p <port> -U <username> -d <name> -f <ścieżka do pliku create_table.sql>
```

Zasilenie bazy danych danymi po wcześniejszym polaczeniu sie z baza danych postgres

```
\copy exoplanets FROM '/ścieżka/do/pliku/cleaned_5250.csv' DELIMITER ',' CSV HEADER
```