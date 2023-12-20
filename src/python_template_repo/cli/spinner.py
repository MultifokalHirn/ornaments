# from typing import Any

# from .._types import SpinnerT
# from .config import _err_console

# SPINNER = "dots"


# class DummySpinner:
#     """A dummy spinner class implementing needed interfaces.
#     But only display text onto screen.
#     """

#     def __init__(self, text: str) -> None:
#         self.text = text

#     def _show(self) -> None:
#         _err_console.print(f"[primary]STATUS:[/] {self.text}")

#     def update(self, text: str) -> None:
#         self.text = text
#         self._show()

#     def __enter__(self: SpinnerT) -> SpinnerT:
#         self._show()  # type: ignore[attr-defined]
#         return self

#     def __exit__(self, *args: Any) -> None:
#         pass


# class SilentSpinner(DummySpinner):
#     def _show(self) -> None:
#         pass
