# In python, strings are immutable sequences of characters.
# Which means once string is created, it can't be changed.
# We can create a new string by concatenating or slicing the existing string.

s = "  Hello, Python!  "
print(s.lower())        # "  hello, python!  "
print(s.strip())        # "Hello, Python!"
print(s.replace("!", "?"))
print(s.split(","))     # ["  Hello", " Python!  "]
print("Py" in s)
print(f"Length: {len(s)}")