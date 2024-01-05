# catch_exceptions(default_return_value=None): Catches any exceptions thrown by the decorated function and optionally returns a default value. This can be useful for making your code more robust against unexpected errors.


import pytest
from ornaments._exceptions import OrnamentsException
from ornaments._warnings import UncaughtExceptionWarning
from ornaments.helpers import catch_exceptions


def test_uncaught() -> None:
    @catch_exceptions(exceptions=[])
    def my_erroneous_method() -> None:
        raise OrnamentsException("Error")

    with pytest.raises(expected_exception=OrnamentsException):
        my_erroneous_method()


def test_uncaught_warning() -> None:
    @catch_exceptions(exceptions=[], warn_uncaught=True)
    def my_erroneous_method() -> None:
        raise OrnamentsException("Error")

    with pytest.raises(expected_exception=OrnamentsException):
        with pytest.warns(expected_warning=UncaughtExceptionWarning):
            my_erroneous_method()


def test_caught() -> None:
    @catch_exceptions(exceptions=[OrnamentsException])
    def my_erroneous_method() -> None:
        raise OrnamentsException("Error")

    my_erroneous_method()
