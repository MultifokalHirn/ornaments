[![Tests](https://github.com/MultifokalHirn/python_template_repo/actions/workflows/python-checks.yaml/badge.svg?branch=main)](https://github.com/MultifokalHirn/python_template_repo/actions/workflows/python-checks.yaml)
![Coverage](./docs/img/coverage.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/MultifokalHirn/python_template_repo)
![GitHub issues](https://img.shields.io/github/issues/MultifokalHirn/python_template_repo)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/MultifokalHirn/python_template_repo)

# Python Project Template

This is my personal template repository for python projects containing everything needed to start developing.

<!-- - Base Setup for Python Development
- Development and CI tools already Set Up
- Sensible Configuration out of the Box -->

![py3](https://img.shields.io/badge/python->=3.11.0-3776AB?logo=python&logoColor=FFFFFF&style=flat-square)
![pdm](https://img.shields.io/badge/depedency_manager-pdm-blueviolet?logoColor=FFFFFF&style=flat-square)
![pytest](https://img.shields.io/badge/test%20suite-pytest-0A9EDC?logo=pytest&logoColor=FFFFFF&style=flat-square)
![ruff](https://img.shields.io/badge/linter-ruff-006400?&style=flat-square)
![mypy](https://img.shields.io/badge/typechecker-mypy-blue?&style=flat-square)

![pyproject](https://img.shields.io/badge/pyproject.toml-000000?logo=python&style=flat-square)
![precommit](https://img.shields.io/badge/.pre--commit--config.yaml-000000?logo=precommit&style=flat-square)
![visualstudiocode](https://img.shields.io/badge/-.vscode/-000000?logo=visualstudiocode&logoColor=007ACC&style=flat-square)
![templates](https://img.shields.io/badge/Templates-000000?logo=github&logoColor=FFFFFF&style=flat-square)
<!-- ![editorconfig](https://img.shields.io/badge/-.editorconfig-000000?logo=editorconfig&style=flat-square) -->

![make](https://img.shields.io/badge/Makefile-FFFFFF?logo=gnu&logoColor=A42E2B&style=flat-square)
![ghactions](https://img.shields.io/badge/Github_Actions-FFFFFF?logo=githubactions&style=flat-square)
![conventionalcommits](https://img.shields.io/badge/Conventional%20Commits-FFFFFF?logo=conventionalcommits&style=flat-square)
<!-- ![docker](https://img.shields.io/badge/-Docker-FFFFFF?logo=docker&style=flat-square) -->
<!-- [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit&style=flat-square) -->
<!-- [![conventional-commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg&style=flat-square)](https://conventionalcommits.org&style=flat-square) -->

<!--
  - [`pyenv`](./.python-version)-->

<!-- [![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release) -->

  <!-- - `semantic-release` for automated versioning and changelog generation -->
<!-- - `commitizen` for version control and changelog generation -->

<!-- omit in toc
## Table of Contents
 -->

## Demo
>
[![asciicast](./docs/img/demo.svg)](https://asciinema.org/a/jJnVjjAALevmZBbgnWYGknz9b?autoplay=1&preload=1&loop=1)
<!-- omit in toc
TODO: embed as html to specify font family
 -->
### Quickstart

``` bash
git clone https://github.com/MultifokalHirn/python_template_repo.git
cd python_template_repo/

make bootstrap     # sets up virtual environment and installs pdm
make dev           # sets up dev environment and installs dependencies
make ci            # runs formatter, linter, typechecker, and tests
```

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for information on how to setup and contribute to this project.

### Features

- [x] [`pyproject.toml`](./pyproject.toml) with [`pdm`](https://pdm.fming.dev/) as dependency manager
- [x] Coverage Reporting and automated badge generation
- [x] [`Makefile`](./Makefile) with targets for common tasks like setting up the dev environment, running tests, and formatting code
- [x] Dev packages configured out of the box (in [`pyproject.toml`](./pyproject.toml))
- [x] `pre-commit` hooks in [`.pre-commit-config.yaml`](./.pre-commit-config.yaml)
- [x] Templates for [Issues](./.github/ISSUE_TEMPLATE.md) and [PRs](./.github/PULL_REQUEST_TEMPLATE.md) on GitHub
- [x] Github Actions for testing and linting
- [x] Dependabot config for automated dependency updates
- [x] Configuration for VSCode in [`.vscode/`](./.vscode)

## Roadmap

### Demo Project

- [ ] create demo project to showcase best practices and features

### Improve Documentation

- [ ] document project structure
- [ ] document pyenv
- [ ] expand list of tools I have tried and decided against

### Ideas for v2 Release

- [ ] set up tox for testing with multiple python versions
- [ ] set up Dockerfile
- [ ] docker-compose for easy setup of dev environment
- [ ] set up devcontainer
- [ ] set up commitizen
- [ ] set up semantic-release
- [ ] set up github actions for semantic versioning

<!-- ### Ideas for the Future

- [ ] find out how to sync templates with projects that use them? -->

## "Why don't you use X?"

> This template is meant to be a starting point for my own projects and may not follow other people's preferred setups.

Depending on the tool of configuration detail, I either actively decided against something or I have not yet tried them.

If you have any suggestions for improvements, or tools to check out, please [file an issue](https://github.com/MultifokalHirn/python_template_repo/issues).

### Tried and Decided Against

- `black` - I like configuring stuff
- `flake8` - replaced by `ruff`
- `autopep8` - replaced by `ruff`
- `isort` - replaced by `ruff`
- `poetry` - using `pdm` instead because of bad experience with `poetry`

### Currently in Evaluation

- `tox`
- `readthedocs`

## Troubleshooting

> In this section, you will find some common issues you might encounter and how to resolve them. If you are experiencing any issues that are not covered here, please [file an issue](https://github.com/MultifokalHirn/python_template_repo/issues).

### I does not work! I tried everything

Well, have you tried turning it off and on again?

## License

This project is authored by Lennard Wolf and open sourced under MIT license, see [`LICENSE`](./LICENSE) for details.

![License](https://img.shields.io/github/license/MultifokalHirn/python_template_repo)
