# Double
# Create a new list named double_nums by multiplying each number in nums by two.

nums = [4, 8, 15, 16, 23, 42]
double_nums = [num * 2 for num in nums]
print(double_nums)

#########################################################################################


# Squares
# You’ve been given a list of the numbers between 0 and 10. We created this list using the range function! Create a new list named squares that contains the square of every number in this list.

nums = range(11)

squares = [num ** 2 for num in nums]

print(nums)


#########################################################################################

# add_ten 
# Create a new list named add_ten that adds ten to every element in the list nums.

nums = [4, 8, 15, 16, 23, 42]

add_ten  = [num + 10 for num in nums]

print(add_ten)


#########################################################################################

# Divide By Two
# Create a new list named divide_by_two that contains half of every element in the list nums. Make sure to divide by 2, not 2.0!


nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num / 2 for num in nums]
print(nums)


#########################################################################################


# Parity
# Create a new list named parity that contains a 1 or a 0 for each element of nums. For each element, if that element was even, the new list should contain a 0. If the element was odd, the new list should contain a 1.

nums = [4, 8, 15, 16, 23, 42]
parity = [1 if num % 2 else 0 for num in nums]
print(parity)
    


#########################################################################################

# Add Hello

# Create a new list named greetings that adds "Hello, " in front of each name in the list names.

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]
print(greetings)


#########################################################################################

# First Character

# Create a new list named first_character that contains the first character from every name in the list names

names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
print(first_character)


#########################################################################################

# Size (Lengths)

# Create a new list named lengths that contains the size of each name in the list of names

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
print(lengths)


#########################################################################################

# Opposite (not)

# Create a new list named opposite that contains the opposite boolean for each element in the list booleans.

booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]
print(opposite)


#########################################################################################

# Same String (== operator)

# Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at position i equals "Jerry". The entry should be False otherwise

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]
print(is_Jerry)


#########################################################################################

# Greater Than Two
# Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.

nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]
print(greater_than_two)


#########################################################################################
 
# Product (multiplying elements in a nested list)

# Create a new list named product that contains the product of each sub-list of nested_lists.

nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [item1 * item2 for (item1, item2) in nested_lists]
print(product)


#########################################################################################

# Greater Than

# Create a new list named greater_than that contains True if the first number in the sub-list is greater than the second number in the sub-list, and False otherwise.

nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [True if item1 > item2  else False for (item1, item2) in nested_lists]
print(greater_than)


#########################################################################################

# First Only
# Create a new list named first_only that contains the first element in each sub-list of nested_lists.

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item1 for (item1, item2) in nested_lists]
print(first_only)


#########################################################################################

# sum (zip & list comprehension
# Add With Zip
# Use list comprehension and the zip function to create a new list named sums that sums corresponding items in lists a and b. For example, the first item in the new list should be 5 from adding 1 and 4 together.

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
c = zip(a,b)
sums = [item1 + item2 for (item1, item2) in c]
print(c)
print(sums)



#########################################################################################

# Divide With Zip

# Use list comprehension and the zip function to create a new list named quotients that divides the elements in list b by those in list a . For example, the second item in the new list should be 2.5 from dividing 5.0 by 2.0.

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [item2 / item1 for (item1, item2) in zip(a,b)]
print(quotients)


#########################################################################################

# Captials
# You’ve been given two lists: a list of capitals and a list of countries. Create a new list named locations that contains the string "capital, country" for each item in the original lists. For example, if the 5th item in the capitals list is "Lima" and the 5th item in the countries list is "Peru", then the 5th item in the new list should be "Lima, Peru"

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital + ", " + country for (capital, country) in zip(capitals,countries)]
print(locations)


#########################################################################################




#########################################################################################




#########################################################################################




#########################################################################################




#########################################################################################







