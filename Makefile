build:        ## Build the services
	chmod +x scripts/build.sh
	scripts/build.sh

docker-update:        ## Build the services
	python3 scripts/update_docker.py
