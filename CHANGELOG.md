## Unreleased

### Feat

- add devcontainer.json, configure dependabot, minor fixes

### Fix

- template shouldn't give access to itself

## 1.0.0 (2023-11-15)

### Feat

- adds pdm based dependencies

### Fix

- more trying to get makefile to work in github actions; ruff replaces flake8 and "autopep8"
- misc fixes, starting to work in tox.ini
- dont install pdm again after bootstrapping; fix import bug
- try to get tests to work for 3.8
- pdm cofniguration did not work on systems without a system wide pdm
- readme
- update vscode workspace settings to reflect deprecations
- getting app module to be callable
- import logic in submodules, fixed linting issues
