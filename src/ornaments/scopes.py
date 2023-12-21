from typing import Final

CLASS_SCOPE: Final[set[str]] = {"class"}
SESSION_SCOPE: Final[set[str]] = {"session"}
OBJECT_SCOPE: Final[set[str]] = {"instance", "object"}
ALL_SCOPES: Final[set[str]] = CLASS_SCOPE | SESSION_SCOPE | OBJECT_SCOPE
