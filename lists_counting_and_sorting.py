### Length

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)


##############################################################################################


### selecting specific elements

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(len(employees))
print(employees[8])

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element)
print(element5)


##############################################################################################


### slicing lists

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]

print(beginning)

middle = suitcase[2:4]

print(middle)


suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]
print(end)

##############################################################################################


### counting

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

print(jake_votes)



##############################################################################################


### sorting 1 - change the list

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
sorted_addresses = addresses.sort()
print(addresses)
print(cities)


### sorting 2 - does not change the original list, but makes a new variable

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)

print(games_sorted)



##############################################################################################



### List exercises

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

###inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse? Save your answer to inventory_len###

inventory_len = len(inventory)
print(inventory_len)

###Select the first element in inventory. Save it to the variable first###

first = inventory[0]
print(first)

###Select the last item from inventory and save it to the variable last###

last = inventory[-1]
print(last)

###Select items from the inventory starting at index 2 and up to, but not including, index 6. Save your answer to inventory_2_6###

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

###Select the first 3 items of inventory and save it to the variable first_3###

first_3= inventory[:3]
print(first_3)

###How many 'twin bed's are in inventory? Save your answer to twin_beds###

twin_beds = inventory.count('twin bed')
print(twin_beds)

##Sort inventory using .sort()##
inventory.sort()