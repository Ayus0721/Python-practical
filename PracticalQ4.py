"""Q4. WAP that accepts a character and performs the following: 
a. print whether the character is a letter or numeric digit or a special character 
b. if the character is a letter, print whether the letter is uppercase or lowercase 
c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output 
is NINE)"""

#Ans of A

def checkLtr(n):
    
 
    if n.isalpha():
        print("Given character is letter\n",n)
    elif n.isdigit():
        print("the given character is numeric digit\n",n)
    else:
        print("The given charater is special character\n",n)

#Ans of B
def check_case(p):
    if p.isupper():
        print("The given character is uppercase\n",p)
    elif p.islower():
        print("Then given character is lower case\n",p)
    else:
        print("Given character is niether uppercase nor lowercase\n")

#Ans of C
def check_digit_name(digit):
    # Dictionary mapping numeric digits to their names
    digit_names = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }

    if digit.isdigit() and len(digit) == 1:
        print(digit_names[digit])
    else:
        print("Invalid input. Please enter a single numeric digit.")



a=input("Please give a Character:\n")
checkLtr(a)
check_case(a)

b=input("Please give a Digit:\n")
check_digit_name(b)
