'''
Modify the code to create a new list containing only the words longer than 3 characters.
words = [ ’ apple ’ , ’ banana ’ , ’ kiwi ’ , ’ orange ’ , ’ grape ’ ]
# Modify the code h e r e
p r i n t ( ” Long words : ” , l o n g w o r d s )
'''

words = ['apple', 'banana', 'kiwi', 'orange', 'grape']

long_words = [word for word in words if len(word) > 3]

print("Long words:", long_words)


'''
Create a program that prompts the user to enter a number and then calculates and prints its
factorial using a while loop.
'''

number = int(input("Enter a number: "))

factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print(f"The factorial is: {factorial}")

'''
Write a function called is ‘leap’ year that takes a year as an argument and returns True if it’s
a leap year and False otherwise.
'''

def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year_to_check = int(input("Enter a year: "))

result = leap(year_to_check)
print(f"{year_to_check} is a leap year: {result}")


'''
Write a function that generates the Fibonacci series up to a specified number of terms.
'''

def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    return fibonacci_series

num_of_terms = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_result = generate_fibonacci(num_of_terms)
print(f"Fibonacci series up to {num_of_terms} terms: {fibonacci_result}")


'''
Create a function that takes a list of numbers as input and returns the sum of all the elements
'''

def calculate_sum(numbers):
    
    return sum(numbers)

input_numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
result_sum = calculate_sum(input_numbers)
print(f"The sum of the numbers is: {result_sum}")


'''
Given the following class representing a Circle, add a method calculate ‘circumference’ that
returns the circumference of the circle.
c l a s s C i r c l e :
d e f i n i t ( s e l f , r a di u s ) :
s e l f . r a di u s = r a di u s
d e f c a l c u l a t e a r e a ( s e l f ) :
r e t u r n 3. 1 4 ∗ s e l f . r a di u s ∗ s e l f . r a di u s
# Add the c a l c u l a t e c i r c u m f e r e n c e method h e r e
c i r c l e = C i r c l e ( 5 )
p r i n t ( ‘ Area : ’ , c i r c l e . c a l c u l a t e a r e a ( ) )
p r i n t ( ‘ Ci r cum fe r enc e : ’ , c i r c l e . c a l c u l a t e c i r c u m f e r e n c e ( ) )
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print('Area:', circle.calculate_area())
print('Circumference:', circle.calculate_circumference())

'''The following code contains an error related to division by zero. Modify the code to handle
this error gracefully.
numerator = i n t ( i n p u t ( ‘ Enter the numerator : ’ ) )
denominator = i n t ( i n p u t ( ‘ Enter the denominator : ’ ) )
r e s u l t = numerator / denominator
p r i n t ( ‘ The r e s u l t o f the d i v i s i o n i s : ’ , r e s u l t )
'''
numerator = int(input('Enter the numerator: '))
denominator = int(input('Enter the denominator: '))

if denominator != 0:
    result = numerator / denominator
    print('The result of the division is:', result)
else:
    print('Error: Division by zero is not allowed.')

