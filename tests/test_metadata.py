from __future__ import annotations


def test_metadata() -> None:
    from ornaments.__metadata__ import __description__, __license__, __title__

    # assert __author__ is not None
    assert __description__ is not None
    assert __license__ is not None
    assert __title__ is not None


def test_version() -> None:
    from ornaments.__version__ import __version__

    assert __version__ is not None


# def test_deprecated_export() -> None:
#     import ornaments

#     if hasattr(ornaments, "deprecated_reexport"):
#         assert ornaments.deprecated_reexport is not None
