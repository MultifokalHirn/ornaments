from ornaments.decorators import only_called_once
import pytest


class TestOnlyCalledOnceDecorator:
    def test_object_scope(self):
        class MyClass:
            @only_called_once(scope="object")
            def my_method(self):
                return "Called my_method"

        obj = MyClass()
        assert obj.my_method() == "Called my_method"
        with pytest.raises(Exception):
            obj.my_method()

    def test_class_scope(self):
        class MyClass:
            @only_called_once(scope="class")
            def my_class_method():
                return "Called my_class_method"

        assert MyClass.my_class_method() == "Called my_class_method"
        with pytest.raises(Exception):
            MyClass.my_class_method()

    @only_called_once(scope="session")
    def my_function():
        return "Called my_function"

    def test_session_scope(self):
        assert my_function() == "Called my_function"
        with pytest.raises(Exception):
            my_function()
