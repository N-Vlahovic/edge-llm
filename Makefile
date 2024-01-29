build:          ## Build the services
	python3 scripts/update_docker.py
	docker compose up --build -d

stop:           ## Stops the services
	docker compose stop

kill:           ## Kills the services
	docker compose down -v

docker-update:  ## Build the services
	python3 scripts/update_docker.py
