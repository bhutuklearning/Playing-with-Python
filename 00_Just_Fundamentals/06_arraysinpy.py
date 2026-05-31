# Arrays or lists in python


# In Python we use lists as dynamic arrays.
# (For numeric arrays use array module or numpy, but standard is list.)

nums = [1, 2, 3, 4]
nums.append(5)        # add
nums.pop()            # remove last
nums[0] = 10          # update
print(nums[1:3])      # slicing [2,3]
print(len(nums))


# Target: to perform some operations on Lists.
# Common: insert, remove, extend, list comprehensions: [x*x for x in nums]