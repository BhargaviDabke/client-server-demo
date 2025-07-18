
FROM python:3.13-slim-bookworm

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Equivalent to running pip install -r requirements.txt

COPY pyproject.toml .

COPY uv.lock . 

RUN uv sync   

EXPOSE 8000

COPY . . 

CMD ["uv", "run", "server.py"]
