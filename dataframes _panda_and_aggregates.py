# Calculating Column Statistics
# In the previous lesson, you learned how to perform operations on each value in a column using apply.

# In this exercise, you will learn how to combine all of the values from a column for a single calculation.

# Some examples of this type of calculation include:

# The DataFrame customers contains the names and ages of all of your customers. You want to find the median age:
# print(customers.age)
# >> [23, 25, 31, 35, 35, 46, 62]
# print(customers.age.median())
# >> 35
# The DataFrame shipments contains address information for all shipments that you’ve sent out in the past year. You want to know how many different states you have shipped to (and how many shipments went to the same state).
# print(shipments.state)
# >> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
# print(shipments.state.nunique())
# >> 3
# The DataFrame inventory contains a list of types of t-shirts that your company makes. You want a list of the colors that your shirts come in.
# print(inventory.color)
# >> ['blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'orange', 'orange', 'orange']
# print(inventory.color.unique())
# >> ['blue', 'green', 'orange']
# The general syntax for these calculations is:

# df.column_name.command()
# The following table summarizes some common commands:

# mean
# std
# median
# max
# min
# nunique
# unique

# 1.
# Once more, we’ll revisit our orders from ShoeFly.com. Our new batch of orders is in the DataFrame orders. Examine the first 10 rows using the following code:

# print(orders.head(10))
# 2.
# Our finance department wants to know the price of the most expensive pair of shoes purchased. Save your answer to the variable most_expensive.

# 3.
# Our fashion department wants to know how many different colors of shoes we are selling. Save your answer to the variable num_colors.

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

# print(orders.head(10))

most_expensive = orders.price.max()
print(most_expensive)

num_colors = orders.shoe_color.nunique()
print(num_colors)


######################################################################################################################


# Calculating Aggregate Functions I

# In general, we use the following syntax to calculate aggregates:

# df.groupby('column1').column2.measurement()
# where:

# column1 is the column that we want to group by ('student' in our example)
# column2 is the column that we want to perform a measurement on (grade in our example)
# measurement is the measurement function we want to apply (mean in our example)

# 1.
# Let’s return to our orders data from ShoeFly.com.

# In the previous exercise, our finance department wanted to know the most expensive shoe that we sold.

# Now, they want to know the most expensive shoe for each shoe_type (i.e., the most expensive boot, the most expensive ballet flat, etc.).

# Save your answer to the variable pricey_shoes.

# 2.
# Examine the object that you just created using:

# print(pricey_shoes)
# 3.
# What type of object is pricey_shoes?

# Enter the following code to check:

# print(type(pricey_shoes))

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))


#######################################################################

# Calculating Aggregate Functions II

# Generally, youll always see a groupby statement followed by reset_index, this will transform the series into a dataframe

# df.groupby('column1').column2.measurement()
#     .reset_index()

# 1.
# Modify your code from the previous exercise so that it ends with reset_index, which will change pricey_shoes into a DataFrame.

# 2.
# Examine the object that you’ve just created using the following code:

# print(pricey_shoes)
# 3.
# Now, what type of object is pricey_shoes?

# Enter the following code to check:

# print(type(pricey_shoes))

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))


#######################################################################

# Calculating Aggregate Functions III

# Numpy Percentile

# 1.
# Once more, we’ll return to the data from ShoeFly.com. Our Marketing team says that it’s important to have some affordably priced shoes available for every color of shoe that we sell.

# Let’s calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. Save the data to the variable cheap_shoes.

# Note: Be sure to use reset_index() at the end of your query so that cheap_shoes is a DataFrame.

# 2.
# Display cheap_shoes using print.

import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

print(cheap_shoes)

#######################################################################

# Calculating Aggregate Functions IV
# grouping by multiple columns

# example using mean of one column where grouping by 2 other columns
# df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()

# 1.
# At ShoeFly.com, our Purchasing team thinks that certain shoe_type/shoe_color combinations are particularly popular this year (for example, blue ballet flats are all the rage in Paris).

# Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.

# You should be able to do this using groupby and count().

# Note: When we’re using count(), it doesn’t really matter which column we perform the calculation on. You should use id in this example, but we would get the same answer if we used shoe_type or last_name.

# Remember to use reset_index() at the end of your code!

# 2.
# Display shoe_counts using print.


import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)

shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()
print(shoe_counts)

#######################################################################

# Pivot Tables

# In Pandas, the command for pivot is:

# df.pivot(columns='ColumnToPivot',
#          index='ColumnToBeRows',
#          values='ColumnToBeValues')
# 1.
# In the previous example, you created a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased for ShoeFly.com.

# The purchasing manager complains that this DataFrame is confusing.

# Make it easier for her to compare purchases of different shoe colors of the same shoe type by creating a pivot table. Save your results to the variable shoe_counts_pivot.

# Your table should look like this:

# shoe_type	black	brown	navy	red	white
# ballet flats	…	…	…	…	…
# sandals	…	…	…	…	…
# stilettos	…	…	…	…	…
# wedges	…	…	…	…	…
# Remember to use reset_index() at the end of your code!

# 2.
# Display shoe_counts_pivot using print.

import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color',
                                      index='shoe_type',
                                      values='id'
                                      ).reset_index()

print(shoe_counts_pivot)

#######################################################################

# Aggregate Statistics in Pandas review

