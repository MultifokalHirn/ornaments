from ornaments._types import AlteredDecoratable, Decoratable, Decorator


def dummy_decorator() -> Decorator:
    def decorator(func: Decoratable) -> Decoratable:
        return func

    return decorator


def return_none_decorator() -> Decorator:
    def decorator(func: Decoratable) -> AlteredDecoratable:
        if False:
            func()
        return lambda: None

    return decorator
