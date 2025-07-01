# =============================================================================
# base - Prepara a base do contâiner
# =============================================================================
FROM python:3.9-alpine AS base

ENV PYTHONUNBUFFERED 1
RUN apk update && apk add --virtual .build-deps \
  gcc musl-dev make

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /service

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false

# =============================================================================
# development - Instala dependências de dev e copia o código fonte
# =============================================================================
FROM base AS dev
RUN poetry install --no-root
COPY . /service/

# =============================================================================
# Lint - faz verificações estáticas no código
# =============================================================================
FROM dev AS Lint
RUN black --check --diff .

# =============================================================================
# DevService - Roda o serviço em modo de desenvolvimento
# =============================================================================
FROM dev AS devService
ENV DEBUG=true
CMD ["nameko", "run", "--config", "config.yaml", "service"]

# =============================================================================
# Release (instala dependências de prod)
# =============================================================================
FROM base AS release
RUN poetry install --only main --no-root
COPY . /service/
CMD ["nameko", "run", "--config", "config.yaml", "service"]
