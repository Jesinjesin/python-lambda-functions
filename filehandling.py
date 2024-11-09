# to create the file using python
'''f = open("libin.txt","w")
f.write("Friday\n")
f.write("Saturday\n")
f.write("Sunday\n")
f.close()
'''

# to open the particular using python
'''
f = open("libin.txt","r")

l = f.read()

print(l)

f.close()
'''
# it is open file in read mode
'''with open("libin.txt","r") as f:
    print(f.tell())
    print(f.read(11))
    print(f.tell()) 
'''
'''import os, sys
file_name = input("Enter File Name: ")
if os.path.isfile(file_name):
    print("File is present")
    with open(file_name, "r") as f:
        print(f.read())
'''
# it is used to craete csv file using csv module using python
'''
import csv
with open("student.csv","w") as f:
    pen = csv.writer(f)
    pen.writerow(["StudId", "Name", "Address"])
    stud_id = int(input("Enter no. "))
    name = input("Enter name ")
    address = input("Enter Address: ")
    pen.writerow([stud_id, name, address])
'''
# it is used to tell number of lines in particular file
'''
#No. of Lines in a given text file
f = open("libin.txt","r")
lines = f.readlines()
count = 0
for line in lines:
    print(line, end='')
    count+=1
print(count)
f.close()
'''
# it is used to tell number of letters in particular file
'''
#No. of letters in a given text file
f = open("libin.txt","r")
lines = f.readlines()
count = 0
for line in lines:
    print(line, end='')
    count+=1
print(count)
f.close()
'''
# it is used find the particular word present in the file
'''
#Occurrence of a particular word  in a given text file
f = open("libin.txt","r")
lines = f.readlines()
count = 0
for line in lines:
    print(line, len(line), end=' ')

f.close()
'''

