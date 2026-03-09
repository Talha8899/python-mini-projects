# This programe is covert the temperature from 
# celcius to farenheit and vice versa
# This program takes a numerical value and converts it based on user selection.

#get temperature from user 
Temp=int(input("enter the temperature reading  you want to convert:"))
#get chove fro user and convert into small alphabets
choice=input("convert it in celcius or farenheit:").lower()
#cheeking the choice and calculate
if (choice=="c" or choice=="celcius"):
    celcius=(Temp-32)*5/9
    print("the temperature is:",celcius,"celcius")
elif (choice=="f" or choice=="farenheit"):
    farenheit=(Temp*9/5)+32
    print("the temprature is :",farenheit,"farenheit")
else:
    print("error invalid choice")