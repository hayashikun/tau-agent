up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

build:
	docker compose build

format:
	ruff format .
	ruff check . --fix
