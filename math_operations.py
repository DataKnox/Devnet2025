def divide(a: float, b: float) -> float:

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b 