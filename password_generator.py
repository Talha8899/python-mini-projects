# this programe generate a random password for user in the form of string
#importing string and random module
import string
import secrets
#taking password length as input from user
#length=int(input("input the length of password:"))
length=10
charecters=string.ascii_letters+string.digits
#randomly pick characters and digits to form a password and print it 
password="".join(secrets.choice(charecters)for i in range(length))
print(password)