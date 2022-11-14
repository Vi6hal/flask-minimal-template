.PHONY: start install test build setup-offline test docker-build

start:
	@bash bin/run.sh

install:
	@pip install -r requirements.txt

install-offline:
	@pip install --no-index --find-links=deps -r requirements.txt

setup-offline:
	@pip download -d deps -r requirements.txt

test:
	@pytest tests

docker-build:
	@docker build . -t flask-app
