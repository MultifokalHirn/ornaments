.ONESHELL: # this ensure that all commands in a target run in the same shell
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: help
help: ## Show available commands and their descriptions
	@echo "Usage: make [target]"
	@echo ""
	@awk -F ':.*?## ' '/^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: logo
logo: ## Show ornaments logo
	$(VENV)/python src/ornaments/_utils.py

.PHONY: in-venv
in-venv: ## Ensure we are in the virtual environment
	$(VENV)/pdm config python.use_venv true
# TODO: needed?

.PHONY: bootstrap
bootstrap: python-version clean-venv venv ## Delete existing & create new venv

.PHONY: prod
prod: in-venv  ## Install package dependencies
	# Installing package dependencies...
	$(VENV)/pdm install --prod

.PHONY: dev
dev: in-venv prod  ## Install (all) dev dependencies
	# Installing dev dependencies...
	$(VENV)/pdm install -dG :all

.PHONY: bootstrap-dev
bootstrap-dev:  ## Setup a fresh dev environment [this will delete your existing venv]
	# setting up a fresh dev environment...
	$(MAKE) bootstrap
	$(MAKE) dev
	$(MAKE) setup-pre-commit
	$(MAKE) logo

setup-pre-commit: in-venv ## Install pre-commit hooks
	# installing pre-commit hooks...
	$(VENV)/pre-commit autoupdate
	$(VENV)/pre-commit install && $(VENV)/pre-commit install --hook-type commit-msg
.PHONY: setup-pre-commit

.PHONY: update
update: ## Update dependencies and pre-commit hooks
	$(VENV)/pdm self update
	$(VENV)/pdm run update-all
	$(VENV)/pre-commit autoupdate

.PHONY: lint
lint: ## Run linter on python files
lint:
	$(VENV)/pdm run lint

.PHONY: format
format: ## Run formatter on python files
	$(VENV)/pdm run format

mypy: ## Run mypy on python files
mypy:
	$(VENV)/pdm run mypy
.PHONY: mypy

.PHONY: test
test: ## Run unit tests
	$(VENV)/pdm run test

.PHONY: ci
ci: ## Run formatter, linter, mypy, and unit tests
	$(VENV)/pdm run ci

.DEFAULT_GOAL := help

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

.PHONY: python-version
python-version: ## Show the python version
	# Using the following python version:
	@python --version

include Makefile.venv
