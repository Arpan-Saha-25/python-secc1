'''
Write a program that takes a temperature value and a scale (Celsius or Fahrenheit) as input
from the user. Convert the temperature to the other scale and print the result.
'''

choice = int(input("Select 1 for celsius or 2 for fahrenheit :\n"))
if choice == 1:
    print("Enter the temp [deg C] : ")
    cel = float(input())
    farh = (cel * 9/5) + 32
    print("Fahrenheit = " , farh)

elif choice == 2:
    print("Enter the temp [deg F] : ")
    farh = float(input())
    cel = (farh - 32)*5/9
    print("celsius = " , cel)

else:
    print("Wrong Input.")
    exit()

 