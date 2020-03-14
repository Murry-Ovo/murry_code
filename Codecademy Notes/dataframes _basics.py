# Create a dataframe manually

# You run an online clothing store called Panda’s Wardrobe. You need a DataFrame containing information about your products.

# Create a DataFrame with the following data that your inventory manager sent you:

# Product ID	Product Name	Color
# 1	t-shirt	blue
# 2	t-shirt	green
# 3	skirt	red
# 4	skirt	black

# We have already filled in the information for Product ID in df1.

# Add the code to create the columns Product Name and Color and their associated data.

import codecademylib
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black'] 
})

print(df1)


###################################################################

# Create a Dataframe 2 using lists of lists

# You’re running a chain of pita shops called Pita Power. You want to create a DataFrame with information on your different store locations.

# Use a list of lists to create a DataFrame with the following data:

# Store ID	Location	Number of Employees
# 1	San Diego	100
# 2	Los Angeles	120
# 3	San Francisco	90
# 4	Sacramento	115

# We have filled in the information for the first two rows in df2.

# Add the code to create the 3rd and 4th rows, and the column names.

import codecademylib
import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
  # Fill in rows 3 and 4
],
  columns=[
    #add column names here
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)


###################################################################

# Loading and Saving CSVs

# You’re working for the County of Whoville and you just received a CSV of data about the different cities in your county. Read the CSV 'sample.csv' into a variable called df, so that you can learn more about the cities.

# df = pd.read_csv('sample.csv')

# Let’s inspect the CSV.

# Type print(df) on the next line and then run your code. What sort of data were you sent?


import codecademylib
import pandas as pd

df = pd.read_csv('sample.csv')

print(df)

###################################################################


# Inspect a DataFrame

# 1.
# You’re working for a Hollywood studio, trying to use data to predict the next big hit. Load the CSV imdb.csv into a variable called df, so that you can learn about popular movies from the past 90 years.

# 2.
# Let’s learn about these movies.

# Paste the following code into script.py:

# print(df.head())
# What happens when you press “Run”?

# 3.
# What exactly is in this dataset?

# Paste the following code into script.py to learn more about this data:

# What happens when you press “Run”?

# print(df.info())


import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

print(df.head())

print(df.info())


###################################################################

# Select Columns

# There are two possible syntaxes for selecting all values from a column:

# Select the column as if you were selecting a value from a dictionary using a key. In our example, we would type customers['age'] to select the ages.
# If the name of a column follows all of the rules for a variable name (doesn’t start with a number, doesn’t contain spaces or special characters, etc.), then you can select it using the following notation: df.MySecondColumn. In our example, we would type customers.age.
  
  
# 1.
# The DataFrame df represents data collected by four health clinics run by the same organization. Each row represents a month from January through June and shows the number of appointments made at four different clinics.

# You want to analyze what’s been happening at the North location. Create a variable called clinic_north that contains ONLY the data from the column clinic_north.

# 2.
# What exactly have you selected?

# After you create the variable, enter the command:

# print(type(clinic_north))
# to see what data type you’ve created.

# How is this different from what you get if you type the following?

# print(type(df))

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north']
print(type(clinic_north))
print(type(df))
print(clinic_north)


###################################################################

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)


clinic_north_south = df[['clinic_north','clinic_south']]
print(clinic_north_south)
print(type(clinic_north_south))

###################################################################

# Select Rows

# using iloc()
# iloc = index location

# You are getting ready to staff the clinic for March this year. You want to know how many visits took place in March last year, to help you prepare.

# Write a command that will produce a Series made up of the March data from df from all four clinic sites and save it to the variable march.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march = df.iloc[2]
print(march)


###################################################################

# Selecting Multiple Rows

# using list location methods, -1 or 4:4 or -3: you can select multiple rows

# 1.
# One of your doctors thinks that there are more clinic visits in the late Spring.

# Write a command that will produce a DataFrame made up of the data for April, May, and June from df for all four sites (rows 3 through 6), and save it to april_may_june.

# 2.
# Inspect april_may_june using print.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df.iloc[-3:]
print(april_may_june)

###################################################################

# Select Rows with Logic I

# In Python, == is how we test if a value is exactly equal to another value.
# df[df.age == 30]

# Greater Than, > — Here, we select all rows where the customer’s age is greater than 30:
# df[df.age > 30]

