# import functools  # pragma: no cover
# import time  # pragma: no cover


# def rate_limited(max_calls, period):  # pragma: no cover
#     def decorator(func):
#         calls = []

#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             now = time.perf_counter()
#             calls.append(now)

#             while calls and calls[0] < now - period:
#                 calls.pop(0)

#             if len(calls) > max_calls:
#                 raise RateLimitExceededError("Rate limit exceeded")
#             return func(*args, **kwargs)

#         return wrapper

#     return decorator


# class RateLimitExceededError(Exception):  # pragma: no cover
#     pass


# # @rate_limited(max_calls=3, period=5)
# # def api_request():
# #     print("API request executed")

# # for _ in range(5):
# #     try:
# #         api_request()
# #         time.sleep(1)
# #     except RateLimitExceededError:
# #         print("Rate limit exceeded, waiting...")
# #         time.sleep(2)
