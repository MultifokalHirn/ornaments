from collections.abc import Callable
from typing import Any, ParamSpec, TypeAlias, TypeVar

# Params = ParamSpec("Params")
# ReturnType = TypeVar("ReturnType", covariant=True)

P = ParamSpec("P")
R = TypeVar("R", covariant=True)  # Return type
AltR: TypeAlias = Any | None

# Decoratable: TypeAlias = Callable[Params, ReturnType]
Decoratable: TypeAlias = Callable[P, R]
AlteredDecoratable: TypeAlias = Callable[P, R | AltR]

Decorator = Callable[[Decoratable], Decoratable]
D = ParamSpec("D")  # DecoratorParams
# DecoratorParams = ParamSpec("DecoratorParams")
