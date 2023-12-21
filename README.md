
<!-- markdownlint-disable -->
*****under construction*****

<p align="center">
  <!-- github-banner-start -->
    <h1><code>ornaments</code></h1>
  <!-- github-banner-end -->
</p>

<!-- markdownlint-restore -->
![GitHub last commit](https://img.shields.io/github/last-commit/MultifokalHirn/ornaments)
[![Tests](https://github.com/MultifokalHirn/ornaments/actions/workflows/python-checks.yaml/badge.svg?branch=main)](https://github.com/MultifokalHirn/ornaments/actions/workflows/python-checks.yaml)
![Coverage](./docs/img/coverage.svg)

<!-- ![GitHub issues](https://img.shields.io/github/issues/MultifokalHirn/ornaments)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/MultifokalHirn/ornaments) -->

`ornaments` helps to *future-proofly* document the intent of one's `python` code.

<img align="left" src="./docs/img/ornaments.png" width="100" height="100" />

It aims to do so through meaningful `@decorator` functions that help other developers understand, (re-)use, and debug your code.

<br clear="left"/>

<details>

<summary><h2>Contents</h2></summary>

- [Overview](#overview)
  - [Why decorators?](#why-decorators)
  - [Example](#example)
  - [Structure](#structure)
- [Addendum](#addendum)

</details>

## Overview

`ornaments` provides functionality for

- various value/type checks as well limiters during runtime
- various context-dependend logging functionalities (i.e. execution time)
- *testable* meta information (i.e. deprecation warnings)

### Why decorators?

A `@decorator` 'talks about' other code in a way that is <u>understandable for both the human reader *as well as* the interpreter</u>. By being meaningful to *both*, `@decorator` based documentation can bypass the (all to common) disconnect between documentation and code.

### Example

``` python
from ornaments.invariants import only_called_once

@only_called_once(scope="session", enforce=True)
def only_once_callable_function() -> None:
    return None

# -----

only_once_callable_function()
>>> None

# This should raise an error
only_once_callable_function()
>>> Traceback (most recent call last):
    File "<input>", line 1, in <module>
      only_once_callable_function()
    File "./ornaments/src/ornaments/invariants/only_called_once.py", line 45, in wrapper
      raise CalledTooOftenError(msg)
    ornaments.exceptions.CalledTooOftenError: Function only_once_callable_function has already been called in session. call_scope=(4522676512, <function only_once_callable_function at 0x10d929120>)
```

<!-- <img width="1421" alt="Screenshot 2023-12-21 at 01 48 35" src="https://github.com/MultifokalHirn/ornaments/assets/7870758/8fce40d2-65e4-4c1f-8077-d5eb40641bc5"> -->

### Structure

``` txt
ornaments/
├── exceptions.py
├── scopes.py
│
├── helpers/
│   ├── log_execution_time.py
│   ├── log_parameters.py
│   └── retry.py
│
├── invariants/
│   └── only_called_once.py
│
├── limiters/
│   └── execution_time_limit.py
│
├── markers/
│   └── deprecated.py
│
└──  runtime_checks
    ├── parameter_validation.py
    └── return_type_validation.py

```

## Addendum
>
> See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for information on how to setup and contribute to this project.

![License](https://img.shields.io/github/license/MultifokalHirn/ornaments)

<img align="center" src="./docs/img/o1.png" width="100" height="100" />
<img align="center" src="./docs/img/o2.png" width="100" height="100" />
<img align="center" src="./docs/img/oran.png" width="100" height="100" />
<br />
<br />

**Author -** [`MultifokalHirn`](github.com/MultifokalHirn)
