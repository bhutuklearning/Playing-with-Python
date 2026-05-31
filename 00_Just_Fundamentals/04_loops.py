
# Only Practicing Loops

# For Loops
for i in range(3):  # 0,1,2
    print(i)

# iterate list
for fruit in ["apple", "banana"]:
    print(fruit)

list1 = [1, 2, 3]
for i in list1:
    print(i)

# while
n = 0
while n < 3:
    print(n)
    n += 1

# There are few keywords which helps to break the loop or skip the current iteration
# break and continue
for i in range(1, 5):
    if i == 3:
        break  # it will break the loop when i is 3
    print(i)