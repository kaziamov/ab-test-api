PORT ?= 8000

up:
	docker-compose up

start:
	poetry run uvicorn ab_test_api:app --port $(PORT) --reload

start-server:
	uvicorn ab_test_api:app --host 0.0.0.0 --port $(PORT) --reload

lint:
	poetry run flake8 ab_test_api

freeze:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
