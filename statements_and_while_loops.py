import os

os.system('clear')
clear = lambda: os.system('clear')
clear()

'''
# Task 1 - Comitting numbers. Your task is to write a Python program using while loop to print out numbers from -5 to 5, without 0.
# You **can't** use `break` and `continue` statements! 

print('\nTask 1')
i = -5
while i in range(-5, 6):
    if i == 0:
        i += 1
    print(i, end=' ')
    i += 1



# Task 2 - Upper and lower letters. Your task is to write a Python program using **while** loop, that iterates over given string 
# and converts the lower letters to capital letters and vice versa. Print it out after changes.
# Hint: use string's methods and be careful of long texts and new lines!
# Note: You can use any text

print('\n\nTask 2')
i = 0
text = input('Enter a text: ')
text = list(text)
while i < len(text):
    if text[i].isupper():
        text[i] = text[i].lower()
    elif text[i].islower():
        text[i] = text[i].upper()
    i += 1
print(''.join(text))



# Task 3 - Average of numbers. Your task is to write a Python program using **while** loop, to calculate the average of n integer numbers 
# (input from the user). Input 0 (zero) finishes entering numbers and prints out calculations.  
# Hint: Average of **n** numbers is their sum divided by **n**,   
# for example average of numbers 5, 7 and 12 is (5 + 7 + 12)/3 = 24/3 = 8. 

print('\nTask 3')
i = 0
sum = 0
while i < 3:
    i += 1 
    number = int(input('Enter an integer: '))
    sum += number
print('Average of the above numbers is: ', sum / (i))

'''

# Task 4 - Find a character. Your task is to write a Python program using **while** loop, to find indexes of prompted character in the given text.  
# Note: Program should be case-sensitive, that means that uppercase and lowercase letters are treated as distinct!
# Hint: use string's methods and be careful of long texts and new lines!  
# Note: You can use any text, for example from lyrics. My was:  

print('\nTask 4')

text = '''She came to me one morning
        One lonely Sunday morning
        Her long hair flowing in the mid-winter wind
        I know not how she found me
        For in darkness I was walking
        And destruction lay around me from a fight I could not win'''
text = list(text)
char = input('What should be found?: ')
i = 0
while i < len(text):
    if text[i] == char:
        print(f'Character {char} found at index {i}')
    i += 1



# Task 5 - Find divisible numbers. Your task is to write a Python program using **while** loop, read (prompt) three numbers (a,b,c) 
# and check how many numbers between `a` and `b` are divisible by `c`. Input 0 (zero) as a third number (divisor) finishes program 
# and prints out the results.

print('\nTask 5')
a = int(input('Type starting integer: '))
b = int(input('Type ending integer: '))
c = int(input('Type divisor: '))
i = a
while i in range(a, b + 1):
    if c == 0:
        break
    if i % c == 0:
        print(i, ' is divisible by', c)
    i += 1




'''
- Your results should look like this:


```bash
Type starting integer: 1
Type ending integer: 100
Type divisor: 15


15  is divisible by 15
30  is divisible by 15
45  is divisible by 15
60  is divisible by 15
75  is divisible by 15
90  is divisible by 15


Type starting integer: 5
Type ending integer: 8
Type divisor: 0
``` 
'''