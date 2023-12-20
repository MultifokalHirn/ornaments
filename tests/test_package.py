from __future__ import annotations


def test_metadata() -> None:
    from python_template_repo.__metadata__ import __description__, __license__, __title__

    # assert __author__ is not None
    assert __description__ is not None
    assert __license__ is not None
    assert __title__ is not None


def test_version() -> None:
    from python_template_repo.__version__ import __version__

    assert __version__ is not None


# def test_deprecated_export() -> None:
#     import python_template_repo

#     if hasattr(python_template_repo, "deprecated_reexport"):
#         assert python_template_repo.deprecated_reexport is not None
