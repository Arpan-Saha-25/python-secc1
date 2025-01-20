'''Write a program that takes a number as input from the user and prints its multiplication
table up to 10.'''

number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
