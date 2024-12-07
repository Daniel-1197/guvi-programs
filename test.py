#1.	What is Python
# python is a high level,intepreted and general purpose language.some of it features are;
#simple and easy as it has simple syntax,execute code line by line
#it has dynamic typing so  we dont need to declare the data type.
#workes on various operating system
#use cases of python.
#*web devlopment
#*mobile and desktop application devlopment



#2.	Data Types: What are the basic data types available in Python

#Ans. the basic datatypes available in python are integers,float,string,boolean,lisyt,tuple,set and dicitonary
#integer:x=5
#float:x=5.4
#string:name="danny"
#boolean:=true or false
#list=[22,3,"danny"]
#tuple=(3,4,20,'a',"prem")
#myset={"daniel",20}
#dictionary={'name':'disney'}

#3.	List Operations: Given the list numbers = [1, 2, 3, 4, 5], how would you add the number 6 to the end of the list?

#lst1=[1,2,3,4,5,]
#lst1.append(6)
#print(lst1)

#4.	String Manipulation: How can you convert the string "PYTHON" to lowercase using a Python method?

#txt="PYTHON"
#result=txt.lower()
#print(result)

#5.	Conditional Statements: Write a simple Python program that prints "Even" if the variable num is an even number, and "Odd" if the variable num is an odd number

#num1=int(input("enter the no:"))
#if num1 %2==0:
    #print("even")
#else:
    #print("odd")

#6.	Functions: Define a Python function named is_prime that takes a single integer argument and returns True if the integer is a prime number, otherwise returns False

#def is_prime(a):
   # if a <=1:
        #return False
    #for i in range(2, int(a**0.5) +1):
        #if a%i==0:
            #return False
    #return True
#print(is_prime(13))

#7.	Loops: How can you loop over and print each item in the list [10, 20, 30, 40, 50] using a for loop?

#num2=[10,20,30,40,50]
#for i in num2:
   # print(i)

#8.	File Handling: Write a Python script that reads a text file named "notes.txt" and prints each line in the file.

with open(file="notes.txt",mode="r") as file_obj:
 print(file_obj.read())


#1.	FizzBuzz Problem: Write a Python program that prints each number from 1 to 100 on a new line. For each multiple of 3, print "Fizz" instead of the number. For each multiple of 5, print "Buzz" instead of the number. For numbers which are multiples of both 3 and 5, print "FizzBuzz".

# for i in range(1,101):
#     if i % 3 ==0:
#         print("Fizz")
#     elif i % 5==0:
#         print("Buzz")
#     elif i % 3==0 and i % 5==0:
#         print("FizzBuzz")
#     else:
#         print(i)

#2.	Reverse a String: Reverse a string [‘1’,2,’hello’,True] without using any built-in function

#lst1= [‘1’,2,’hello’,True]
#rev_lst



#3.	Find the Missing Number: Given a list of numbers  [1,2,3,4,7,9,6,10]with numbers missing, print the missing number?
# lst2=[1,2,3,4,7,9,6,10]
# minimum_lst2=min(lst2)
# maximum_lst2=max(lst2)
# total_range=range(minimum_lst2,maximum_lst2+1)
# missing_num=[]
# for i in total_range:
#     if i not in lst2:
#         missing_num.append(i)
# print(missing_num)

#4.	Detect Duplicates in an Array: Print duplicate number (1,2,3,3,4,5) ?
lst3=[1,2,3,3,4,5]
seen=[]
duplicates=[]
for i in lst3:
    if i in seen:
        duplicates.append(i)
    else:
        seen.append(i)
print(duplicates)

#5 palindrome
# mystr = input("Enter the string: ")
# mystr = mystr.lower().replace(" ","")
# rev_mystr = mystr[::-1]
# if mystr == rev_mystr:
#     print(True)
# else:
#     print(False)

#6.anagram
# str_x = input("Enter the string: ")
# str_y = input("Enter the another string: ")
# str_x = str_x.lower()
# str_y = str_y.lower()
# sorted_x = sorted(str_x)
# # sorted_y = sorted(str_y)
# # if sorted_x == sorted_y :
# #     print(True)
# # else:
# #     print(False)








