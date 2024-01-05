class OrnamentsWarning(UserWarning):
    # TODO: think about whether this is a valuable distinction
    pass


class CalledTooOftenWarning(OrnamentsWarning):
    pass


class InvalidReturnTypeWarning(OrnamentsWarning):
    pass


class UncaughtExceptionWarning(OrnamentsWarning):
    """
    Warning raised when an exception is not caught by a decorator.
    """

    pass
