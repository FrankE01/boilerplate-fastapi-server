FROM python:3.12-slim

WORKDIR /usr/src/app

RUN python -m pip install poetry && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./ ./

CMD ["uvicorn","main:app","0.0.0.0:8000"]