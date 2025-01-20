'''
Given the following function, modify it to take two parameters (a and b) and return the sum
of their squares.
d e f square sum ( ) :
a = i n p u t ( ‘ Enter the f i r s t number : ’ )
b = i n p u t ( ‘ Enter the sec ond number : ’ )
#Write the e q u a ti o n h e r e
r e t u r n  r e s u l t

'''

def square_sum(a, b):
    result = a**2 + b**2
    return result

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

result = square_sum(first_number, second_number)
print(f'The sum of the squares is: {result}')



'''
Consider the following Python code. Identify and fix the errors to make it run correctly.
num = i n p u t ( ‘ ‘ Enter a number : ” )
r e s u l t = num ∗ 2
p r i n t ( ‘ The r e s u l t i s : ’ + r e s u l t )

'''
num = input('Enter a number: ')
result = float(num) * 2  
print('The result is: ' + str(result))


'''Given a list of numbers, modify the code to create a new list containing the squares of the numbers.
o ri gi n al n um b e r s = [ 2 , 4 , 6 , 8 , 1 0]
# Modify the code h e r e
p r i n t ( ‘ Squared numbers : ’ , squared numbers )
'''
original_numbers = [2, 4, 6, 8, 10]
squared_numbers = [num**2 for num in original_numbers]
print('Squared numbers:', squared_numbers)


'''
 Given a dictionary representing a book, modify the code to add a new key-value pair for the
publication year.
b o o k i n f o = { ’ t i t l e ’ : ’ The Great Gatsby ’ , ’ author ’ : ’F. S c o t t Fi t z g e r al d ’ }
# Add the p u b l i c a t i o n ye a r t o the d i c t i o n a r y
p r i n t ( ‘ Updated Book I n f o rm a ti o n : ’ , b o o k i n f o )
'''
book_info = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
book_info['publication_year'] = 1925
print('Updated Book Information:', book_info)


'''
Given the following class representing a Car, add a method ‘start engine’ that prints ‘Engine
started.’
c l a s s Car :
d e f i n i t ( s e l f , brand , model ) :
s e l f . brand = brand
s e l f . model = model
d e f d i s p l a y i n f o ( s e l f ) :
p r i n t ( f ”{ s e l f . brand} { s e l f . model }” )
# Add the s t a r t e n g i n e method h e r e
# Example u s a ge :
my car = Car ( ’ Toyota ’ , ’Camry ’ )
my car . d i s p l a y i n f o ( )
my car . s t a r t e n g i n e ( )
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"{self.brand} {self.model}")

    def start_engine(self):
        print("Engine started.")

my_car = Car('Toyota', 'Camry')
my_car.display_info()
my_car.start_engine()

'''
Given the following code for a simple temperature converter, modify it to handle both Celsius
to Fahrenheit and Fahrenheit to Celsius conversions based on user input.
c h oi c e = i n p u t ( ‘ Enter ’C’ f o r C e l s i u s t o F a h r e n h ei t o r ’F’ f o r F a h r e n h ei t t o C e l s i u s : ’ )
i f c h oi c e == ’C’ :
c e l s i u s = f l o a t ( i n p u t ( ‘ Enter tempe r a tu re i n C e l s i u s : ’ ) )
f a h r e n h e i t = # Enter the e q u a ti o n
p r i n t ( f ‘ The tempe r a tu re i n F a h r e n h ei t i s : { f a h r e n h e i t } ’ )
e l i f c h oi c e == ’F ’ :
# Do same f o r f a h r e n h e i t t o c e l s i u s c o n v e r si o n
e l s e :
p r i n t ( ‘ I n v a l i d c h oi c e . Pl e a s e e n t e r ’C’ o r ’F ’ . ’ )

'''
choice = input('Enter \'C\' for Celsius to Fahrenheit or \'F\' for Fahrenheit to Celsius: ')

if choice == 'C':
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'The temperature in Fahrenheit is: {fahrenheit}')
elif choice == 'F':
    fahrenheit = float(input('Enter temperature in Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'The temperature in Celsius is: {celsius}')
else:
    print('Invalid choice. Please enter \'C\' or \'F\'.')


'''
wing code is supposed to take a string as input and print the reversed string. However, it has some mistakes. Fix the code.
t e x t = i n p u t ( ” Enter a s t r i n g : ” )
r e v e r s e d t e x t = t e x t [ : : −1 ]
p r i n t ( ” The r e v e r s e d s t r i n g i s : ” r e v e r s e d t e x t )

'''
text = input("Enter a string: ")
reversed_text = text[::-1]
print("The reversed string is:", reversed_text)


'''
Write a program that calculates ticket prices based on age. Ask them to modify the code to
include a discount of 10% for students (ages 13-18) and seniors (ages 61 and above).
age = i n t ( i n p u t ( ‘ Enter your age : ’ ) )
i f 0 <= age <= 5 :
t i c k e t p r i c e = 0 # Free f o r a g e s 0−5
e l i f 6 <= age <= 1 2:
t i c k e t p r i c e = 5
e l i f 13 <= age <= 1 8:
t i c k e t p r i c e = 10 # Modify t h i s t o i n cl u d e a 10% di s c o u n t
e l i f 19 <= age <= 6 0:
t i c k e t p r i c e = 15
e l s e :
t i c k e t p r i c e = 10 # Di sc oun t f o r s e n i o r s ( 6 1 and above )
p r i n t ( f ‘ The t i c k e t p r i c e f o r a { age}−year−ol d i s : ${ t i c k e t p r i c e } ’ )
'''
age = int(input('Enter your age: '))

if 0 <= age <= 5:
    ticket_price = 0  
elif 6 <= age <= 12:
    ticket_price = 5
elif 13 <= age <= 18:
    ticket_price = 10 - (0.10 * 10)  
elif 19 <= age <= 60:
    ticket_price = 15
else:
    ticket_price = 10 - (0.10 * 10)  

print(f'The ticket price for a {age}-year-old is: ${ticket_price:.2f}')


