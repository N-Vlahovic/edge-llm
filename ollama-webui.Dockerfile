FROM ghcr.io/ollama-webui/ollama-webui:main

RUN apt-get update && apt install -y tmux httpie
