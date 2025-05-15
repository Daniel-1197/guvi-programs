# 1. Total number of vowels and count of each vowel in the given string

input_text = "Guvi Geeks Network Private Limited"
vowels_counts = {'A':0,'E':0,'I':0,'O':0,'U':0}
text = input_text.upper()

for i in text:
    if i in vowels_counts:
        vowels_counts[i] += 1

total_vowels_count = sum(vowels_counts.values())

print("Count of each vowel : ",vowels_counts)
print("Total number of vowels : ",total_vowels_count)

# 2. Pyramid of numbers from 1 to 20 using for loop

max_number = 20
starting_number = 1
rows = 6

for i in range(1,rows + 1):
    for j in range(i):
       if starting_number <= max_number:
        print(starting_number, end=" ")
        starting_number += 1
       else:
           break
    print()

# 3. Write a program that takes a string and returns  a new string with all the vowels removed

old_str = input("Enter the string: ")
vowels = ('a','e','i','o','u')
old_str = old_str.lower()
new_str = ""

for i in old_str:
    if i not in vowels:
        new_str += i

print("Non-vowel string : ",new_str)

# 4. Write a program that takes a string and returns the number of unique characters in it

input_str = input("Enter the string: ")
input_str = input_str.lower()
unique_char = set(input_str)
print("number of unique characters :" ,len(unique_char))

# 5. Write a program that takes a string and returns true if it is a palindrome or false otherwise

palindrome_input = input("Enter the string: ")
reversed_input = palindrome_input[::-1]
if palindrome_input == reversed_input:
    print(True)
else:
    print(False)

# 7. Write a program that takes a string and returns the most frequent character in it

input_txt = input("Enter the string: ")
char_frequency = {}

for i in input_txt:
    if i not in char_frequency:
        char_frequency[i] = 1
    else:
        char_frequency[i] += 1

most_freq_char = ' '
max_frequency = 1
for i in char_frequency:
    if char_frequency[i] > max_frequency:
        max_frequency = char_frequency[i]
        most_freq_char = i
print("Most frequent character:",most_freq_char)

# 8. Write a program that takes a string and returns true if its an anagram of another string or false otherwise

first_str = input("Enter the first string: ")
second_str = input("Enter the second string: ")
if sorted(first_str)== sorted(second_str):
    print(True)
else:
    print(False)

# 9. Write a program that takes a string and returns the number of words in it

sentence = input("Enter the sentence: ")
words_count = sentence.split()
print("Number of words :",len(words_count))
