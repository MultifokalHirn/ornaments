# from typing import TYPE_CHECKING

# if TYPE_CHECKING or True:  # TODO: find out why TYPE_CHECKING breaks code in runtime
#     from typing import Any, Protocol, TypeVar

#     class RichProtocol(Protocol):
#         """
#         Protocol for classes that can be rendered by Rich.

#         class MyRichClass(NamedTuple):
#             name: str
#             secret: str | None = None

#             def __rich__(self) -> str:
#                 lines: list[str] = []
#                 lines.append(f"[primary]name[/] = {self.name}")
#                 if self.secret is not None:
#                     lines.append(f"[error]secret[/] = {self.secret}")
#                 return "\n".join(lines)
#         """

#         def __rich__(self) -> str:
#             ...

#     SpinnerT = TypeVar("SpinnerT", bound="Spinner")

#     class Spinner(Protocol):
#         """
#         Protocol for classes that can be used as spinners in Rich.
#         """

#         def update(self, text: str) -> None:
#             ...

#         def __enter__(self: SpinnerT) -> SpinnerT:
#             ...

#         def __exit__(self, *args: Any) -> None:
#             ...
