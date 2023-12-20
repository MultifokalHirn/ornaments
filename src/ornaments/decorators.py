import logging
from collections.abc import Callable
from functools import wraps
from typing import Any

"""
#TODO: Add more decorators:

"""


def log_parameters(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    This decorator logs the parameters with which a function is called. The logging level (e.g., debug, info, warning) can be specified.

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
            pass

        return wrapper

    return decorator


def time_execution(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    Measures and logs the execution time of a function. This is useful for performance monitoring.

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
            pass

        return wrapper

    return decorator


def validate_parameters(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    Checks the parameters against a provided validation function or a set of rules before executing the function. If the parameters don't meet the criteria, it can raise an exception or log a warning.


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
            pass

        return wrapper

    return decorator


def checked_return_type(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    Checks that the return value of the function is of a specified type. If not, it raises an exception or logs a warning.

    # Example usage:
        class MyClass:
            @checked_return_type(scope="object")
            def my_method(self):
                print("Called my_method")

            @checked_return_type(scope="class")
            def my_class_method():
                print("Called my_class_method")

        @checked_return_type(scope="session")
        def my_function():
            print("Called my_function")

    """
    if scope not in {"object", "class", "session"}:
        raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(wrapped=func)
        def wrapper(*args, **kwargs) -> Any:
            pass

        return wrapper

    return decorator


def deprecate_function(replacement: Callable) -> Callable[..., Callable[..., Any]]:
    """
    Marks a function as deprecated. It can log a warning whenever the function is called and optionally suggest a replacement function.

    # Example usage:
        class MyClass:
            @deprecate_function(scope="object")
            def my_method(self):
                print("Called my_method")

            @deprecate_function(scope="class")
            def my_class_method():
                print("Called my_class_method")

        @deprecate_function(scope="session")
        def my_function():
            print("Called my_function")

    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(wrapped=func)
        def wrapper(*args, **kwargs) -> Any:
            pass

        return wrapper

    return decorator


def retry_on_exception(exception: Exception, max_retries: int = 3) -> Callable[..., Callable[..., Any]]:
    """
    Automatically retries a function if it raises a specified exception. The number of retries can be limited.

    # Example usage:
        class MyClass:
            @retry_on_exception(scope="object")
            def my_method(self):
                print("Called my_method")

            @retry_on_exception(scope="class")
            def my_class_method():
                print("Called my_class_method")

        @retry_on_exception(scope="session")
        def my_function():
            print("Called my_function")

    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(wrapped=func)
        def wrapper(*args, **kwargs) -> Any:
            pass

        return wrapper

    return decorator


def only_called_once(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
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
