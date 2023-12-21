# For Contributors

Most of the setup is automated with `make`. Check the [`Makefile`](./Makefile) to learn more.

## Requirements

* `Python>=3.11`
* `make`:
  * macOS: `xcode-select --install`
  * Linux: visit [gnu.org](https://www.gnu.org/software/make)
  * Windows: `choco install make` or check [chocolatey.org](https://chocolatey.org/install)

## Setup

`make` will take care of setting a the virtual environment (it will be located in `.venv`). It will also install `pdm` and with it all dependencies.

Furthermore, it will install `pre-commit` hooks to run checks on staged changes before each commit and to enforce the commit message style.

``` bash
make bootstrap-dev
```

### Screencast

[![asciicast](https://asciinema.org/a/628233.svg)](https://asciinema.org/a/628233)

<!-- ### Setting up pre-commit hooks

[`pre-commit`](https://github.com/pre-commit/pre-commit) should be used to run checks on staged changes before each commit and to enforce the commit message style.

Before you start development, please install the hooks like so:

``` bash
pre-commit install && pre-commit install --hook-type commit-msg
``` -->

## Development
<!-- >
> In order to have notifications in your terminal on macOS, you can install a package for that like so:
> `brew install terminal-notifier` -->

To run all of the checks below (formatting, testing, linting, typechecks) run:

``` bash
make ci
```

### Static Analysis

`ornaments` uses `ruff` for formatting & linting and `mypy` for typechecks.

``` bash
make format   # ruff formatting and auto-fixes
make lint     # ruff checks
make mypy     # mypy
```

### Testing

To trigger `pytest` and `coverage` run the following:

``` bash
make test
```

This will also generate a coverage badge which is displayed in the README.

## Commit Message Style

A [uniform commit message style](https://commitizen-tools.github.io/commitizen/tutorials/writing_commits/)
and [here](https://www.conventionalcommits.org/en/v1.0.0/). for better readibilty shall be enforced to be able to generate a [changelog](./CHANGELOG.md).

### Allowed Prefixes

``` txt
fix:  feat:  docs:  style:  refactor:  perf:
test:  build:  ci:  chore:  revert:
```

### Example

``` bash
git commit -m "feat: adds support for new feature"
```
