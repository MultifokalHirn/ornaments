class OrnamentsException(BaseException):
    # TODO: think about whether this is a valuable distinction
    pass


class CalledTooOftenError(OrnamentsException):
    pass


class InvalidReturnTypeError(OrnamentsException):
    pass


class IllegalCallError(OrnamentsException):
    pass
