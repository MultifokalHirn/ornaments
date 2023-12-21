# def retry_on_exception(exception: Exception, max_retries: int = 3) -> Callable[..., Callable[..., Any]]:
# TODO: Implement this decorator
#     """
#     Automatically retries a function if it raises a specified exception. The number of retries can be limited.

#     # Example usage:
#         class MyClass:
#             @retry_on_exception(scope="object")
#             def my_method(self):
#                 print("Called my_method")

#             @retry_on_exception(scope="class")
#             def my_class_method():
#                 print("Called my_class_method")

#         @retry_on_exception(scope="session")
#         def my_function():
#             print("Called my_function")

#     """

#     def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(wrapped=func)
#         def wrapper(*args, **kwargs) -> Any:
#             pass

#         return wrapper

#     return decorator
