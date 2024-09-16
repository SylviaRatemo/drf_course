FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN set -e; \
    apt-get update && \
    apt-get -y install netcat-openbsd gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /code

# Copy requirements first to cache pip installs when code changes
COPY requirements.txt /code/
WORKDIR /code

RUN set -e; \
    python -m pip install --upgrade pip --no-cache-dir; \
    python -m pip install -r /code/requirements.txt --default-timeout=200 --no-cache-dir;

# Copy the rest of the code
COPY . /code/

RUN chmod +x /code/docker/entrypoints/entrypoint.sh

EXPOSE 8000

# Use CMD if you want more flexibility
ENTRYPOINT ["/code/docker/entrypoints/entrypoint.sh"]
