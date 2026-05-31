# Functional helpers for iterables.

# map(func, iterable) → applies func to each element
# filter(func, iterable) → keeps elements where func is True
# reduce(func, iterable, [initial]) → reduces to single value (from functools)


from functools import reduce

nums = [1,2,3,4,5]

# map
squares = list(map(lambda x: x*x, nums))  # [1,4,9,16,25]
print(squares)

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2,4]
print(evens)

# reduce
total = reduce(lambda a,b: a+b, nums)  # 15
print(total)