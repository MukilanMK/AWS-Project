# Simple Flask App

Minimal Python Flask application ready for deployment (Docker / Gunicorn / Heroku).

Quickstart

- Run locally:

```bash
python -m venv .venv
.\.venv\Scripts\activate    # Windows
pip install -r requirements.txt
python run.py
```

- Run tests:

```bash
pip install -r requirements.txt
pytest -q
```

- Docker build & run:

```bash
docker build -t simple-flask-app .
docker run -p 5000:5000 simple-flask-app
```

Endpoints

- `GET /` — returns JSON {"message": "Hello, world!"}
