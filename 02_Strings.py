a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

c = "I am learning Python, trying to show the ways to use string in Python"

# print(a)
# print(b)
# print(c)

# print(a[1].upper())

# for x in c:
#     print(x)

# print(len(c))

# print("Python" in c)

# if "Python" in c:
#     print("Yes, 'Python' is present.")
# if "Java" not in c:
#     print("No, 'Java' is NOT present.")

'''   Python - Slicing Strings '''


b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])

''' The strip() method removes any whitespace from the beginning or the end: '''

x = " Hello, World! "
print(x.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:

a = "Hello, World!"
# print(a.replace("H", "J"))


# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# rupees = 500
# text = f"I went to a shop and bought some fruits, vegetables and other cooking items for my family worth {rupees} rupees."
text = "I went to a shop and bought some fruits, vegetables and other cooking items for my family worth {rupees} rupees."
# print(text)
print(text.format(rupees=2000))