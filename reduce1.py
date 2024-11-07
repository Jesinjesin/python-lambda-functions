#Maximum number of a given list:
from functools import reduce 
numbers_list = [10,20,5,7,8,12]
max = reduce(lambda no1, no2: no1 if no1>no2 else no2, numbers_list)
print(max)
