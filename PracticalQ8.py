# WAP to create a list of the cubes of only the even integers appearing in the input list 
# (may have elements of other types also) using the following:
# a. 'for' loop 
# b. list comprehension 

a=eval(input('Enter the numbers: '))
if (a%2==0): 
 for i in range(0,1000):
    print(a**3)
    break
else:
 print('It is not an even number')

# b. list comprehension
list1 = list(input("enter list item with a space").split())
print("your input list: ",list1)

list3 = [int(i) for i in list1 if i.isdigit()]
cube_list2 = [item ** 3 for item in list3 if isinstance(item, int) and item % 2 == 0]
print("Using list conprehension: ",cube_list2)

 
