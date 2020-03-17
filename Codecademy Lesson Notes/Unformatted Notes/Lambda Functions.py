# Contains A

# Create a lambda function named contains_a that takes an input word and returns True if the input contains the letter 'a'. Otherwise, return False.

#Write your lambda function here
contains_a = lambda word: "a" in word

print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")
 

##################################################

# Long String
# Create a lambda function named long_string that takes an input str and returns True if the string has over 12 characters in it. Otherwise, return False.

#Write your lambda function here
long_string = lambda string: len(string) > 12 

print long_string("short")
print long_string("photosynthesis")


##################################################

# Ends With A
# Create a lambda function named ends_in_a that takes an input str and returns True if the last character in the string is an a. Otherwise, return False.


#Write your lambda function here
ends_in_a = lambda word: word[-1] == 'a'

print ends_in_a("data")
print ends_in_a("aardvark")



##################################################

# Double Or Zero
# Create a lambda function named double_or_zero that takes an integer named num. If num is greater than 10, return double num. Otherwise, return 0.

#Write your lambda function here

double_or_zero = lambda num: num * 2 if num > 10 else 0

print double_or_zero(15)
print double_or_zero(5)


##################################################

# Even/Odd

# Create a lambda function named even_or_odd that takes an integer named num. If num is even, return "even". If num is odd, return "odd".

#Write your lambda function here

even_or_odd = lambda num: "even" if num%2 == 0 else "odd"

print even_or_odd(10)
print even_or_odd(5)



##################################################


# Multiple of Three

# Create a lambda function named multiple_of_three that takes an integer named num. If num is a multiple of three, return "multiple of three". Otherwise, return "not a multiple".

#Write your lambda function here

multiple_of_three = lambda num: "multiple of three" if num%3 == 0 else "not a multiple"

print multiple_of_three(9)
print multiple_of_three(10)

##################################################

# Movie Rating

# Create a lambda function named rate_movie that takes a number named rating. If rating is greater than 8.5, return "I liked this movie". Otherwise return "This movie was not very good".

#Write your lambda function here

rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"

print rate_movie(9.2)
print rate_movie(7.2)



##################################################



# Ones' Place
# Create a lambda function named ones_place that returns the ones’ place of the input num.

#Write your lambda function here

ones_place = lambda num: num%10

print ones_place(123)
print ones_place(4)



##################################################

# Double Square

# Create a lambda function named double_square that takes an input named num. The function should return twice the square of num.

#Write your lambda function here

double_square = lambda num: (num**2)*2

print double_square(5)
print double_square(3)



##################################################


# Add Random
# Create a lambda function named add_random that takes an input named num. The function should return num plus a random integer number between 1 and 10 (inclusive).


import random
#Write your lambda function here

add_random = lambda num: num + random.randint(1,10)

print add_random(5)
print add_random(100)

##################################################



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


##################################################




##################################################




##################################################





##################################################




##################################################




##################################################





##################################################




##################################################




##################################################


