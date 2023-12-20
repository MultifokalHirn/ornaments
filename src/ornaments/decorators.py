import logging
from collections.abc import Callable
from functools import wraps
from typing import Any


def only_called_once(scope="object", enforce: bool = False):
    """
    Decorator that ensures a function is only called once in a given scope.

    # Example usage:
        class MyClass:
            @only_called_once(scope="object")
            def my_method(self):
                print("Called my_method")

            @only_called_once(scope="class")
            def my_class_method():
                print("Called my_class_method")

        @only_called_once(scope="session")
        def my_function():
            print("Called my_function")

    """
    if scope not in {"object", "class", "session"}:
        raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(wrapped=func)
        def wrapper(*args, **kwargs) -> Any:
            if scope == "object":
                # Use the id of the instance for object scope
                key = (id(args[0]), func)
            elif scope == "class":
                # Use the class of the instance for class scope
                key = (args[0].__class__, func)
            else:  # session scope
                # Use the function itself for session scope
                key = func

            called = getattr(wrapper, "called", set())
            if key not in called:
                called.add(key)
                setattr(wrapper, "called", called)
                return func(*args, **kwargs)
            else:
                msg = f"Function {func.__name__} has already been called in this {scope}."
                if enforce:
                    raise Exception(msg)
                else:
                    logging.error(msg=msg)

        return wrapper

    return decorator
