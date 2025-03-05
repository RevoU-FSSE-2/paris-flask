FROM python:3.11-slim-bookworm

RUN apt-get update

COPY --from=ghcr.io/astral-sh/uv:0.6.4 /uv /uvx /bin/
WORKDIR /flask_app
RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project
COPY . .
# flask --app main run --port 8000 --reload --debug --host 0.0.0.0
CMD ["uv", "run" , "flask", "--app", "main", "run", "--port", "8000", "--reload", "--debug", "--host", "0.0.0.0"]