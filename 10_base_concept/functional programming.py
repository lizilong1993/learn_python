from functools import reduce

my_list = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x*y, my_list) # take the function lambda as variable
print(result)