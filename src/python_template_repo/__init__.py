"""<your project name here>

<your project description here>
"""

# Local

# from . import _exceptions, _types
from .__metadata__ import __description__, __license__, __title__
from .__version__ import __version__

# Public Re-Exports
__all__ = [
    # "cli",
    # "utils",
    # "_exceptions",
    # "_types",
    "__title__",
    "__description__",
    "__version__",
    "__author__",
    "__license__",
]

"""
Deprecated public re-exports - these will be removed in a future release.

Example usage:

    ```python
    from python_template_repo import deprecated_reexport

    _deprecated: dict[str, Any] = {
        "deprecated_reexport": deprecated_reexport,
        ...
        }
    ```
"""
# _deprecated: dict[str, Any] = {}


# def __getattr__(name: str) -> Any:
#     if name in _deprecated:
#         import warnings

#         real = _deprecated[name]
#         warnings.warn(
#             message=f"{name} is deprecated, please use {real.__name__} instead",
#             category=DeprecationWarning,
#             stacklevel=2,
#         )
#         return real
#     raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
#
# __all__.extend(_deprecated)
