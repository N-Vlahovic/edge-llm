# Edge LLM
## Deploy large language models on low power, single-board computers.

Seamlessly deploy LLMs locally on your Jetson Nano and make use of small models such as [TinyLlama](https://huggingface.co/TinyLlama) and leverage their power using a web-ui.

### Requirements
- NVidia Jetson Nano
- 4GB >= RAM
- 32GB >= Storage (64GB >= preferred)
- JetPack SDK


### Getting Started

#### Updating Docker
If you installed JetPack following the [official getting-started docs](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit), it might be that your `docker; docker-compose` version is somewhat dated. 

Running `make docker-update` will update `docker; docker-compose` by invoking the `./scripts/update_docker.sh` script, which:
- Removes the existing `docker; docker-compose` installations
- Adds the Docker's official GPG key
- Adds the repository to Apt sources
- Installs the Docker packages
- Enables docker service
- Adds the current `$USER` to the `docker` user group (a reboot will be necessary)


#### Creating an ENV File
The `docker-compose.yml` file has abstracted certain parameters by leveraging `.env` files. An `.env` file with the following variables needs to be created:
- `LLM_PORT=<int>`: The exposed port (on the Jetson nano - not the container) of the LLM backend. 
- `WEBUI_PORT=<int>`: The exposed port (on the Jetson nano - not the container) of the LLM WebUI. 

Here is a possible way to create the `.env` file:
```zsh
echo 'LLM_PORT=8000' >> .env && echo 'WEBUI_PORT=3000' >> .env
```

#### Building the Services
