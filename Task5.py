# FILTER FUNCTION
# 1. Expected output of the following python code
# data = [10,501,22,37,100,999,87,351]
# result = filter(lambda x:x>4 , data)
# print(list(result))

# All the elements in given list are > 4 so output has all the elements
#output: [10,501,22,37,100,999,87,351]   

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
        yield a         # using generator
        a,b = b,a+b

series = list(fibonacci(50))
print(series)

# 4. Python code to validate regular expression for the following
# a. email address
# b. mobile numbers of bangladesh
# c. telephone numbers of USA
# d. 16 character alphanumeric password composed of alphabets of upper case,lower case,special characters,
# numbers

import re                                     # importing regular expression from external library
email_id = "'danielprem97@gmail.com"
print(re.findall('@',email_id))              # a. validating gmail 
print(re.findall('.com',email_id))
bangladesh_phone = '+8801712345678'              # b. Phone Number of Bangladesh should start with country code 
print(re.search(r'^\+880',bangladesh_phone))
telephone_usa = '+1 215 555-1234'
print(re.search(r"^\+1",telephone_usa))       # c. Telephone Number of USA should start with country code  
password = 'Xyzabcdefgh#123!'
print(re.findall('[a-z]',password))            # d. to find lower case alphabets
print(re.findall('[A-Z]',password))            # d. to find upper case alphabets
print(re.findall('\d',password))               # to find numbers (digits from 0-9)
print(re.findall('\W',password))               # to find special characters (not a word character)
print(re.match(".{16}",password))              # should have 16 characters









