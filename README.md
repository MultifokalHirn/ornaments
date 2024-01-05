
<!-- markdownlint-disable -->

<p align="center">
  <!-- github-banner-start -->
    <h1><code>ornaments</code></h1>
  <!-- github-banner-end -->
</p>

<!-- markdownlint-restore -->
[![Maturity badge - level 1](https://img.shields.io/badge/Maturity-Level%201%20--%20New%20Project-yellow.svg)](https://github.com/tophat/getting-started/blob/master/scorecard.md)
[![Tests](https://github.com/MultifokalHirn/ornaments/actions/workflows/python-checks.yaml/badge.svg?branch=main)](https://github.com/MultifokalHirn/ornaments/actions/workflows/python-checks.yaml)
![Coverage](./docs/img/coverage.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/MultifokalHirn/ornaments)
<!-- ![GitHub issues](https://img.shields.io/github/issues/MultifokalHirn/ornaments)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/MultifokalHirn/ornaments) -->
<img align="right" src="./docs/img/ornaments.png" width="100" height="100" />
`ornaments` helps to *future-proofly* document the intent of one's `python` code.

It aims to do so through meaningful `@decorator` functions that help other developers understand, (re-)use, and debug your code.

<br clear="left"/>

<!-- <details><summary><h2>Contents</h2></summary> -->

<h2>Contents</h2>

- [Overview](#overview)
  - [Why decorators?](#why-decorators)
  - [Scope](#scope)
- [Usage](#usage)
  - [But what if I want to use the same function in different contexts? 🤔](#but-what-if-i-want-to-use-the-same-function-in-different-contexts-)
- [Goal Structure](#goal-structure)
- [Development](#development)

<!-- </details> -->

## Overview

### Why decorators?

A `@decorator` 'talks about' other code in a way that is <u>understandable for both the human reader *as well as* the interpreter</u>. By being meaningful to *both*, `@decorator` based documentation can bypass the (all to common) disconnect between documentation and code.

### Scope

`ornaments` provides functionality for adding various

- value/type checks (as well limiters for input/execution duration) during runtime
- context-dependend logging functionalities (i.e. execution time)
- *testable* meta information (i.e. deprecation warnings)

## Usage

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
    ornaments._exceptions.CalledTooOftenError: Function only_once_callable_function has already been called in session. call_scope=(4522676512, <function only_once_callable_function at 0x10d929120>)
```

### But what if I want to use the same function in different contexts? 🤔

``` python
from ornaments.invariants import only_called_once

def my_reusable_function() -> None:
    return None

@only_called_once(scope="session", enforce=True)
def only_once_callable_function() -> None:
    return my_reusable_function()

# -----

my_reusable_function()
>>> None

my_reusable_function()
>>> None

only_once_callable_function()
>>> None

# This should raise an error
only_once_callable_function()
>>> Traceback (most recent call last):
    File "<input>", line 1, in <module>
      only_once_callable_function()
    File "./ornaments/src/ornaments/invariants/only_called_once.py", line 45, in wrapper
      raise CalledTooOftenError(msg)
      ...
```

<!-- <img width="1421" alt="Screenshot 2023-12-21 at 01 48 35" src="https://github.com/MultifokalHirn/ornaments/assets/7870758/8fce40d2-65e4-4c1f-8077-d5eb40641bc5"> -->
🚀

<!-- ## Ideas

``` python
if [typecheck | boolcheck | truthycheck | positivecheck | ...] and [raise | log | ...] error
```

. -->

## Goal Structure

``` txt
ornaments
├── helpers
│   ├── catch_all_exceptions.py
│   ├── normalized_exceptions.py
│   └── retry.py
├── invariants
│   ├── conditional_execution.py
│   └── only_called_once.py
├── limits
│   ├── call_limit.py
│   └── execution_time_limit.py
├── logging
│   ├── log_calls.py
│   ├── log_execution_time.py
│   ├── log_parameters.py
│   ├── log_return.py
│   └── log_value.py
├── markers
│   ├── stable.py
│   ├── wobbly.py
│   └── deprecated.py
├── monitoring
│   ├── monitored_attribute.py
│   └── monitored_calls.py
├── runtime_checks
│   ├── checked_return_type.py
│   └── parameter_validation.py
└── safety
    └── fallback_function.py
```

## Development
>
> See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for information on how to setup and contribute to this project.

[![asciicast](https://asciinema.org/a/628233.svg)](https://asciinema.org/a/628233)

<h2> Addendum </h2>

![License](https://img.shields.io/github/license/MultifokalHirn/ornaments)

<div>
  <img align="center" src="./docs/img/o1.png" width="100" height="100" />
  <img align="center" src="./docs/img/o2.png" width="100" height="100" />
  <img align="center" src="./docs/img/oran.png" width="100" height="100" />
</div>
<br />

``` txt
           .::=+=--++=::.
       .-+++*-+++ =*+*=++=-:
     :+#+-=:-.:+--+++=.=+:=**=.
   .+#==::--+#*-...:=%%+-:**==*=
  .@%=*=+:*#*.       .#@#-==-==-*.
  #@--+=-##::          %@#=:=:+::=
 -@@:==+:%+-.          =@=:++=:: -.
 *@@:-==:%*-.          =@*+=+-+-.-.
 :@@:.-==+@%-          %@===+==: =.
  #@-++-=--#%=       :%%----=:. :=
   #@=.:-:+++++==:--++=.::=++..:+
   :*%#*=:*+: -==:#%#*.==+::..--
   ::-+**=++-:=--.*%%%==--.:::.
        :--:==-:--:--:-:::::
            . . :  : ...
```

<br />

**Author -** [`MultifokalHirn`](https://github.com/MultifokalHirn)
