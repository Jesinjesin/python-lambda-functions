l1 = [10,15,20,25,30]
l2 = [5,10,15,20,30,40,50]

result = list(filter(lambda no:no[0] %10==0 and no[1]%10==0, 
            zip(l1,l2)))
print(result)
