start-deps:
	docker-compose up -d redis

lint:
	flake8

test:
	pytest
