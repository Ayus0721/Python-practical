#Q3. WAP to create a pyramid of the character ‘*’ and a reverse pyramid
r = int(input("Enter number of rows: "))

for i in range(r):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

#reverse one
a=int(input("Enter the number of Rows:"))
for i in range(a,0,-1):
    for j in range(i):
        print(' * ',end='')
    print('\n')
