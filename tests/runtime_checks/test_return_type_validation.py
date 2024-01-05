import pytest
from ornaments._exceptions import InvalidReturnTypeError
from ornaments._warnings import InvalidReturnTypeWarning
from ornaments.runtime_checks import checked_return_type


def test_checked_return_type_enforce_true() -> None:
    @checked_return_type(enforce=True)
    def correct_function() -> int:
        return 1

    assert correct_function() == 1

    @checked_return_type(enforce=True)
    def erroneous_function() -> str:
        return 1  # type: ignore

    with pytest.raises(InvalidReturnTypeError):
        erroneous_function()


def test_checked_return_type_enforce_false() -> None:
    @checked_return_type(enforce=False)
    def correct_function() -> int:
        return 1

    assert correct_function() == 1

    @checked_return_type(enforce=False)
    def erroneous_function() -> str:
        return 1  # type: ignore

    with pytest.warns(InvalidReturnTypeWarning):
        erroneous_function()


def test_checked_return_type_without_return_type() -> None:
    with pytest.raises(ValueError):

        @checked_return_type(enforce=False)
        def function_without_return_type():
            return 1
