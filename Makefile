.ONESHELL:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

help: ## Show available commands and their descriptions
	@echo "Usage: make [target]"
	@echo ""
	@awk -F ':.*?## ' '/^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.PHONY: help

.PHONY: in-venv
in-venv: ## make sure we're in the venv
	$(VENV)/pdm config python.use_venv true
.PHONY: bootstrap
bootstrap: python-version clean-venv venv ## Delete existing & create new venv

prod: in-venv  ## install package dependencies
	# installing prod dependencies...
	$(VENV)/pdm install --prod
.PHONY: prod

dev: in-venv prod  ## install (all) dev dependencies
	# installing dev dependencies...
	$(VENV)/pdm install -dG :all
.PHONY: dev

bootstrap-dev:  ## set up a fresh dev environment
	# setting up a fresh dev environment...
	$(MAKE) bootstrap
	$(MAKE) dev
	$(MAKE) setup-pre-commit
.PHONY: bootstrap-dev

setup-pre-commit: in-venv ## install pre-commit hooks
	# installing pre-commit hooks...
	$(VENV)/pre-commit autoupdate
	$(VENV)/pre-commit install && pre-commit install --hook-type commit-msg
.PHONY: setup-pre-commit

update: ## update lock file if needed
	$(VENV)/pdm self update
	$(VENV)/pdm run update-all
	$(VENV)/pre-commit autoupdate
.PHONY: update

lint: ## Run linter on python files
lint:
	$(VENV)/pdm run lint
.PHONY: lint

format: ## Run formatter on python files
format:
	$(VENV)/pdm run format
.PHONY: format

mypy: ## Run mypy on python files
mypy:
	$(VENV)/pdm run mypy
.PHONY: mypy

test: ## Run unit tests
test:
	$(VENV)/pdm run test
.PHONY: test

ci: ## Run formatter, linter, mypy, and unit tests
ci:
	$(VENV)/pdm run ci
.PHONY: ci

.DEFAULT_GOAL := help

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

python-version: ## Show the python version
	# Using the following python version:
	@python --version
.PHONY: python-version

include Makefile.venv
