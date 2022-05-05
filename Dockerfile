FROM python:3.9-alpine3.13

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=1.1.12

RUN apk add --no-cache python3-dev gcc libc-dev musl-dev openblas gfortran build-base postgresql-libs postgresql-dev libffi-dev curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH "/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-interaction --no-ansi

COPY iam /app/iam

ENV PYTHONPATH="/app:$PYTHONPATH"

ENTRYPOINT [ "python" ]
CMD [ "/app/iam/app.py" ]