# Less Than, < — Here, we select all rows where the customer’s age is less than 30:
# df[df.age < 30]

# Not Equal, != — This snippet selects all rows where the customer’s name is not Clara Oswald:
# df[df.name != 'Clara Oswald']

# You’re going to staff the clinic for January of this year. You want to know how many visits took place in January of last year, to help you prepare.

# Create variable january using a logical statement that selects the row of df where the 'month' column is 'January'.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january = df[df.month == 'January']
print(january)


###################################################################

# Select Rows with Logic II

# In Python, | means “or” and & means “and”.
# 1.
# You want to see how the number of clinic visits changed between March and April.

# Create the variable march_april, which contains the data from March and April. Do this using two logical statements combined using |, which means “or”.

# 2.
# Inspect march_april using print.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march_april = df[(df.month == 'March') |
                 (df.month == 'April')]

print(march_april)

###################################################################

# Select Rows with Logic III

# Another doctor thinks that you have a lot of clinic visits in the late Winter.

# Create the variable january_february_march, containing the data from January, February, and March. Do this using a single logical statement with the isin command.


import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january_february_march = df[df.month.isin(['January',
                                           'February',
                                           'March'])]

print(january_february_march)

#####################################################################

# Setting indices

# 1.
# Examine the code in the workspace. Note that df2 is a subset of rows from df.

# Type the following and press “Run”:

# print(df2)
# Note that the indices on df2 are not consecutive.

# 2.
# Create a new DataFrame called df3 by resetting the indices on df2 (don’t use inplace or drop). Did df2 change after you ran this command?

# 3.
# Reset the indices of df2 by using the keyword inplace=True and drop=True. Did the indices of df2 change? How is df2 different from df3?

import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]
print(df2)

df3 = df2.reset_index()

print(df3)

# by not assigning this to a new variable it changes DF2:

df2.reset_index(inplace = True, drop = True)
print(df2)

###################################################################

# Review

# 1.
# In this example, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store. You’ve seen this data; now it’s your turn to work with it!

# Load the data from shoefly.csv into the variable orders.

# 2.
# Inspect the first 5 lines of the data.

# 3.
# Your marketing department wants to send out an email blast to everyone who ordered shoes!

# Select all of the email addresses from the column email and save them to a variable called emails.

# 4.
# Frances Palmer claims that her order was wrong. What did Frances Palmer order?

# Use logic to select that row of orders and save it to the variable frances_palmer.

# 5.
# We need some customer reviews for our comfortable shoes. Select all orders for shoe_type: clogs, boots, and ballet flats and save them to the variable comfy_shoes.
  
  
import codecademylib
import pandas as pd

# 1
orders = pd.read_csv('shoefly.csv')

# 2
# print(orders.head())

# 3
emails = orders['email']
# print(emails)

# 4
frances_palmer = orders[(orders.first_name == 'Fances') |
                        (orders.last_name == 'Palmer')]

# print(frances_palmer)

# 5
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 
                                            'boots', 
                                            'ballet flats'])]
print(comfy_shoes)
                         

###################################################################

# Adding a Column 1


# The DataFrame df contains information on products sold at a hardware store. Add a column to df called 'Sold in Bulk?', which indicates if the product is sold in bulk or individually. The final table should look like this:

# Product ID	Product Description	Cost to Manufacture	Price	Sold in Bulk?
# 1	3 inch screw	0.50	0.75	Yes
# 2	2 inch nail	0.10	0.25	Yes
# 3	hammer		3.00	5.50	No
# 4	screwdriver	2.50	3.00	No

import codecademylib
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df)

###################################################################

# Adding a Column 2

# To have all rows the same:

# Add a column to df called Is taxed?, which indicates whether or not to collect sales tax on the product. It should be 'Yes' for all rows.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Is taxed?'] = 'Yes'

print(df)

###################################################################

# Adding a Column 3
# To calculate a new column using other columns
# If a column name does not conform to the rules for variable names the syntax will be different

# Add a column to df called 'Margin', which is equal to the difference between the Price and the Cost to Manufacture.

import codecademylib
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add column here
df['Margin'] = df.Price - df['Cost to Manufacture'] 

print(df)

###################################################################

# Performing column operators

# Apply the function lower to all names in column 'Name' in df. Assign these new names to a new column of df called 'Lowercase Name'.

import codecademylib
from string import lower
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df.Name.apply(lower)

print(df)

###################################################################

# Reviewing Lambda

