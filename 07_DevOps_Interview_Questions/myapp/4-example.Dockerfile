# Installing tools to build a Python project
FROM debian:11-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# Installing all dependencies for the project
FROM build AS build-venv

COPY requirements.txt /requirements.txt

RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copeing project to the new Distroless Image
FROM gcr.io/distroless/python3-debian11

COPY --from=build-venv /venv /venv

COPY main.py .

ENTRYPOINT [ "/venv/bin/python3", "main.py" ]