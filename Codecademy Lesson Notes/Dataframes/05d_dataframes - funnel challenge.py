'''1.
Inspect the DataFrames using print and head:

visits lists all of the users who have visited the website
cart lists all of the users who have added a t-shirt to their cart
checkout lists all of the users who have started the checkout
purchase lists all of the users who have purchased a t-shirt
2.
Combine visits and cart using a left merge.

3.
How long is your merged DataFrame?

4.
How many of the timestamps are null for the column cart_time?

What do these null rows mean?

5.
What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?

Note: To calculate percentages, it will be helpful to turn either the numerator or the denominator into a float, by using float(), with the number to convert passed in as input. Otherwise, Python will use integer division, which truncates decimal points.

6.
Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

7.
Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.

Examine the result using print and head.

8.
What percentage of users proceeded to checkout, but did not purchase a t-shirt?

9.
Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

How might Cool T-Shirts Inc. change their website to fix this problem?

Average Time to Purchase
10.
Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Start by adding the following column to your DataFrame:

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
11.
Examine the results using:

print(all_data.time_to_purchase)
12.
Calculate the average time to purchase using the following code:

print(all_data.time_to_purchase.mean())'''


import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# 1 - Inspecting the dataframes
# print(visits.head())
# print(cart.head())
# print(checkout.head())
# print(purchase.head())

# 2 - combining visits and cart with a left merge
visits_cart = pd.merge(visits, 
                       cart,
                       how = 'left'
                      )
# print(visits_cart)

#3 - How long is the new dataframe
visits_cart_rows = len(visits_cart)
print('The number of records in visits_cart is: '+str(visits_cart_rows))

# 4 - How many timestamps are NULL from cart_time
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print('The number of null values in cart_time is: '+str(null_cart_times))

# 5 - What percentage of users ended up not placing a t-shirt in their cart
null_cart_time_percentage = float(null_cart_times) / float(visits_cart_rows)
null_cart_time_percentage_formatted = str(round(null_cart_time_percentage*100,2))+'%'
print('The percentage of customers that visited the site but did not put a t-shirt in the cart is '+null_cart_time_percentage_formatted)

print('-----------------------------------------------')

# 6 - repeat the above for cart and checkout
cart_checkout = pd.merge(cart, 
                         checkout,
                         how = 'left'
                        )
# print(cart_checkout)
cart_checkout_rows = len(cart_checkout)
print('The number of records in cart_checkout is: '+str(cart_checkout_rows))

# creating a new list which is just the null records 
null_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
# printing len to work out how many null records
print('The number of null values in checkout is: '+str(null_checkout))

null_checkout_percentage = float(null_checkout) / float(cart_checkout_rows)
null_checkout_percentage_formatted = str(round(null_checkout_percentage*100,2))+'%'
print('The percentage of customers that did not click on checkout after putting a t-shirt in their cart is: '+null_checkout_percentage_formatted)

print('-----------------------------------------------')

# 7 - Merge all 4 datasets 
visits_cart_checkout = pd.merge(visits_cart, 
                                checkout,
                                how = 'left'
                               )
all_data = pd.merge(visits_cart_checkout,
                     purchase,
                     how = 'left'
                    )                           

# creating dataset which is only how many rows in checkout are not null
checkout_rows = all_data[all_data.checkout_time.notnull()].reset_index()
checkout_rows_len = len(checkout_rows)
# print(all_data[all_data.checkout_time.notnull()])

# #how many rows in purchase are null
null_purchase_rows = checkout_rows[checkout_rows.purchase_time.isnull()]
null_purchase_rows_len = len(null_purchase_rows)

print('The number of customers who clicked on checkout is: '+str(checkout_rows_len))
print('The number of customers who clicked on checkout but did not make a purchase is: '+str(null_purchase_rows_len))

null_purchase_percentage = float(null_purchase_rows_len) / float(checkout_rows_len)
null_purchase_percentage_formatted = str(round(null_purchase_percentage*100,2))+'%'
print('The percentage of customers who clicked on checkout but did not make a purchase is: '+null_purchase_percentage_formatted)

print('-----------------------------------------------')

print('''
Findings

The weakest step of the funnel is between visits and cart, where over 80 percent of customers who visit the site do not put a t-shirt in their basket

They could change their website by making it easier to put a tshirt in their basket. make the 'add to basket button' bigger, discount their stock and show the pound and percentage savings to make it very clear how much of a deal people are getting. 

They could improve the pictures of their t-shirts both on and off models so people can see what the designs look like whilst being worn.''')

print('-----------------------------------------------')

all_data['time_to_purchase'] = \
        all_data.purchase_time - \
        all_data.visit_time

# print(all_data.time_to_purchase)
print('The average time from visiting the website to making a purchase is: '+str(all_data.time_to_purchase.mean()))