# Create a lambda function mylambda that returns the first and last letters of a string, assuming the string is at least 2 characters long. For example:
# print(mylambda('This is a string'))
# should produce:
# 'Tg'

mylambda = lambda string: string[0] + string[-1]
print(mylambda('This is a string'))

###################################################################

# Reviewing Lambda Function: If Statements

# You are managing the webpage of a somewhat violent video game and you want to check that each user’s age is 13 or greater when they visit the site.

# Write a lambda function that takes an inputted age and either returns Welcome to BattleCity! if the user is 13 or older or You must be over 13 if they are younger than 13. Your lambda function should be called mylambda.

import codecademylib
mylambda = lambda x: 'Welcome to BattleCity!' \
	if x >= 13 \
  else 'You must be over 13'

# I did this:

mylambda2 = lambda age: 'Welcome to BattleCity!' if age >= 13 else 'You must be over 13'

print(mylambda(14))
print(mylambda2(14))

###################################################################

# Applying a Lambda to a Column and creating a new column

# Create a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).

# The DataFrame df represents the hours worked by different employees over the course of the week. It contains the following columns:

# 'name': The employee’s name
# 'hourly_wage': The employee’s hourly wage
# 'hours_worked': The number of hours worked this week
# Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.

import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)


###################################################################

# Applying a Lambda to a Row

# If an employee worked for more than 40 hours, she needs to be paid overtime (1.5 times the normal hourly wage).

# For instance, if an employee worked for 43 hours and made $10/hour, she would receive $400 for the first 40 hours that she worked, and an additional $45 for the 3 hours of overtime, for a total for $445.

# Create a lambda function total_earned that accepts an input row with keys hours_worked and hourly_wage and uses an if statement to calculate the hourly wage.

# Use the lambda function total_earned and apply to add a column total_earned to df with the total amount earned by each employee.

import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)



###################################################################

# Renaming Columns

# The DataFrame df contains data about movies from IMDb.

# We want to present this data to some film producers. Right now, our column names are in lower case, and are not very descriptive. Let’s modify df using the .columns attribute to make the following changes to the columns:
  

import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)


###################################################################


# Renaming Columns II

# If we didn’t know that df was a table of movie ratings, the column name might be confusing.

# To clarify, let’s rename name to movie_title.

# Use the keyword inplace=True so that you modify df rather than creating a new DataFrame!

import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns={
  'name': 'movie_title'},
  inplace=True)          

print(df)

###################################################################

# 1.
# Once more, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store.

# More messy order data has been loaded into the variable orders. Examine the first 5 rows of the data using print and head.

# 2.
# Many of our customers want to buy vegan shoes (shoes made from materials that do not come from animals). Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.

# 3.
# Our marketing department wants to send out an email to each customer. Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.

import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)


###################################################################

# Petal Power Inventory
# You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

# If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

# Answer Customer Emails
# 1.
# Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.

# 2.
# Inspect the first 10 rows of inventory.

# 3.
# The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.

# 4.
# A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.

# 5.
# Another customer emails to ask what types of seeds are sold at the Brooklyn location.

# Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.

# Inventory
# 6.
# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.

# 7.
# Petal Power wants to know how valuable their current inventory is.

# Create a column called total_value that is equal to price multiplied by quantity.

# 8.
# The Marketing department wants a complete description of each product for their catalog.

# The following lambda function combines product_type and product_description into a single string:

# combine_lambda = lambda row: \
#     '{} - {}'.format(row.product_type,
#                      row.product_description)
# Paste this function into script.py.

# 9.
# Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.

import codecademylib
import pandas as pd

#1
inventory = pd.read_csv('inventory.csv')

#2
# print(inventory.head(10))

#3
staten_island = inventory.head(10)
# print(staten_island)

#4
# product_request = staten_island['product_description']
#or
product_request = staten_island.product_description
# print(product_request)

#5
seed_request = inventory[(inventory.location == 'Brooklyn') &
                         (inventory.product_type == 'seeds')]
# print(seed_request)

#6
in_stock = lambda row: True if row.quantity > 0 else False
inventory['in_stock'] = inventory.apply(in_stock, axis=1)
# print(inventory)

#7
inventory['total_value'] = inventory.price * inventory.quantity
# print(inventory)

#8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] =  inventory.apply(combine_lambda, axis=1)
print(inventory)
      
  




###################################################################




###################################################################




###################################################################







