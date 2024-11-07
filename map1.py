from functools import reduce
numbersList = [1,2,3,4,5]
result = reduce(lambda no1, no2: no1+no2, numbersList,10)
print(result)
