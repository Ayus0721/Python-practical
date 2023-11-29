                                                                                            # Basic Excercise for Beginners

# Excercise 1: Swap the number without using third variable

def swap(a,b):
    a=a+b   # here we are adding a and b 
    b=a-b   # now put value of a in this we get a+b-b we gives us b=a
    a=a-b   # now here put the value of both a and b we get in RHS (a+b)-(a-b) we results to a=b this is how swap can be done without using third variable
    print(a,b)

x=int(input("Enter the first number:\n"))
y=int(input("Enter the second number:\n"))
print(x,y)
swap(x,y)

#Excercise 2: Write a program to extract each digit from an integer in reverse order.

n=int(input("Enter the number:"))
x=str(n)
y=x[::-1]
k=" ".join(y)
print(k)

#Excercise 3: Write a program that will give you the sum of 3 digits 

x=int(input("Enter three digit number:"))
first=x%10    #we get the last digit of the number
a=x//10   #we get first two digit number at quotient
second=a%10   #here we get the second last digit
third=a//10

print("The sum of three digits are:",(first+second+third))

#Excercise 4: Write a program that will reverse a four digit number. Also it checks whether the reverse

x=int(input("Enter four digit number:"))
first=x%10    #we get the last digit of the number
a=x//10   #we get first three digit number at quotient
second=a%10   #here we get the third last digit
b=a//10   #we get frist two digit number at quotient
third=b%10  #we get the third digit 
fourth=b//10 # we get the first digit 

r=first*1000+second*100+third*10+fourth
print("The reverse is:\n",r)

#let's check 
if x==r:
    print(True)
else:
    print(False)

#Excercise 5: write a program to find the euclidean distance between two coordinates

import math
num_1=float(input("x1: "))
num_2=float(input("y1: "))
num_3=float(input("x2: "))
num_4=float(input("y2: "))

a=[num_1,num_2]
b=[num_3,num_4]

print("_"*100)
print("Eculedian distance(distance formula) for the given co-ordinate will be: ",round(math.dist(a,b),2))

#Excercise 6: Write a program that will tell whether the given number is divisible by 3 & 6

n=int(input("Enter the number: "))
if n%3==0 and n%6==0:
    print("The given the number is divisible by 3 and 6")
else:
    print("The given the number is not divisible by 3 and 6")

#Excercise 7: Write a program that will take three digits from the user and add the square of each digit

n=int(input("Enter the three digit number:"))
#462
a=n%10      #2
num=n//10   #46
b=num%10    #6
c=num//10   #4

sqr_1=(a**2)+(b**2)+(c**2)
print("Sum of square of each digit is: ",sqr_1)

#Excercise 8:Write the program that will check whether the number is armstrong number or not.

n=int(input("Enter the three digit number:"))
#462
a=n%10      #2
num=n//10   #46
b=num%10    #6
c=num//10   #4
s=(a**3)+(b**3)+(c**3)
if s==n:
    print("The given number is armstrong number")
else:
    print("The given number is not armstrong number")

#Excercise 9:Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

x=int(input("Enter four digit number:"))
first=x%10    #we get the last digit of the number
a=x//10   #we get first three digit number at quotient
second=a%10   #here we get the third last digit
b=a//10   #we get frist two digit number at quotient
third=b%10  #we get the third digit 
fourth=b//10 # we get the first digit 

r=(first**4)+(second**4)+(third**4)+(fourth**4)

if r==x:
    print("the number is narcissist number")
else:
    print("the number is not narcissist number")

                                                                                            # PYTHON INPUT AND OUTPUT EXCERCISE 

#Excercise 1: Accept number from a user

name=input("Enter your name: ")

#Excercise 2: Display three string "Name","is","James" as "Name**is**James"

print("Name","is","James",sep="**")

#Excercise 3:Convert decimal number to octal using print() output formatting
# the octal number of decimal number 8 is 10

n=int(input("Enter the decimal number: "))
print(oct(n)[-2:])

#Excercise 4: Display float number with 2 decimal places using print()
n=float(input("Enter the float number:"))
x=float(round(n,2))
print(x)

#Excercise 5: print all factors of a given number provided by the user.

num=int(input("Enter the number: "))

for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")

#Excercise 6: Accept a list of 5 float numbers as an input from the user

l=[]

while len(1)<5:
    n=float(input("Enter the number to add in a list:"))
    l.append(n)

print(l)
