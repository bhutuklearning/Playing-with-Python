# Functions that yield values lazily (one at a time) instead of returning a full list — memory efficient.

def squares_up_to(max_n):
    for i in range(max_n):
        yield i*i

for sq in squares_up_to(5):
    print(sq)  # 0,1,4,9,16


# Function of yield keyword

# Also generator expressions: (x*x for x in range(5))