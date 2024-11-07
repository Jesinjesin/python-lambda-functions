from functools import reduce
numbers_list = [1,2,3,4,5]
result = reduce(lambda no1, no2: no1+no2, numbers_list)

print(result)
