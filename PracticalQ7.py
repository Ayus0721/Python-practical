#Function that accepts two strings and returns the indices of all occurences of second stirng in the first string as a list

def find_occurrences(x, y):
    indices = []
    index = x.find(y)
    
    while index != -1:
        indices.append(index)
        index = x.find(y, index + 1)

    return indices

# Example usage:
main_str = input("Enter string:")
sub_str = input("Enter the second one:")
result = find_occurrences(main_str, sub_str)
print(result)
