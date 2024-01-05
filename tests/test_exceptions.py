import pytest
from ornaments._exceptions import OrnamentsException
from ornaments._warnings import UncaughtExceptionWarning


def test_uncaught_exception_warning() -> None:
    def my_erroneous_method() -> None:
        raise OrnamentsException("This is an error message")

    with pytest.raises(OrnamentsException):
        try:
            my_erroneous_method()
        except OrnamentsException as e:
            raise e from UncaughtExceptionWarning(f"Uncaught exception ({type(e)}): {e}")
