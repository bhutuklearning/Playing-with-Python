# Small anonymous functions defined with lambda.
add = lambda a,b: a+b
print(add(2,3))  # 5

# common with sorting
items = [("b",2), ("a",1)]
items.sort(key=lambda x: x[1])
print(items)  