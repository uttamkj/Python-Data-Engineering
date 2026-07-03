from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Modify the behavior or arguments before execution
        result = func(*args, **kwargs)
        # Modify the output after execution
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"hello, {name}"

print(greet("alice"))  # Output: HELLO, ALICE
