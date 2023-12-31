import warnings
from collections.abc import Callable
from functools import wraps

from ornaments._exceptions import InvalidReturnTypeError
from ornaments._types import P, R
from ornaments._warnings import InvalidReturnTypeWarning


def checked_return_type(enforce: bool = False) -> Callable:
    """
    Checks that the return value of the function is of a specified type. If not, it raises an exception or raises a warning.

    # Example usage:

        @checked_return_type
        def my_function() -> int:
            return 1

    """

    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        expected_type = func.__annotations__.get("return")
        if expected_type is None:
            raise ValueError("Expected type must be specified in the function annotations.")

        @wraps(wrapped=func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | None:
            result = func(*args, **kwargs)

            if not isinstance(result, expected_type):
                msg = f"Function {func.__name__} returned object with wrong type. result={result}"
                if enforce is True:
                    raise InvalidReturnTypeError(msg)
                else:
                    warnings.warn(message=msg, category=InvalidReturnTypeWarning)

            return result

        return wrapper

    return decorator
