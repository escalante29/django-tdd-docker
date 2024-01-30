# pull official base image
FROM python:3.12-slim-bookworm

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# updated
# install system dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
    build-essential postgresql-client netcat-traditional \
	&& rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# new
# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

# new
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]