# stackoverflow-searcher-api

Proxy API for searching questions on StackOverflow. Caches search query results on local DB.

The search API is exposed at:

```http
GET /api/search/
```

This project is meant to be used in conjuction with the [client project](https://github.com/AluBhorta/stackoverflow-searcher-client).

## Usage

Dependencies:

- python (>= 3.6)
- pip

First install virtualenv:

```sh
pip install virtualenv
```

Initialize and activate a new python environment with virtualenv:

```sh
# Linux/Mac
virtualenv .venv
source .venv/bin/activate

# Windows
python -m virtualenv .venv
.venv\Scripts\activate
```

Install requirements using pip:

```sh
pip install -r requirements.txt
```

Run DB migrations:

```sh
python manage.py makemigrations

python manage.py migrate
```

Run API server on http://127.0.0.1:8000/

```sh
python manage.py runserver
```
