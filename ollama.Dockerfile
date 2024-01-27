FROM ollama/ollama:latest

RUN apt-get update && apt install -y tmux
