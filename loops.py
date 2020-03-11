# simple for loop

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)


############################################################

# using range and variables in a for loop

promise = "I will not chew gum in class"

for i in range(5):
  print(promise)


############################################################

# appending each item for one list to another with a for loop


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for i in students_period_A:
  students_period_B.append(i)
  print(i)

print(students_period_B)


############################################################

# breaks in loops

# ends the loop when criteria is met

# 1.
# You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption. Using a for loop, iterate through the dog_breeds_available_for_adoption list and print out each dog breed.

# 2.
# Inside your for loop, after you print each dog breed, check if it is equal to dog_breed_I_want. If so, print "They have the dog I want!"

# 3.
# Add a break statement when your loop has found dog_breed_I_want, so that the rest of the list does not need to be checked.


dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break


############################################################

# continue

# allows you to skip a value based on specified criteria

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)


###########################################################

# while loops and .pop()

# You are adding students to a Poetry class, the size of which is capped at 6. While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list and add it to the students_in_poetry list.

# Print the students_in_poetry list.

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop(-1))

print(students_in_poetry)


###########################################################

# Nested Loops

# 1.
# We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert’s Scoop Shop. We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

# 2.
# Go through the sales_data list. Call each inner list location, and print out each location list.

# 3.
# Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.

# By the end, you should have the sum of every number in the sales_data nested list.

# 4.
# Print out the value of scoops_sold.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  
for location in sales_data:
  for element in location:
    scoops_sold = scoops_sold + element
    
print(scoops_sold)


###########################################################

# List Comprehension

# We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters. Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.

# Print can_ride_coaster.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

###########################################################

# List comprehension 2

# We have provided a list of temperatures in celsius. Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.

# *Note: * To convert, use the formula:

# temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [c_to_f(temp_in_celsius) for temp_in_celsius in celsius]
##or##
# fahrenheit = [temp_in_celsius * (9/5) + 32 for temp_in_celsius in celsius]

print(fahrenheit)    


##########################################################

# Exercise

# 1.
# Create a list called single_digits that consists of the numbers 0-9 (inclusive).

# 2.
# Create a for loop that goes through single_digits and prints out each one.

# 3.
# Create a list called squares. Assign it to be an empty list to begin with.

# 4.
# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

# 5.
# After the for loop, print out squares.

# 6.
# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

# 7.
# Print cubes.

single_digits = range(0,10)

squares = []

for element in single_digits:
  print(element)
  squares.append(element * element)
  
print(squares)

cubes = [element ** 3 for element in single_digits]

print(cubes)

##########################################################

## Loops Exercise ##

# 1.
# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

# First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

# 2.
# Iterate through the prices list and add each price to the variable total_price.

# 3.
# After your loop, create a variable called average_price that is the total_price divided by the number of prices.

# You can get the number of prices by using the len() function.

# 4.
# Print the value of average_price so the output looks like:

# Average Haircut Price: <average_price>
# 5.
# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

# 6.
# Print new_prices.

# Revenue:
# 7.
# Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

# Create a variable called total_revenue and set it to 0.

# 8.
# Use a for loop to create a variable i that goes from 0 to len(hairstyles)

# Hint: You can use range() to do this!

# 9.
# Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.

# 10.
# After your loop, print the value of total_revenue, so the output looks like:

# Total Revenue: <total_revenue>
# 11.
# Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.

# 12.
# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

# You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.

# 13.
# Print cuts_under_30.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
new_prices = [price - 5 for price in prices]

## calculating the average ##
#########################################################
for price in prices:
  total_price = total_price + price

average_price = total_price / len(prices)

print('Average Haircut Price: ' + str(average_price))
#########################################################

## Revenue ##
#########################################################
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = total_revenue + (prices[i] * last_week[i])

print('Total Revenue: ' + str(total_revenue))

average_daily_revenue = total_revenue / 7

print('Average Daily Revenue ' + str(average_daily_revenue))
#########################################################

## Advertising ##
#########################################################
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
concat_cuts_under_30 = ''

for hairstyle in cuts_under_30:
  if hairstyle == cuts_under_30[0]:
    concat_cuts_under_30 = concat_cuts_under_30 + hairstyle
  else:  
    concat_cuts_under_30 = concat_cuts_under_30 + ' / ' + hairstyle
 
print('We Have The Following Cuts For Under $30: ' + concat_cuts_under_30)
#########################################################


  

  
  
