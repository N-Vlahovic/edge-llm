init:           ## Build the services
	python3 scripts/check_dotenv.py
	python3 scripts/check_docker.py
	docker compose up --build -d

build:          ## Build the services
	docker compose up --build -d

pull: $(model)  ## Pull a model
	docker exec -it ollama ollama pull $(model)

stop:           ## Stops the services
	docker compose stop

kill:           ## Kills the services
	docker compose down -v

docker-update:  ## Build the services
	python3 scripts/check_docker.py
