# 1. Total number of vowels and count of each vowel in the given string

text = "Guvi Geeks Network Private Limited"
vowels = {'A':0,'E':0,'I':0,'O':0,'U':0}
text = text.upper()

for i in text:
    if i in vowels:
        vowels[i] += 1

total_vowels = sum(vowels.values())

print("Count of each vowel : ",vowels)
print("Total number of vowels : ",total_vowels)

# 2. Pyramid of numbers from 1 to 20 using for loop

n = 20
strt = 1
rows = 6

for i in range(1,rows + 1):
    for j in range(i):
       if strt <= n:
        print(strt, end=" ")
        strt += 1
       else:
           break
    print()

# 3. Write a program that takes a string and returns  a new string with all the vowels removed

oldstr = input("Enter the string: ")
vowels1 = ('a','e','i','o','u')
oldstr = oldstr.lower()
newstr = ""

for i in oldstr:
    if i not in vowels1:
        newstr += i

print("Non-vowel string : ",newstr)

# 4. Write a program that takes a string and returns the number of unique characters in it

str2 = input("Enter the string: ")
str2 = str2.lower()
str2 = str2.replace(" ","")
myset = set(str2)
print("number of unique characters :" ,len(myset))

# 5. Write a program that takes a string and returns true if it is a palindrome or false otherwise

mystr = input("Enter the string: ")
mystr = mystr.lower().replace(" ","")
rev_mystr = mystr[::-1]
if mystr == rev_mystr:
    print(True)
else:
    print(False)

# 7. Write a program that takes a string and returns the most frequent character in it

txt = input("Enter the string: ")
txt = txt.lower().replace(" ","")
frequency = {}

for i in txt:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

max_char = max(frequency,key=frequency.get)
print("Most frequent character:",max_char)

# 8. Write a program that takes a string and returns true if its an anagram of another string or false otherwise

str_x = input("Enter the string: ")
str_y = input("Enter the another string: ")
str_x = str_x.lower().replace(" ","")
str_y = str_y.lower().replace(" ","")
sorted_x = sorted(str_x)
sorted_y = sorted(str_y)
if sorted_x == sorted_y :
    print(True)
else:
    print(False)

# 9. Write a program that takes a string and returns the number of words in it

str1 = input("Enter the string: ")
str2 = str1.split()
print("Number of words :",len(str2))
















