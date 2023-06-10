include .env



dev: freeze
	docker-compose up --force-recreate

up:
	docker-compose up

show: up migrate

start:
	poetry run uvicorn ab_test_api:app --host ${HOST} --port ${PORT} --reload

start-server:
	uvicorn ab_test_api:app --host ${HOST} --port ${PORT} --reload

start-db:
	docker-compose -f docker-compose.db.yml up


lint:
	poetry run flake8 ab_test_api

freeze:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

install:
	poetry install

migrate:
	poetry run python ab_test_api/migration.py

rm:
	docker-compose stop && \
	docker-compose rm && \
	sudo rm -rf pgdata/

rm-venv:
	rm -rf `poetry env info -p`

p: lint
	git push