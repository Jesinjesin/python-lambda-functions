no = int(input("enter the number:"))
count= 0
for i in range(2,no):
    if(no%i==0):
        count=count+1
        print(no,"is not a prime")
        break
else:
    	print(no,"is a prime")
