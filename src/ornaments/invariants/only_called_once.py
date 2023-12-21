import warnings
from collections.abc import Callable
from functools import wraps
from typing import Any

from ..exceptions import CalledTooOftenError, CalledTooOftenWarning
from ..scopes import CLASS_SCOPE, OBJECT_SCOPE, SESSION_SCOPE


def only_called_once(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    Decorator that ensures a function is only called once in a given scope.

    Example usage:

    ```python
        @only_called_once(scope="session", enforce=True)
        def my_function() -> str:
            return "Called my_function"

    ```
    """

    def decorator(func: Callable) -> Callable:
        @wraps(wrapped=func)
        def wrapper(*args, **kwargs) -> Any:
            if scope in OBJECT_SCOPE:
                # Use the id of the instance for object scope
                call_scope = (id(args[0]), func)
            elif scope in CLASS_SCOPE:
                # Use the class as identifier for session scope
                # Note: only really useful if the class itself is instantiated more than once
                # - otherwise, this will behave just as session scope
                call_scope = (args[0].__class__, func)
            elif scope in SESSION_SCOPE:  # session scope
                # Use the function itself as identifier for session scope
                call_scope = (func,)
            else:
                raise ValueError(f"Invalid scope. Must be one of {OBJECT_SCOPE | CLASS_SCOPE | SESSION_SCOPE}.")

            calls_in_scope: set[Any | tuple[Any]] = getattr(wrapper, "calls_in_scope", set())
            if call_scope in calls_in_scope:
                msg = f"Function {func.__name__} has already been called in {scope}. call_scope={call_scope}"
                if enforce is True:
                    raise CalledTooOftenError(msg)
                else:
                    warnings.warn(message=msg, category=CalledTooOftenWarning)
            else:
                calls_in_scope.add(call_scope)
                setattr(wrapper, "calls_in_scope", calls_in_scope)
                return func(*args, **kwargs)

        return wrapper

    return decorator
