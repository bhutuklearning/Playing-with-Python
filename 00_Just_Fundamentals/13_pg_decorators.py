
# This is the playground where I will learning about decorators and getting my hands dirty.

# Decorator is a  function that modifies another function without changing its original code.
# Decorators can be used in
# log function calls
# measure execution time
# check authentication
# retry API requests
# cache results

'''
In a nutshell, Instead of rewriting code inside every function,
you decorate the function once.
'''

# Functions are objects in Python which simply means"
# functions can be stored in variables
# passed to another function
# returned from another function

# Example of a function
def hello(name: str) -> str:
    return f"Hello, {name}!"

print(hello("Dada")) 

# Functions inside functions because python allows nested functions
def outer_function():
    # print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()

outer_function()

# Returning function
def outer_fn():
    def inner_fn():
        return "Hello from the inner function."

    return inner_fn

result = outer_fn()
print(result())


# Basic Decorator Example

def decorator_fn1(original_fn):

    def wrapper_function():
        print("Before the original function.")
        original_fn()
        print("After the original function.")

    
    return wrapper_function

@decorator_fn1
def display():
    print("This is the original function.")

# Calling the display function
display()



