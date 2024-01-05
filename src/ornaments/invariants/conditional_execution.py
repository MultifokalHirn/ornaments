from collections.abc import Callable
from functools import wraps
from typing import ParamSpec

from ornaments._types import Decorator, P, R

C = ParamSpec("C")

# def only_callable_if(condition_func: Callable[C, bool], enforce: bool = False) -> Callable[[Callable[P, R]], Callable[P, R]]:
#     """
#     Decorator that ensures a function is only called once in a given scope.

#     Example usage:

#     ```python
#         from ornaments.invariants import only_callable_if

#         class MyClass:
#             my_condition: bool

#             def __init__(self, my_condition: bool = False):
#                 self.my_condition = my_condition

#             @only_callable_if(condition_func=lambda self: self.my_condition, enforce=True)
#             def maybe_do_something(self) -> None:
#                 print("Did something!")

#     ```
#     """

#     def decorator(func: Callable[P, R]) -> Callable[P, R]:
#         @wraps(wrapped=func)
#         def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
#             if condition_func(*args: C.args, **kwargs: C.kwargs) is True:
#                 return func(*args, **kwargs)
#             return func(*args, **kwargs)

#         return wrapper

#     return decorator


def not_called_if(condition_func: Callable[[], bool], warn: bool = False) -> Decorator:
    """
    Decorator that ensures a function is only called if a provided condition function returns True.

    Example usage:

    ```python
        from ornaments.invariants import not_called_if

        class MyClass:
            my_condition: bool

            def __init__(self, my_condition: bool = False):
                self.my_condition = my_condition

            @not_called_if(condition_func=lambda self: self.my_condition)
            def maybe_do_something(self) -> None:
                print("Did something!")

    ```
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        @wraps(wrapped=func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | None:
            if condition_func() is True:
                return func(*args, **kwargs)
            return None

        return wrapper

    return decorator
