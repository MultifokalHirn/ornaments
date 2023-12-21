from typing import Final

CLASS_SCOPE: Final[set] = {"class"}
SESSION_SCOPE: Final[set] = {"session"}
OBJECT_SCOPE: Final[set] = {"instance", "object"}
ALL_SCOPES: Final[set] = CLASS_SCOPE | SESSION_SCOPE | OBJECT_SCOPE
