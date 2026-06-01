
# Implementing decorators to understand properly.
# Execution Time Decorator
import time

def calculating_execution_time(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time  
        print(f"Execution time: {execution_time:.6f} seconds")

    return wrapper

@calculating_execution_time
def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    print(f"Total: {total}")

sample_function()

''''
Problem: What About Arguments?
Current wrapper only works for functions without parameters.

Bad:
@decorator
def add(a, b):
    return a + b

This will fail unless wrapper accepts arguments.

Solution: *args and **kwargs
'''

# Universal Decorator with Arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the original function.")
        result = func(*args, **kwargs)
        print("After the original function.")
        return result

    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(1, 3))

'''
#### Summary of Decorators
a) take a function
b) add extra behavior
c) return modified function
'''