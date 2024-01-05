# catch_exceptions(default_return_value=None): Catches any exceptions thrown by the decorated function and optionally returns a default value. This can be useful for making your code more robust against unexpected errors.

from collections.abc import Callable
from functools import wraps
from typing import Any

from ornaments._types import P, R
from ornaments._warnings import UncaughtExceptionWarning

# def catch_exception(function: Callable[P, T]) -> Callable[P, Optional[T]]:
#     def decorator(*args: P.args, **kwargs: P.kwargs) -> Optional[T]:
#         try:
#             return function(*args, **kwargs)
#         except Exception:
#             return None

#     return decorator


def catch_exceptions(
    exceptions: list[type[BaseException]] = [BaseException], fallback_return: Any | None = None, warn_uncaught: bool = False
) -> Callable[P, R | Any | None]:
    def decorator(func: Callable[P, R]) -> Callable[P, R | Any | None]:
        @wraps(wrapped=func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | Any | None:
            try:
                return func(*args, **kwargs)
            except BaseException as e:
                if type(e) not in exceptions and not any([issubclass(e_type, type(e)) for e_type in exceptions]):
                    if not warn_uncaught:
                        raise e
                    raise e from UncaughtExceptionWarning(f"Uncaught exception in {func.__name__} ({type(e)}): {e} ")
                return fallback_return

        return wrapper

    return decorator
