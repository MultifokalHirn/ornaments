import pytest
from ornaments.decorators import only_called_once


class TestEnforcedOnlyCalledOnceDecorator:
    def test_object_scope(self) -> None:
        class MyClass:
            @only_called_once(scope="object", enforce=True)
            def my_method(self) -> str:
                return "my_method"

        obj = MyClass()
        assert obj.my_method() == "my_method"
        with pytest.raises(expected_exception=Exception):
            obj.my_method()

    def test_class_scope(self) -> None:
        class MyClass:
            @only_called_once(scope="class", enforce=True)
            def my_class_scope_method(self) -> str:
                return "my_class_scope_method"

        obj1 = MyClass()
        obj2 = MyClass()
        assert obj1.my_class_scope_method() == "my_class_scope_method"

        with pytest.raises(expected_exception=Exception):
            obj1.my_class_scope_method()
            obj2.my_class_scope_method()

    @only_called_once(scope="session", enforce=True)
    def my_session_function(self) -> str:
        return "my_session_function"

    def test_session_scope(self) -> None:
        assert self.my_session_function() == "my_session_function"
        with pytest.raises(expected_exception=Exception):
            self.my_session_function()
