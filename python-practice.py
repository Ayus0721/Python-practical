""" Excercise 1: Swap the number without using third variable"""
"""
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
"""
#Excercise 3: Write a program that will give you the sum of 3 digits 

# x=int(input("Enter three digit number:"))
# first=x%10    #we get the last digit of the number
# a=x//10   #we get first two digit number at quotient
# second=a%10   #here we get the second last digit
# third=a//10

# print("The sum of three digits are:",(first+second+third))

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