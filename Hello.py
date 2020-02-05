print("Hello World\n")

# Creating  a list
List = []

# Creating a List with the use of string
List1 = ["Hello"]

# Creating a List with the use of multiple string
List2 = ["Good", "Morning"]

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List3 = [["Good", "Morning"], ["Hello"]]

# Print nested list
print(List3)

# Creating a List with
# the use of Numbers
# (Having duplicate values)
List4 = [1, 2, 4, 4, 3, 3, 3, 6, 5]

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List5 = [1, 2, 'Good', 4, 'Morning', 6, 'Hello']

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)

# Inserting element to list insert(index, value)
List.insert(2, 13)

print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Hello', 'World'])

# accessing a element using
# negative indexing
# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])

# Removing elements from List
# using Remove() method
List.remove(8)

# Creating a List
List7 = ['G', 'E', 'E', 'K', 'S', 'F',
         'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Intial List: ")
print(List7)

# Print elements of a range
# using Slice operation
Sliced_List = List7[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a
# pre-defined point to end
Sliced_List = List7[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List7[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

print(List7)

# Negative Index list slicing

# Creating a List
List8 = ['G', 'E', 'E', 'K', 'S', 'F',
        'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List8)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List8[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List8[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)



for item in list:
    print(item)