def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
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
def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def ping():
    print("Pong!")

ping()  # Prints "Pong!" three times
import json

# Convert JSON String -> Python Dict (Deserialization)
json_string = '{"name": "Alice", "age": 30, "is_member": true}'
data = json.loads(json_string)
print(data["name"])  # Output: Alice

# Convert Python Dict -> JSON String (Serialization)
user_profile = {"name": "Bob", "age": 25, "skills": ["Python", "SQL"]}
new_json_string = json.dumps(user_profile, indent=4)
print(new_json_string)
import json

# Writing a dictionary to a JSON file
data_to_save = {"project": "AI Assistant", "version": 2.0}
with open("config.json", "w") as file:
    json.dump(data_to_save, file, indent=4)

# Reading data back from the JSON file
with open("config.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data["project"])  # Output: AI Assistant
