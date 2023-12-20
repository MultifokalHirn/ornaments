"""Single-Source of Truth Package Versioning and Metadata.

We the `pyproject.toml` file as a single-source of truth for the package metadata.
As such, rather than duplicating the metadata in code here, it is retrieved
from the installed package metadata at runtime.
"""

from importlib import metadata

# Retrieve Metadata from Package
__title__: str = metadata.metadata(distribution_name=__package__)["name"]
__description__: str = metadata.metadata(distribution_name=__package__)["summary"]
__author__: str = "Lennard Wolf"  # pragma: no cover
__license__: str = metadata.metadata(distribution_name=__package__)["license"]  # pragma: no cover
# __version__: str = metadata.metadata(__package__)["version"] # TODO