# 1.
# Let’s examine some more data from ShoeFly.com. This time, we’ll be looking at data about user visits to the website (the same dataset that you saw in the introduction to this lesson).

# The data is a DataFrame called user_visits. Use print and head() to examine the first few rows of the DataFrame.

# 2.
# The column utm_source contains information about how users got to ShoeFly’s homepage. For instance, if utm_source = Facebook, then the user came to ShoeFly by clicking on an ad on Facebook.com.

# Use a groupby statement to calculate how many visits came from each of the different sources. Save your answer to the variable click_source.

# Remember to use reset_index()!

# 3.
# Paste the following code into script.py so that you can see the results of your previous groupby:

# print(click_source)
# 4.
# Our Marketing department thinks that the traffic to our site has been changing over the past few months. Use groupby to calculate the number of visits to our site from each utm_source for each month. Save your answer to the variable click_source_by_month.

# 5.
# The head of Marketing is complaining that this table is hard to read. Use pivot to create a pivot table where the rows are utm_source and the columns are month. Save your results to the variable click_source_by_month_pivot.

# It should look something like this:

# utm_source	1 - January	2 - February	3 - March
# email	…	…	…
# facebook	…	…	…
# google	…	…	…
# twitter	…	…	…
# yahoo	…	…	…
# 6.
# View your pivot table by pasting the following code into script.py:

# print(click_source_by_month_pivot)


import codecademylib
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())

click_source = user_visits.groupby('utm_source').id.count().reset_index()
# print(click_source)

click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index()
# print(click_source_by_month)

click_source_by_month_pivot = click_source_by_month.pivot(columns='month',index='utm_source',values='id').reset_index() 
print(click_source_by_month_pivot)

    

#######################################################################

# Challenge - A/B Testing for ShoeFly.com

# 1.
# Examine the first few rows of ad_clicks.

# 2.
# Your manager wants to know which ad platform is getting you the most views.

# How many views (i.e., rows of the table) came from each utm_source?

# 3.
# If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.

# 4.
# We want to know the percent of people who clicked on ads from each utm_source.

# Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.

# 5.
# Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

# Save your results to the variable clicks_pivot.

# 6.
# Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

# Was there a difference in click rates for each source?

# Analyzing an A/B Test
# 7.
# The column experimental_group tells us whether the user was shown Ad A or Ad B.

# Were approximately the same number of people shown both adds?

# 8.
# Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

# 9.
# The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

# Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.

# 10.
# For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.

# 11.
# Compare the results for A and B. What happened over the course of the week?

# Do you recommend that your company use Ad A or Ad B


import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head(20))

source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(source_count)

# Why doesn't this work
# is_click = lambda row: True if ~row.ad_click_timestamp.isnull() else False
# or
# is_click = lambda row: True if row.ad_click_timestamp is not None else False
# ad_clicks['is_click'] = ad_clicks.apply(is_click, axis=1)
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
# print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', 
                                      index='utm_source', 
                                      values='user_id').reset_index()
# print(clicks_pivot)

clicks_pivot['percent_clicked'] = (clicks_pivot[True]) / (clicks_pivot[False] + clicks_pivot[True])
# print(clicks_pivot)

# 7.
count_ad_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(count_ad_group)

# 8.
# grouping by ex_group and is_click
ad_group_cp = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

# pivoting
ad_group_cp_pivot = ad_group_cp.pivot(columns = 'is_click',
                                                    index = 'experimental_group',
                                                    values = 'user_id'
                                                    ).reset_index()
# adding click percentage column to pivot
ad_group_cp_pivot['click_percentage'] = (ad_group_cp_pivot[True] /                                         (ad_group_cp_pivot[True] + ad_group_cp_pivot[False])) * 100
# print(ad_group_cp_pivot)

# 9.
a_clicks = ad_clicks[(ad_clicks.experimental_group == 'A')]
b_clicks = ad_clicks[(ad_clicks.experimental_group == 'B')]

# 10.
# For group A
# grouping by day and is_click
a_clicks_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

# pivoting
a_clicks_day_pivot = a_clicks_day.pivot(columns = 'is_click',
                                        index = 'day',
                                        values = 'user_id'
                                       ).reset_index()

# adding a percentage column
a_clicks_day_pivot['click_percentage'] = (a_clicks_day_pivot[True] /                                         (a_clicks_day_pivot[True] + a_clicks_day_pivot[False])) * 100
# print(a_clicks_day_pivot)

# For group B
# grouping by day and is_click
b_clicks_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

# pivoting
b_clicks_day_pivot = b_clicks_day.pivot(columns = 'is_click',
                                        index = 'day',
                                        values = 'user_id'
                                       ).reset_index()

# adding a percentage column
b_clicks_day_pivot['click_percentage'] = (b_clicks_day_pivot[True] /                                         (b_clicks_day_pivot[True] + b_clicks_day_pivot[False])) * 100

print(ad_group_cp_pivot)
print(a_clicks_day_pivot)
print(b_clicks_day_pivot)

# 11.
# I would recommend Ad A, it has a higher overall click percentage, and had a higher click percentage each day except Tuesday, although that day was very close. 
# the click percentage on Weds is much lower in both groups, suggest not running the ad that day if it costs per day. 





#######################################################################


#######################################################################


#######################################################################


#######################################################################










