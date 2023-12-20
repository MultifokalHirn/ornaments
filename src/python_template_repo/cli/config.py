# import enum
# import logging

# from rich.console import Console
# from rich.theme import Theme

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.NullHandler())


# DEFAULT_THEME: dict[str, str] = {
#     "primary": "cyan",
#     "success": "green",
#     "warning": "yellow",
#     "error": "red",
#     "info": "blue",
#     "req": "bold green",
# }

# _console = Console(highlight=False, theme=Theme(DEFAULT_THEME))
# _err_console = Console(stderr=True, theme=Theme(DEFAULT_THEME))


# class Verbosity(enum.IntEnum):
#     QUIET = -1
#     NORMAL = 0
#     DETAIL = 1
#     DEBUG = 2


# LOG_LEVELS = {
#     Verbosity.NORMAL: logging.WARN,
#     Verbosity.DETAIL: logging.INFO,
#     Verbosity.DEBUG: logging.DEBUG,
# }
