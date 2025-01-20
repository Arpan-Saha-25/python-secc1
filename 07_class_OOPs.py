'''
write a program that simulates an ATM withdrawal. Ask them to modify the code to include
a maximum withdrawal limit of 2000 rupees per transaction.
a c c o u n t b al a n c e = 10000 # Assuming i n i t i a l acc oun t b al a n c e i s 10000 r u p e e s
withdrawal amount = i n t ( i n p u t ( ‘ Enter the amount you want t o withdraw : ’ ) )
# Modify the code t o i n cl u d e a maximum wi thd r aw al l i m i t
max withdrawal = 2000
i f withdrawal amount % 100 == 0 :
a c c o u n t b al a n c e −= withdrawal amount
p r i n t ( f ‘ Withdrawal s u c c e s s f u l . Remaining b al a n c e : ${ a c c o u n t b al a n c e } ’ )
e l s e :
p r i n t ( ‘ Withdrawal amount must be d i v i s i b l e by 1 0 0 . ’ )
'''

account_balance = 10000  # Assuming initial account balance is 10000 rupees
withdrawal_amount = int(input('Enter the amount you want to withdraw: '))

max_withdrawal = 2000

if withdrawal_amount % 100 == 0:
    if withdrawal_amount <= max_withdrawal:
        account_balance -= withdrawal_amount
        print(f'Withdrawal successful. Remaining balance: {account_balance} rupees')
    else:
        print(f'Maximum withdrawal limit exceeded. Please enter an amount up to {max_withdrawal} rupees.')
else:
    print('Withdrawal amount must be divisible by 100.')


'''
Write a program that determines if a given character is a vowel or a consonant. Ask them to
modify the code to handle both uppercase and lowercase letters.
ch a r = i n p u t ( ” Enter a s i n g l e c h a r a c t e r : ” )
# Modify the code t o h andle both u p p e r c a s e and l o w e r c a s e l e t t e r s
i f ch a r . l owe r ( ) i n ’ aei ou ’ :
p r i n t ( ‘ Vowel ’ )
e l s e :
p r i n t ( ‘ Consonant ’ )
'''
char = input("Enter a single character: ")

if char.lower() in 'aeiou':
    print('Vowel')
else:
    print('Consonant')

'''
Write a program that prints a pattern using nested loops to create a triangle of numbers.
Ask them to modify the code to print a square pattern.
rows = i n t ( i n p u t ( ” Enter the number o f rows f o r the p a t t e r n : ” ) )
# Modify the code t o p ri n t a d i f f e r e n t p a t t e r n
f o r i i n r an ge ( 1 , rows + 1 ) :
f o r j i n r an ge ( 1 , i + 1 ) :
p r i n t ( j , end=” ” )
p r i n t ( )
'''
rows = int(input("Enter the number of rows for the pattern: "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(j, end=" ")
    print()
