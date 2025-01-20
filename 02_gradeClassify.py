'''Develop a program that prompts the user to enter a numerical grade. Classify the grade into
categories (A, B, C, D, F) and print the corresponding classification'''

grade = float(input("Enter the numerical grade: "))

if 90 <= grade <= 100:
    classification = "A"
elif 80 <= grade < 90:
    classification = "B"
elif 70 <= grade < 80:
    classification = "C"
elif 60 <= grade < 70:
    classification = "D"
elif 0 <= grade < 60:
    classification = "F"
else:
    print("Invalid grade. Please enter a grade between 0 and 100.")
    exit()

print(f"Your grade is: {classification}")


