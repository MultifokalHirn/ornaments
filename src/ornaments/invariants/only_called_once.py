import warnings
from functools import wraps
from typing import Any
from collections.abc import Callable

from .._types import P, R
from ..exceptions import CalledTooOftenError, CalledTooOftenWarning
from ..scopes import CLASS_SCOPE, OBJECT_SCOPE, SESSION_SCOPE


def only_called_once(scope: str = "object", enforce: bool = False) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that ensures a function is only called once in a given scope.

    Example usage:

    ```python
        from ornaments.invariants import only_called_once

        @only_called_once(scope="session", enforce=True)
        def only_callable_once() -> str:
            return "First!"

    ```
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(wrapped=func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if scope in OBJECT_SCOPE:
                # Use the id of the instance for object scope
                call_scope = (id(args[0]), func)
            elif scope in CLASS_SCOPE:
                # Use the class as identifier for session scope
                # Note: only really useful if the class itself is instantiated more than once
                # - otherwise, this will behave just as session scope
                call_scope = (id(args[0].__class__), func)
            elif scope in SESSION_SCOPE:  # session scope
                # Use the function itself as identifier for session scope
                call_scope = (id(func), func)
            else:
                raise ValueError(f"Invalid scope. Must be one of {OBJECT_SCOPE | CLASS_SCOPE | SESSION_SCOPE}.")

            previous_call_scopes: set[Any | tuple[Any]] = getattr(wrapper, "calls_in_scope", set())
            if call_scope in previous_call_scopes:
                msg = f"Function {func.__name__} has already been called in {scope}. call_scope={call_scope}"
                if enforce is True:
                    raise CalledTooOftenError(msg)
                else:
                    warnings.warn(message=msg, category=CalledTooOftenWarning)
            previous_call_scopes.add(call_scope)
            setattr(wrapper, "calls_in_scope", previous_call_scopes)
            return func(*args, **kwargs)

        return wrapper

    return decorator
