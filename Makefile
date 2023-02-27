PROJECT_NAME = sqlalchemylab

.PHONY: default
default: help

.PHONY: help
help:
	@echo "All Commands:"
	@echo "	Code Style:"
	@echo "		format - Format code style."
	@echo "	Env:"
	@echo "		db_connect - Connect to database container."
	@echo "		db_generate_revision - Creates a database migration based on models."
	@echo "		db_upgrade - Apply the created database migration."
	@echo "		db_downgrade - Downgrade the current applied migration."
	@echo "		db_drop - Drop database container."
	@echo "		db_up - Starts database container."
	@echo "		db_down - Stops database container."

.PHONY: format
format:
	black -l 88 -t py310 --skip-string-normalization $(PROJECT_NAME)
	unify --in-place --recursive --quote '"' $(PROJECT_NAME)
	isort --profile black .

	black -l 88 -t py310 --skip-string-normalization --check $(PROJECT_NAME)

	mypy --python-version 3.10 --ignore-missing-imports --disallow-untyped-defs --disallow-untyped-calls $(PROJECT_NAME)/

	flake8 $(PROJECT_NAME)

	unify --check-only --recursive --quote '"' $(PROJECT_NAME)

	isort --profile black -c .

.PHONY: clean
clean:
	- @find . -name "*.pyc" -exec rm -rf {} \;
	- @find . -name "__pycache__" -delete
	- @find . -name "*.pytest_cache" -exec rm -rf {} \;
	- @find . -name "*.mypy_cache" -exec rm -rf {} \;

.PHONY: db_connect
db_connect:
	PGPASSWORD=postgres psql -d postgres -h 127.0.0.1 -U postgres

.PHONY: db_generate_revision
db_generate_revision:
	alembic revision --autogenerate

.PHONY: db_upgrade
db_upgrade:
	alembic upgrade head

.PHONY: db_downgrade
db_downgrade:
	alembic downgrade -1

.PHONY: db_drop
db_drop:
	rm -rf volumes/
	docker container ls -a | grep sqlalchemylab_db | awk '{print $1}' | xargs docker container stop | xargs docker container rm

.PHONY: db_up
db_up:
	docker-compose -f docker-compose.yaml up -d

.PHONY: db_down
db_down:
	docker-compose -f docker-compose.yaml down --remove-orphans

