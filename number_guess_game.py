#in this game we generate a random number between 1 to 100 and ask user to guess 
#if user gusses right we congrate user and if not we tell right number

#importing random module
import random
#generate random number
random_number=random.randint(1,100)
#get user number
user_number=int(input("enter a number:"))
#compare both numbers and print result
if (random_number==user_number):
    print("congratulations you gussed right")
else:
    print("sorry wrong guess right number is:",random_number)
