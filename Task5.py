# FILTER FUNCTION
# 1. Expected output of the following python code
# data = [10,501,22,37,100,999,87,351]
# result = filter(lambda x:x>4 , data)
# print(list(result))

#output : [10,501,22,37,100,999,87,351]        # All the elements in given list are > 4 so output has all the elements

# 2. Python code using lambda function to check every element of a list is an integer or string
# LAMBDA FUNCTION

data = ['mango',24,'dani',7890]
result =list(map(lambda x: "Integer" if type(x) == int else "string",data))  #using if in lambda function
print(result)

# 3. Fibonacci series using python lambda function from 1 to 50
# LAMBDA FUNCTION

def fibonacci(x):
    a,b = 1,1           # first two elements of fibonacci series
    while a <= x:
        yield a
        a,b = b,a+b

series = list(fibonacci(50))
print(series)

# 4. Python code to validate regular expression for the following
# a. email address
# b. mobile numbers of bangladesh
# c. telephone numbers of USA
# d. 16 character alphanumeric password composed of alphabets of upper case,lower case,special characters,numbers

import re                                      # Importing regular expression from external library
email_id = "danielprem97@gmail.com"
print(re.findall('@',email_id))
print(re.findall('.com',email_id))
phone_number = '+8801712345678'
print(re.search('^880',phone_number))          # Number should start with country code  








