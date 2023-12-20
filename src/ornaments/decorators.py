import warnings
from collections.abc import Callable
from functools import wraps
from typing import Any, Final

from ._exceptions import CalledTooOftenError, CalledTooOftenWarning

CLASS_SCOPE: Final[set] = {"class"}
SESSION_SCOPE: Final[set] = {"session"}
OBJECT_SCOPE: Final[set] = {"instance", "object"}
ALL_SCOPES: Final[set] = CLASS_SCOPE | SESSION_SCOPE | OBJECT_SCOPE

# def log_parameters(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     This decorator logs the parameters with which a function is called. The logging level (e.g., debug, info, warning) can be specified.

#     # Example usage:
#         class MyClass:
#             @only_called_once(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @only_called_once(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @only_called_once(scope="session")
#         def my_function():
#             print("Called my_function")

#     """
#     if scope not in ALL_SCOPES:
#         raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


# def time_execution(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Measures and logs the execution time of a function. This is useful for performance monitoring.

#     # Example usage:
#         class MyClass:
#             @only_called_once(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @only_called_once(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @only_called_once(scope="session")
#         def my_function():
#             print("Called my_function")

#     """
#     if scope not in ALL_SCOPES:
#         raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


# def validate_parameters(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Checks the parameters against a provided validation function or a set of rules before executing the function. If the parameters don't meet the criteria, it can raise an exception or log a warning.


#     # Example usage:
#         class MyClass:
#             @only_called_once(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @only_called_once(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @only_called_once(scope="session")
#         def my_function():
#             print("Called my_function")

#     """
#     if scope not in ALL_SCOPES:
#         raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


# def checked_return_type(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Checks that the return value of the function is of a specified type. If not, it raises an exception or logs a warning.

#     # Example usage:
#         class MyClass:
#             @checked_return_type(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @checked_return_type(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @checked_return_type(scope="session")
#         def my_function():
#             print("Called my_function")

#     """
#     if scope not in ALL_SCOPES:
#         raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


# def deprecate_function(replacement: Callable) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Marks a function as deprecated. It can log a warning whenever the function is called and optionally suggest a replacement function.

#     # Example usage:
#         class MyClass:
#             @deprecate_function(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @deprecate_function(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @deprecate_function(scope="session")
#         def my_function():
#             print("Called my_function")

#     """

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


# def retry_on_exception(exception: Exception, max_retries: int = 3) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Automatically retries a function if it raises a specified exception. The number of retries can be limited.

#     # Example usage:
#         class MyClass:
#             @retry_on_exception(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @retry_on_exception(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @retry_on_exception(scope="session")
#         def my_function():
#             print("Called my_function")

#     """

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator


def only_called_once(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
    """
    Decorator that ensures a function is only called once in a given scope.

    Example usage:

    ```python
        class MyClass:
            @only_called_once(scope="object", enforce=True)
            def my_method(self) -> str:
                return "Called my_method"

            @only_called_once(scope="class", enforce=True)
            def my_class_scope_method(self) -> str:
                # only applicable if the class itself is instantiated more than once
                return "Called my_class_scope_method"


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
