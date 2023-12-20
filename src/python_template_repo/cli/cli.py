# import contextlib
# import logging
# import warnings
# from collections.abc import Iterator
# from tempfile import mktemp
# from typing import Any

# from pyboxen import boxen
# from rich.console import Console
# from rich.progress import Progress, ProgressColumn

# from .._types import RichProtocol, Spinner
# from .config import LOG_LEVELS, Verbosity, _console, _err_console
# from .spinner import SPINNER, DummySpinner

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.NullHandler())


# def is_interactive(console: Console | None = None) -> bool:
#     """Check if the terminal is run under interactive mode"""
#     if console is None:
#         console = _console
#     return console.is_interactive


# class CLI:
#     """Terminal UI object"""

#     def __init__(self, verbosity: Verbosity = Verbosity.NORMAL) -> None:
#         self.verbosity = verbosity

#     def set_verbosity(self, verbosity: int) -> None:
#         self.verbosity = Verbosity(verbosity)
#         if self.verbosity == Verbosity.QUIET:
#             warnings.simplefilter("ignore", FutureWarning, append=True)

#     def echo(
#         self,
#         message: str | RichProtocol = "",
#         err: bool = False,
#         verbosity: Verbosity = Verbosity.QUIET,
#         **kwargs: Any,
#     ) -> None:
#         """print message using rich console

#         :param message: message with rich markup, defaults to "".
#         :param err: if true print to stderr, defaults to False.
#         :param verbosity: verbosity level, defaults to QUIET.
#         """
#         if self.verbosity >= verbosity:
#             console = _err_console if err else _console
#             if not console.is_interactive:
#                 kwargs.setdefault("crop", False)
#                 kwargs.setdefault("overflow", "ignore")

#             console.print(boxen(message, title="CLI", subtitle="", padding=2, subtitle_alignment="right"), **kwargs)

#     @contextlib.contextmanager
#     def logging(self, type_: str = "install") -> Iterator[logging.Logger]:
#         """A context manager that opens a file for logging when verbosity is NORMAL or
#         print to the stdout otherwise.
#         """
#         file_name: str | None = None
#         if self.verbosity >= Verbosity.DETAIL:
#             handler: logging.Handler = logging.StreamHandler()
#             handler.setLevel(LOG_LEVELS[self.verbosity])
#         else:
#             file_name = mktemp(".log")
#             handler = logging.FileHandler(file_name, encoding="utf-8")
#             handler.setLevel(logging.DEBUG)
#         handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
#         logger.addHandler(handler)

#         try:
#             yield logger
#         except Exception:
#             if self.verbosity < Verbosity.DETAIL:
#                 logger.exception("Error occurs")
#                 self.echo(
#                     f"See [warning]{file_name}[/] for detailed debug log.",
#                     style="error",
#                     err=True,
#                 )
#             raise
#         finally:
#             logger.removeHandler(handler)
#             handler.close()

#     def open_spinner(self, title: str) -> Spinner:
#         """Open a spinner as a context manager."""
#         if self.verbosity >= Verbosity.DETAIL or not is_interactive():
#             return DummySpinner(title)
#         else:
#             return _err_console.status(title, spinner=SPINNER, spinner_style="primary")  # type: ignore

#     def make_progress(self, *columns: str | ProgressColumn, **kwargs: Any) -> Progress:
#         """create a progress instance for indented spinners"""
#         return Progress(
#             *columns,
#             console=_console,
#             disable=self.verbosity >= Verbosity.DETAIL,
#             **kwargs,
#         )

#     def info(self, message: str, verbosity: Verbosity = Verbosity.QUIET) -> None:
#         """Print a message to stdout."""
#         self.echo(f"[info]INFO:[/] [dim]{message}[/]", err=True, verbosity=verbosity)

#     def warn(self, message: str, verbosity: Verbosity = Verbosity.QUIET) -> None:
#         """Print a message to stdout."""
#         self.echo(f"[warning]WARNING:[/] {message}", err=True, verbosity=verbosity)

#     def error(self, message: str, verbosity: Verbosity = Verbosity.QUIET) -> None:
#         """Print a message to stdout."""
#         self.echo(f"[error]WARNING:[/] {message}", err=True, verbosity=verbosity)
