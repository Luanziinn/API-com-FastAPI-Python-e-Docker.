.PHONY: run-docker
run-docker:
	docker-compose up -d

.PHONY: create-migrations
create-migrations:
	alembic revision --autogenerate -m "$(d)"

.PHONY: run-migrations
run-migrations:
	alembic upgrade head

.PHONY: run
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
