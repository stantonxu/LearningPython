def GreaterThanZero(f):
    def wrapped(n):
        if not n > 0:
            errorMessage = "Value is not greater than 0"
            raise ValueError(errorMessage)
        return f(n)
    return wrapped

def IntegerValue(f):
    def wrapped(n):
        if not isinstance(n, int):
            errorMessage = "Value is not an integer"
            raise ValueError(errorMessage)
        return f(n)
    return wrapped

@GreaterThanZero
@IntegerValue
def factorial(n):
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

factorial(1)