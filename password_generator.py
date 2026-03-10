# this programe generate a random password for user in the form of string
#importing string and random module
import string
import random
#taking password length as input from user
length=int(input("input the length of password:"))
charecters=string.ascii_letters+string.digits
#randoly pick characters and digits to form a password and print it 
password="".join(random.choices(charecters,k=length))
print(password)