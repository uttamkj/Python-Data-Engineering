# Try-Except, file handling

#When Python hits an error it raises an exception and crashes. try-except catches that error so your program — and your pipeline — keeps running.

# Without try-except — crashes on bad data # int("abc") ← ValueError: invalid literal — CRASH # With try-except — handles it gracefully 
# ==============================
# Without try-except — crashes on bad data
# ==============================

# int("abc") ← ValueError: invalid literal — CRASH

print("----- Example 1 -----")

# Uncomment the line below to see the crash
# int("abc")

print()


# ==============================
# With try-except — handles it gracefully
# ==============================

print("----- Example 2 -----")

raw = "abc"

try:
    value = int(raw)
    print(f"Converted: {value}")
except ValueError:
    print(f"❌ Cannot convert '{raw}' to int")

# Output:
# ❌ Cannot convert 'abc' to int

print()


# ==============================
# Full structure — try / except / else / finally
# ==============================

print("----- Example 3 -----")

try:
    result = 100 / 0  # ZeroDivisionError

except ZeroDivisionError:
    print("❌ Cannot divide by zero")
    result = 0

else:
    print(f"✅ Result: {result}")  # only if no error

finally:
    print("Always runs — close DB, release resources here")

# Output:
# ❌ Cannot divide by zero
# Always runs — close DB, release resources here

print()


# ==============================
# Catch multiple exception types
# ==============================

print("----- Example 4 -----")


def safe_cast(value, cast_type):
    try:
        return cast_type(value)

    except (ValueError, TypeError):
        return None  # return None for bad data


print(safe_cast("75000", float))  # 75000.0
print(safe_cast("abc", float))    # None
print(safe_cast(None, float))     # None

# Output:
# 75000.0
# None
# None

print()


# ==============================
# Capture the error message
# ==============================

print("----- Example 5 -----")

try:
    x = int("bad")

except ValueError as e:
    print(f"Error: {e}")

# Output:
# Error: invalid literal for int() with base 10: 'bad'

print()


# ==============================
# Bonus Example: Successful conversion
# ==============================

print("----- Example 6 -----")

raw = "123"

try:
    value = int(raw)
    print(f"✅ Converted: {value}")

except ValueError:
    print(f"❌ Cannot convert '{raw}' to int")

# Output:
# ✅ Converted: 123

print()


# ==============================
# Bonus Example: else block execution
# ==============================

print("----- Example 7 -----")

try:
    result = 100 / 5

except ZeroDivisionError:
    print("❌ Cannot divide by zero")

else:
    print(f"✅ Result: {result}")

finally:
    print("Always runs")

# Output:
# ✅ Result: 20.0
# Always runs


'''
try:
    Code that may cause an exception

except:
    Handles the exception

else:
    Runs only if no exception occurs

finally:
    Runs always, whether exception occurs or not
    
try
 ├─ No Error ──► else ──► finally
 │
 └─ Error ─────► except ─► finally
'''
'''
🔶 Data Engineering link: Every pipeline has bad rows. Without try-except, one bad value crashes your entire job. With it, you catch the error per row, log it, and continue processing the rest. The finally block is where you close DB connections and file handles — critical for preventing resource leaks in long-running jobs.
'''


'''

Python has specific exception types for different errors. Catching the right one makes your error handling precise — not a blanket that hides real bugs.

Exception	When it happens	Common in pipelines?
ValueError	Wrong value type — int("abc")	⭐ Very common
TypeError	Wrong type used — "a" + 1	⭐ Very common
KeyError	Dict key doesn't exist — d["age"]	⭐ Very common
IndexError	List index out of range	Common
FileNotFoundError	File path doesn't exist	⭐ Very common
ZeroDivisionError	Dividing by zero	Common in aggregations
AttributeError	Method doesn't exist on object	Common
Exception	Catches ANY exception (catch-all)	Use sparingly
'''

# ==============================
# Handle specific exceptions — best practice
# ==============================

print("----- Example 1 -----")

record = {
    "id": "101",
    "salary": "bad_value"
}

try:
    emp_id = int(record["id"])          # KeyError or ValueError
    salary = float(record["salary"])    # ValueError — "bad_value"

except KeyError as e:
    print(f"Missing field: {e}")

except ValueError as e:
    print(f"Bad value: {e}")  # this fires

# Output:
# Bad value: could not convert string to float: 'bad_value'

print()


# ==============================
# Raise your own custom exceptions
# ==============================

print("----- Example 2 -----")


def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError(
            f"Age {age} is out of valid range 0-120"
        )

    return age


try:
    validate_age(-5)

except ValueError as e:
    print(f"Validation failed: {e}")

# Output:
# Validation failed: Age -5 is out of valid range 0-120

print()


# ==============================
# catch-all — use only as last resort
# ==============================

print("----- Example 3 -----")


def some_risky_operation():
    # Simulating an unexpected error
    return 10 / 0


try:
    result = some_risky_operation()

except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

# Output:
# Unexpected error: ZeroDivisionError: division by zero

print()


# ==============================
# Bonus: KeyError Example
# ==============================

print("----- Example 4 -----")

record = {
    "salary": "75000"
}

try:
    emp_id = int(record["id"])   # KeyError

except KeyError as e:
    print(f"Missing field: {e}")

except ValueError as e:
    print(f"Bad value: {e}")

# Output:
# Missing field: 'id'

print()


# ==============================
# Bonus: Successful Validation
# ==============================

print("----- Example 5 -----")

try:
    age = validate_age(25)
    print(f"Valid age: {age}")

except ValueError as e:
    print(f"Validation failed: {e}")

# Output:
# Valid age: 25
'''
try:
    # risky code

except SpecificException:
    pass

except AnotherSpecificException:
    pass

except Exception:
    # catch-all (keep last)
    pass '''