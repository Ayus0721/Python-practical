""" Q2. WAP to accept a number n and 
a. Check if n is prime 
b. Generate all prime numbers till n
c. Generate first n prime numbers
This program may be done using functions """

#Ans of a.


a=int(input("Enter your Number:"))
f=0
if (a>1):
    for i in range(2,int(a/2)+1):
        if(a%i==0):
            f=1
            break
    if(f==1):
        print("Given number is not a prime number")
    else:
        print("Given number is prime number")
else:
    print("Given number is not prime number")

#Answer of b

r=int(input("Enter the number :"))
for i in range(1,r+1):
    if i > 1:  
        for s in range (2, i):  
            if (i % s) == 0:  
                break  
        else:  
            print (i)  


#Answer of c

def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter the number:"))  
i=2 
lst=[] 
while(1):  
    if(Prime(i)):  
        lst.append(i) 
        if(len(lst)==N): 
            break 
    i+=1 
print("First "+str(N)+" Prime numbers are:",end="") 
print(*lst) 
