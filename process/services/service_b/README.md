# Service B

Simple and fast service...

Python version: 3.9

## Setup

Requirement:
- [Poetry](https://python-poetry.org/) to management dependencies:

```console
poetry install
```

## Local dev

### Run

```console
poetry run nameko run --config config.yaml service 
```

### Tests

```console
poetry run pytest tests
```

### Code

**Black: Format code**

```console
poetry run black .
```

**Black: Check code format**

```console
poetry run black --check .
```

**Flake8: Check code format**

```console
poetry run flake8
```

## Container

**Build**

```console
docker build -t service_b:1.0.0 .
```

**Run**

```console
docker run -it --rm -p 8000:8000 service_b:1.0.0
```