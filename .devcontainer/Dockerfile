# Adding platform so it works on a Mac with M1 Chip - https://stackoverflow.com/questions/65612411/forcing-docker-to-use-linux-amd64-platform-by-default-on-macos
FROM --platform=linux/amd64 python:3.11-bullseye
WORKDIR /

# install dependencies from requirements.txt
COPY .devcontainer/requirements.txt .
RUN pip install -r requirements.txt
