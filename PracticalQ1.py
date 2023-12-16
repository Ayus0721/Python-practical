#Practical for my college first year


#Q1. WAP to find the roots of a quadratic equation


# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
print("Here's the example of Quadratic Equation:")
print("ax^2 + bx + c =0")

a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))
c = int(input("Enter the value for c:"))

# calculate the discriminant
d = (b**2) - (4*a*c)
if(d>0):
    print("Two distinct real roots")
elif("d==0"):
    print("Two equal real roots")
else:
    print("No real roots")

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
