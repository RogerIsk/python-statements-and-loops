import os

os.system('clear')
clear = lambda: os.system('clear')
clear()

# Python Statements and Loops

'''## The for loop
In this exercise, we will focus on the usage of the **for** loop, including:
 - `input()` from the user,
 - `range()` function, 
 - `in` keyword. 
'''

#Task 1 - Multiplication table. write a Python program to create the multiplication table (from 1 to 10) of a number.
# Number is prompted by the user. Print results.

print('\nTask 1')
user_input = int(input("Enter a number: "))
for i in range(1, 11):
    print(user_input, 'x', i, '=', user_input*i)



# Task 2 - Pattern with loop. Your task is to write a Python program to construct the following pattern, using a **for** loop.
# Note: Don't type numbers manually. Use the loop!

print('\nTask 2')
for i in range(1, 10):
    print(str(i)*i)



# Task 3 - Reverse word. Your task is to write a Python program that accepts a word from the user and reverses it, using a **for** loop.  
# Hint: the `range()` function accepts negative numbers!

print('\nTask 3')
user_input = input("Input a word to reverse: ")
reversed_word = ''
for i in range(len(user_input)-1, -1, -1): # range(start, stop, step) - start from the last letter, stop at the first letter, step -1 means go backwards
    reversed_word += user_input[i]         # add the letter to the reversed_word
print('Reversed word:', reversed_word)



# Task 4 - Upper letters. Your task is to write a Python program using **for** loop, that iterates over given string 
#and changes every occurence of 'o' letter into big letter 'O'.  
# Hint: use one of the string's method!  
# Note: You can use any text, for example from lyrics. My was "Hello, I love you, won't you tell me your name?" :smiley:

print('\nTask 4')
user_input = input("Input a sentence with lots of o's: ")
new_string = ''
for i in user_input:      # iterate over the user_input / check all the letters in the string
    if i == 'o':          # if the letter is 'o'
        new_string += 'O' # add a capital 'O' to the new_string
    else:                 # if the letter is not 'o'
        new_string += i   # add the letter to the new_string
print(new_string)


 
# Task 5 - Count digits and letters. Your task is to write a Python program using **for** loop, that counts digits and letters.  
# User should be prompted to enter her/his characters with the keyboard, even without looking at it.  
# Store the information about number of digits and letters in some variables.
# Hint: use one of the string's method and try to type only letters and digits!  

for i in range(1):
    print('\nTask 5')
    user_input = input("Input your characters: ")
    digits = 0
    letters = 0
    for i in user_input:  # iterate over the user_input / check all the letters in the string
        if i.isdigit():   # if the letter is a digit
            digits += 1   # add 1 to the digits counter
        elif i.isalpha(): # if the letter is a letter
            letters += 1  # add 1 to the letters counter
    print('Number of digits: ', digits)
    print('Number of letters: ', letters)






'''
- Your results could look like this:


```
Input your characters: dgbudf8gsdf7g8sd7fg7dsf7g7y7df7ygsdfg775uybgfbfdug8fdsugdfsguf7g7df7g7ydf7yg7rye7gy7eryg
Number of digits:  21
Number of letters:  67 
``` 
'''