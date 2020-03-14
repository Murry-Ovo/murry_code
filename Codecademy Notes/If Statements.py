# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  if num2 > num1 and num2 > num3:
    return num2
  if num3 > num1 and num3 > num2:
    return num3    
  else:
    return "It's a tie!"
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"


---------------------


# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill,rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
  
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True


-----------------------


# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if (num % 10) == 0:
    return True
  else:
    return False
  
  

# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False


------------------------------


# Write your large_power function here:
def large_power(base, exponent):
  if (base ** exponent) > 5000:
    return True
  else:
    return False



# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


---------------------------------------



# Write your twice_as_large function here:
def twice_as_large(num1,num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False
  
  
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True