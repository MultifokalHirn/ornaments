# """
# Configure the logger with a structured JSON log format.
# """

# import logging
# import sys
# from logging import StreamHandler
# from typing import cast

# import structlog
# from structlog.stdlib import BoundLogger, LoggerFactory, add_log_level, filter_by_level


# def setup_logger(*, logger_name: str, log_level: int = logging.INFO) -> BoundLogger:
#     """
#     Set up the logger object to use in your code.

#     ..  code-block:: python
#         :caption: Minimal example

#         from src.logging import setup_logger
#         LOG = setup_logger(logger_name=__name__)

#         # ... later in the code ...
#         LOG.info(
#             "log message",
#             some_key="some value",
#             another_key=True,
#         )
#     """
#     _setup_structlog()
#     logger = cast(BoundLogger, structlog.get_logger(logger_name))
#     logger.setLevel(log_level)
#     if not logger.new()._logger.handlers:
#         logger.addHandler(_configure_logger_handlers())
#     return logger


# def set_logger_level(*, logger: BoundLogger, level: str) -> None:
#     """
#     Allow to set a new logging level by name for an existing logger.

#     ..  code-block:: python
#         :caption: Minimal example

#         from src.logging import set_logger_level

#         # ... in the entry point ...
#         set_logger_level(logger=LOG, level="DEBUG")
#     """
#     # NOTE: level is not further refined with a Literal of allowed strings due
#     # to the dynamic nature of logging levels.
#     clean_level = level.upper()
#     numeric_level = getattr(logging, clean_level)
#     logger.setLevel(numeric_level)
#     logger.info("Log level changed", new_level=clean_level, new_level_numeric=numeric_level)


# def _configure_logger_handlers() -> StreamHandler:  # type: ignore
#     """Internal helper to add handlers."""
#     logger_handler = StreamHandler(sys.stdout)
#     return logger_handler


# def _setup_structlog() -> None:
#     """
#     Internal helper to configure structlog.

#     For further details look at https://www.structlog.org/en/stable/
#     """
#     if structlog.is_configured():
#         return

#     structlog.configure(
#         processors=[
#             filter_by_level,
#             add_log_level,
#             structlog.processors.StackInfoRenderer(),
#             structlog.processors.format_exc_info,
#             structlog.processors.UnicodeDecoder(),
#             structlog.processors.TimeStamper(fmt="iso"),
#             structlog.processors.JSONRenderer(sort_keys=False),
#         ],
#         logger_factory=LoggerFactory(),
#         wrapper_class=BoundLogger,
#         cache_logger_on_first_use=True,
#     )
