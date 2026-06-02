# Just learning and practicing generators in Python.


def generator_function():
    yield 1
    yield 2
    yield 3

x = generator_function()

print(x)

'''Output:
<generator object generator_function at 0x0000027B14734BF0>
Because generator does not execute immediately.'''

# For getting values, use next()
print(next(x))  # Output: 1
print(next(x))  # Output: 2
print(next(x))  # Output: 3

'''
Important Idea

Generator pauses after every yield.

It remembers:
variables
execution position
state

This is the magic.
'''

def test():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")

x = test()

print(next(x)) 
print(next(x)) 


# Infinite Generator
def infinite():

    i=1

    while True:
        yield i
        i += 1
    
x=infinite()
print(next(x))  # Output: 1
print(next(x))  # Output: 2 