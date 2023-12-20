.ONESHELL:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

help: ## Show available commands and their descriptions
	@echo "Usage: make [target]"
	@echo ""
	@awk -F ':.*?## ' '/^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.PHONY: help

bootstrap: python-version clean-venv venv ## Delete existing & create new venv
.PHONY: bootstrap

prod:  ## install prod dependencies
	$(VENV)/pdm install
.PHONY: prod

dev:  ## install all dependencies in lock file
	$(VENV)/pdm install -G :all
.PHONY: dev

update: ## update lock file if needed
	pdm self update
	pdm run update-all
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
	# Show the python version
	@python --version
.PHONY: python-version

include Makefile.venv
