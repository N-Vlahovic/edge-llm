build:        ## Build the services
	python3 scripts/update_docker.py
	chmod +x scripts/build.sh
	scripts/build.sh

stop:        ## Stops the services
	docker compose stop

kill:        ## Kills the services
	docker compose down -v

docker-update:        ## Build the services
	python3 scripts/update_docker.py
