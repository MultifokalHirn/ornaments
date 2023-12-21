# def checked_return_type(scope="object", enforce: bool = False) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Checks that the return value of the function is of a specified type. If not, it raises an exception or logs a warning.

#     # Example usage:
#         class MyClass:
#             @checked_return_type(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @checked_return_type(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @checked_return_type(scope="session")
#         def my_function():
#             print("Called my_function")

#     """
#     if scope not in ALL_SCOPES:
#         raise ValueError("Invalid scope. Must be 'object', 'class', or 'session'.")

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator
