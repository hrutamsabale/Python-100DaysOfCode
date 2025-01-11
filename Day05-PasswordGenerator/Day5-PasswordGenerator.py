import string 
import random
letters=list(string.ascii_uppercase)+list(string.ascii_lowercase)
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','?','/',';','~']
nol=int(input("How many letters do you want? "))
non=int(input("How many numbers do you want? "))
nos=int(input("How many symbols do you want? "))
list1=[]
for i in range(1,nol+1):
    random1=random.randint(0,51)
    list1.append(letters[random1])    
for i in range(1,non+1):
    random1=random.randint(0,9)
    list1.append(numbers[random1])
for i in range(1,nos+1):
    random1=random.randint(0,9)
    list1.append(symbols[random1])
password=""
for i in range(1,len(list1)+1):
    random1=random.randint(0,len(list1)-1)
    password+=list1[random1]
    del list1[random1]

print(f"\nYour password can be: {password}")

