# 1. EVEN AND ODD NUMBERS

lst1=[10,501,22,37,100,999,87,351]
lst_even=[]
lst_odd=[]

for i in lst1:
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)

print(lst_odd)
print(lst_even)

# 4.SUM OF FIRST AND LAST DIGIT OF AN INTEGER

n = int(input("Enter the number: "))
n = str(n)
first_digit = int(n[0])
last_digit = int(n[-1])
sum1 = first_digit + last_digit
print(sum1)

# 6. DUPLICATES IN THE THREE LISTS

lst1 = [10,20,30,'daniel']
lst2 = [40,50,'daniel',20]
lst3 = ['daniel',60,20,30]
duplicate_lst = []
for i in lst1:
    if i in lst2 and i in lst3:
        duplicate_lst.append(i)

print(duplicate_lst)

#  7. NON-REPEATING ELEMENTS IN A LIST

lst = [1,2,4,4,5,5,9]
non_repeating = {}
for i in lst:
    if i not in non_repeating:
        non_repeating[i] = 1
    else:
        non_repeating[i] += 1

result = []
for key,value in non_repeating.items():
    if value == 1:
        result.append(key)

print(result)

#  8. MINIMUM ELEMENT IN A LIST

given_lst = [89,100,76,94,67]
given_lst.sort()
min_element = given_lst[0]
print("Minimum element is: ",min_element)

# 2. COUNT AND LIST OF ALL PRIME NUMBERS

lst2 =[10,501,22,37,100,999,87,351]
lst_prime=[]

for i in lst2:
    is_prime = True
    for n in range(2,int(i ** 0.5) + 1):
        if i % n == 0:
            is_prime = False
            break
    if is_prime == True and i >1 :
            lst_prime.append(i)


print("Total count of prime numbers: ",len(lst_prime))
print("List of prime numbers; ",lst_prime)
