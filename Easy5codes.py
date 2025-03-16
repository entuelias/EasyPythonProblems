# find the max of 2 numbers
def max_two_number(a,b):
    if a > b:
        return a
    elif b > a :
        return b
    else:
       print("they are equal")

# print(max_two_number(8,5))



# check eveness or oddness
def is_even(x):
    return "Even" if x%2 == 0 else "Odd"

# print(is_even(-90))

# Reverse a String
def string_reverser(string):
    return string[::-1]

# print(string_reverser("kebedeeew"))

# sum of the first n natural numbers
def sum_n(n):
    sum = 0
    for i in range(0,n+1):
        sum+=i
    return sum

# print(sum_n(10))

def sum_two_numbers(a, b):
    return a + b

def find_largest(a, b, c):
    return max(a, b, c)

# count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    counter  = 0
    for i in s:
        if i in vowels:
            counter+=1
    return counter
# print(count_vowels("ahbabiihusaa"))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(2 for char in s if char in vowels)

#  Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c *9/5)+32
print(celsius_to_fahrenheit(0))
