import pytest
from ornaments.exceptions import CalledTooOftenError, CalledTooOftenWarning
from ornaments.invariants import only_called_once

# ---------------------------------------------------------------
# enforce=False (default)
# ---------------------------------------------------------------


class SomeRestrictedClassUnenforced:
    @only_called_once(scope="object")
    def callable_once_per_instanceA(self) -> str:
        return "callable_once_per_instanceA"

    @only_called_once(scope="instance")
    def callable_once_per_instanceB(self) -> str:
        return "callable_once_per_instanceB"

    @only_called_once(scope="class")
    def callable_once_per_class(self) -> str:
        return "callable_once_per_class"


@only_called_once(scope="session")
def only_once_callable_function_unenforced() -> str:
    return "only_once_callable_function"


def test_object_scope_unenforced() -> None:
    obj = SomeRestrictedClassUnenforced()
    assert obj.callable_once_per_instanceA() == "callable_once_per_instanceA"
    with pytest.warns(expected_warning=CalledTooOftenWarning):
        obj.callable_once_per_instanceA()

    assert obj.callable_once_per_instanceB() == "callable_once_per_instanceB"
    with pytest.warns(expected_warning=CalledTooOftenWarning):
        obj.callable_once_per_instanceB()


def test_class_scope_unenforced() -> None:
    obj1 = SomeRestrictedClassUnenforced()
    obj2 = SomeRestrictedClassUnenforced()
    assert obj1.callable_once_per_class() == "callable_once_per_class"

    with pytest.warns(expected_warning=CalledTooOftenWarning):
        obj1.callable_once_per_class()
        obj2.callable_once_per_class()


def test_session_scope_unenforced() -> None:
    assert only_once_callable_function_unenforced() == "only_once_callable_function"
    with pytest.warns(expected_warning=CalledTooOftenWarning):
        only_once_callable_function_unenforced()


# ---------------------------------------------------------------
# enforce=True
# ---------------------------------------------------------------


class SomeRestrictedClass:
    @only_called_once(scope="object", enforce=True)
    def callable_once_per_instanceA(self) -> str:
        return "callable_once_per_instanceA"

    @only_called_once(scope="instance", enforce=True)
    def callable_once_per_instanceB(self) -> str:
        return "callable_once_per_instanceB"

    @only_called_once(scope="class", enforce=True)
    def callable_once_per_class(self) -> str:
        return "callable_once_per_class"


@only_called_once(scope="session", enforce=True)
def only_once_callable_function() -> str:
    return "only_once_callable_function"


def test_object_scope_enforced() -> None:
    obj = SomeRestrictedClass()
    assert obj.callable_once_per_instanceA() == "callable_once_per_instanceA"
    with pytest.raises(expected_exception=CalledTooOftenError):
        obj.callable_once_per_instanceA()

    assert obj.callable_once_per_instanceB() == "callable_once_per_instanceB"
    with pytest.raises(expected_exception=CalledTooOftenError):
        obj.callable_once_per_instanceB()


def test_class_scope_enforced() -> None:
    obj1 = SomeRestrictedClass()
    obj2 = SomeRestrictedClass()
    assert obj1.callable_once_per_class() == "callable_once_per_class"

    with pytest.raises(expected_exception=CalledTooOftenError):
        obj1.callable_once_per_class()
        obj2.callable_once_per_class()


def test_session_scope_enforced() -> None:
    assert only_once_callable_function() == "only_once_callable_function"
    with pytest.raises(expected_exception=CalledTooOftenError):
        only_once_callable_function()


# ---------------------------------------------------------------
# nonsense input
# ---------------------------------------------------------------


@only_called_once(scope="nonsense", enforce=True)
def only_once_callable_function_nonsense_scope() -> str:
    return "only_once_callable_function_nonsense_scope"


@only_called_once(scope="session", enforce="nonsense")  # type: ignore
def only_once_callable_function_nonsense_enforce() -> str:
    return "only_once_callable_function_nonsense_enforce"


def test_nonsense_input() -> None:
    with pytest.raises(expected_exception=ValueError):
        only_once_callable_function_nonsense_scope()
        only_once_callable_function_nonsense_enforce()
