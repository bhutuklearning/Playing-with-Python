# Function: It is a block of code which can be used multiple times.
# It can take some input and return some output.

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))