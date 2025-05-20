# Gomu-File

> Anonymous file share serivce

## Quick Start

### Using UV (Recommended)

```bash
uv sync
uv run app.py
```

### Using Traditional venv

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python app.py
```

### Host Service

```bash
docker build -t gomu-file .
docker run -p 8000:8000 gomu-file
```
