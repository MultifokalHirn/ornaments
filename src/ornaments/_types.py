from typing import ParamSpec, TypeVar

# P = TypeVar("P")  # Parameter type
P = ParamSpec("P")
R = TypeVar("R", covariant=True)  # Return type
