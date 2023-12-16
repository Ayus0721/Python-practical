#Program to count frequency of character in a string
def cont(x,y):
    
    print(x.count(y))

a=input('Enter the text in which you want to count: ')
b=input('Enter the letter that you want to count: ')
cont(a,b)
# #Program to replace a character with another string
x=input("Enter the letter:")
a=input("the letter you want to replace\n")
b=input("the letter you want to replace with\n")
print(x.replace(a,b))

#Program to remove first occurence of a character from a string
a= input("Enter your text: ")
char = input("Enter the character that you want to delete: ")
result = ' '
for i in range(len(a)):
    if(a[i] == char):
        result= a[0:i] + a[i + 1:len(a)]
        break
print("Entered text        : ",a)
print("Text after removing : ",result)

#Program to remove all occurences of a string
def removal_of_all_occurence(a,b):
    print(a.replace(b, ' '))

x=input('Enter the text: ')
y=input('Enter the character that you want to remove: ')
removal_of_all_occurence(x,y)