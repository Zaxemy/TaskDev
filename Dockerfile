FROM python:3.13-slim AS builder

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml .
RUN uv venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .
RUN uv pip install -e .

FROM python:3.13-slim AS production

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 7777

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]