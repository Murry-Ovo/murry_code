# Inner Merge
# basic syntax:
# new_df = pd.merge(orders, customers)

# 1.
# You are an analyst Cool T-Shirts Inc. You are going to help them analyze some of their sales data.

# There are two DataFrames defined in the file script.py:

# sales contains the monthly revenue for Cool T-Shirts Inc. It has two columns: month and revenue.
# targets contains the goals for monthly revenue for each month. It has two columns: month and target.
# Create a new DataFrame sales_vs_targets which contains the merge of sales and targets.

# 2.
# Display sales_vs_targets using print.

# 3.
# Cool T-Shirts Inc. wants to know the months when they crushed their targets.

# Select the rows from sales_vs_targets where revenue is greater than target. Save these rows to the variable crushing_it.

import codecademylib
import pandas as pd

sales = pd.read_csv('sales.csv')
# print(sales)
targets = pd.read_csv('targets.csv')
# print(targets)

sales_vs_targets = pd.merge(sales, targets)
# print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
print(crushing_it)


###############################################################################################

# Inner Merge 3
# New syntax:
# new_df = orders.merge(customers)
# this is useful for merging more than one table as you can chain, merge a to b, then merge that with c and so on
# 1.
# We have some more data from Cool T-Shirts Inc. The number of men’s and women’s t-shirts sold per month is in a file called men_women_sales.csv. Load this data into a DataFrame called men_women.

# 2.
# Merge all three DataFrames (sales, targets, and men_women) into one big DataFrame called all_data.

# 3.
# Display all_data using print.

# 4.
# Cool T-Shirts Inc. thinks that they have more revenue in months where they sell more women’s t-shirts.

# Select the rows of all_data where:

# revenue is greater than target
# AND

# women is greater than men
# Save your answer to the variable results.

import codecademylib
import pandas as pd

sales = pd.read_csv('sales.csv')
# print(sales)
targets = pd.read_csv('targets.csv')
# print(targets)

men_women = pd.read_csv('men_women_sales.csv')

all_data = targets.merge(sales)\
                  .merge(men_women)
# print(all_data)

results = all_data[(all_data.revenue > all_data.target) &
                   (all_data.women > all_data.men)]
print(results)


###############################################################################################


# Merge on Specific Columns

# pd.merge() automatically merges on columns with the same name, as this is not always right you mihgt want to rename a column on one of your tables during the merge
# basic syntax:
  
# pd.merge(
#     orders,
#     customers.rename(columns={'id': 'customer_id'}))


import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

orders_products = pd.merge(
	orders,
	products.rename(columns={'id':'product_id'})
)
print(orders_products)

###############################################################################################


# Merge on Specific Columns II

# In the same way as renaming columns to perform a match, you can use left on and right on to specify which column in the left table matches which column in the right table

# if this creates duplicate column names then python will add _x and _y to the column names

# if you want to specify a suffix you can do so within the merge. 

# 1.
# Merge orders and products using left_on and right_on. Use the suffixes _orders and _products. Save your results to the variable orders_products.

# 2.
# Display orders_products using print.


import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
  orders,
  products,
  left_on='product_id',
  right_on='id',
  suffixes=['_orders','_products']
)

print(orders_products)

###############################################################################################

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)
print(products)

merged_df = pd.merge(
  orders,
  products,
  left_on='product_id',
  right_on='product_id',
  suffixes=['_orders','_products'])
            
print(merged_df)

# 1.
# We’ve just released a new product with product_id equal to 5. People are ordering this product, but we haven’t updated the products table.

# In script.py, you’ll find two DataFrames: products and orders. Inspect these DataFrames using print.

# Notice that the third order in orders is for the mysterious new product, but that there is no product_id 5 in products.

# 2.
# Merge orders and products and save it to the variable merged_df.

# Inspect merged_df using:

# print(merged_df)
# What happened to order_id 3?
# it disappeared!!



###############################################################################################

# Outer Merge
# Just like an outer join, retains all rows from both tables and produces nan or None values for the missing data
# As inner merges are the default to perform an outer merge you need to specify this within the merge function like this:
# pd.merge(table_a, tables_b, how='outer')

import codecademylib
import pandas as pd

store_a = pd.read_csv('store_a.csv')
# print(store_a)
store_b = pd.read_csv('store_b.csv')
# print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print(store_a_b_outer)

###############################################################################################


# Left and Right Merge

# 1.
# Let’s return to the two hardware stores, Store A and Store B. They’re not quite sure if they want to merge into a big Super Store just yet.

# Store A wants to find out what products they carry that Store B does not carry. Using a left merge, combine store_a to store_b and save the results to store_a_b_left.

# The items with null in store_b_inventory are carried by Store A, but not Store B.

# 2.
# Now, Store B wants to find out what products they carry that Store A does not carry. Use a left join, to combine the two DataFrames but in the reverse order (i.e., store_b followed by store_a) and save the results to the variable store_b_a_left.

# Which items are not carried by Store A, but are carried by Store B?

# 3.
# Paste the following code into script.py:

# print(store_a_b_left)
# print(store_b_a_left)
# What do you notice about these two DataFrames?

# How are they different?

# How are they the same?

import codecademylib
import pandas as pd

store_a = pd.read_csv('store_a.csv')
# print(store_a)
store_b = pd.read_csv('store_b.csv')
# print(store_b)

store_a_b_left = pd.merge(store_a,
                         store_b,
                         how='left')

store_b_a_left = pd.merge(store_b,
                         store_a,
                         how='left')

print(store_a_b_left)
print(store_b_a_left)

###############################################################################################

# Concatenate DataFrames

# when all columns are the same in multiple dataframes you can create one new dataframe by using concat (similar to a UNION)
# basic syntax:
# pd.concat([df1, df2, df3])

import codecademylib
import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)


menu = pd.concat([bakery, ice_cream])
print(menu)

###############################################################################################


# Merging Multiple Dataframes Review:
  
# 1.
# Cool T-Shirts Inc. just created a website for ordering their products. They want you to analyze two datasets for them:

# visits contains information on all visits to their landing page
# checkouts contains all users who began to checkout on their website
# Use print to inspect each DataFrame.

# 2.
# We want to know the amount of time from a user’s initial visit to the website to when they start to check out.

# Use merge to combine visits and checkouts and save it to the variable v_to_c.

# 3.
# In order to calculate the time between visiting and checking out, define a column of v_to_c called time by pasting the following code into script.py:

# v_to_c['time'] = v_to_c.checkout_time - \
#                  v_to_c.visit_time

# print(v_to_c)
# 4.
# To get the average time to checkout, paste the following code into script.py:

# print(v_to_c.time.mean())



import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c = pd.merge(visits, checkouts)

v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time

print(v_to_c)
print(v_to_c.time.mean())

###############################################################################################



###############################################################################################




###############################################################################################



###############################################################################################




###############################################################################################