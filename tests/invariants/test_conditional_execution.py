# from typing import overload

# import pytest
# from ornaments._exceptions import IllegalCallError
# from ornaments.invariants import not_called_if


# @overload
# def my_condition() -> None:
#     ...


# @overload
# def my_condition() -> bool:
#     ...

# def my_condition() -> bool:
#     return True

# unconditional = lambda: True

# def test_uncaught_exception_warning() -> None:


#     class MyClass:
#         some_value: bool

#         def __init__(self, some_value: bool = False):
#             self.some_value = some_value

#         def my_conditional(self) -> bool:
#             return self.some_value

#         @not_called_if(condition_func=lambda : self.my_conditional)
#         def maybe_do_something(self) -> None:
#             print("Did something!")

#     @not_called_if(condition_func=)
#     def my_method() -> None:
#         raise IllegalCallError("This should not have been called")

#     @overload


#     with pytest.raises(expected_exception=IllegalCallError):
#         my_method()

#     @overload
#     def my_condition() -> bool:
#         return False

#     my_method()
