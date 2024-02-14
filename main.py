# 2)
# def generate_screen():
#     print("-" * 39)
#     print("|" + " " *10 + "Roberto".ljust(28) + "|")
#     print("|".ljust(39) + "|")
#     print("|" + " " * 10 + "5786".ljust(28) + "|")
#     print("|".ljust(39) + "|")
#     print("|" + " " * 10 + "UNIFEI".ljust(28) + "|")
#     print("-" * 39)
# print(generate_screen())



#3) from math import pi
# def circumference_of_circle(x: float) -> float:
#     return 2 * pi * x
# x = float(input('Enter the radius of the circle: '))
# if x < 0 or x >= 10:
#     print('Invalid input. Radius must be between 0 and 10.')
# else:
#     print(circumference_of_circle(x))


#4) f1 = float(input("Enter the GDP fluctuation for the first year: "))
# f2 = float(input("Enter the GDP fluctuation for the second year: "))
# def calculate_total_gdp_fluctuation(f1, f2):
#     return ((f1 + 100)/100) * ((f2+100)/100) - 1
# print("The GDP fluctuation is:", calculate_total_gdp_fluctuation(f1,f2) )




#5) citations = [0,1,3,5,6,]
# def h_index(citations):
#     n = len(citations)
#     left, right = 0, n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if citations[mid] == n - mid:
#             return n - mid
#         elif citations[mid] < n - mid:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return n - left
# print(h_index(citations))





#6) game = 'yes'
# while game == 'yes':
#
#    num = str(int(input('enter secret numbers:')))
#
#
#
#    attempt = True
#
#    while attempt:
#
#        player_num = input("your guess: ")
#
#        bulls = 0
#
#        cows = 0
#
#        for i in range(4):
#
#            if num[i] == player_num[i]:
#
#                bulls += 1
#
#            elif player_num[i] in num:
#
#                cows += 1
#
#        if bulls == 4:
#
#            print("4A!YOU WIN!")
#
#            game = input('Do you want restart game?(yes or no): ')
#
#            attempt = False
#
#        else:
#
#            print(f'{bulls}A, {cows} B')




#7) import math
# def numSquares(n):
#
#     dp = [0] * (n + 1)
#
#     for i in range(1, n + 1):
#
#         dp[i] = i
#
#
#         for j in range(1, int(math.sqrt(i)) + 1):
#
#             dp[i] = min(dp[i], 1 + dp[i - j*j])
#
#     return dp[n]
# print(numSquares(int(input('enter number'))))



#8) from collections import Counter
# def checkInclusion(s1, s2):
#     len_s1 = len(s1)
#     len_s2 = len(s2)
#
#     if len_s1 > len_s2:
#         return False
#
#     freq_s1 = Counter(s1)
#     freq_window = Counter(s2[:len_s1])
#
#     if freq_s1 == freq_window:
#         return True
#
#     for i in range(len_s1, len_s2):
#         char_out = s2[i - len_s1]
#         if freq_window[char_out] == 1:
#             del freq_window[char_out]
#         else:
#             freq_window[char_out] -= 1
#
#         char_in = s2[i]
#         freq_window[char_in] += 1
#
#         if freq_s1 == freq_window:
#             return True
#
#     return False
#
# s1 = "ab"
# s2 = "eidbaooo"
# result = checkInclusion(s1, s2)
# print(result)


# my_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x**2, my_list))
# print(new_list)

# my_list = [1, 2, 3, 4, 5]
# new_list = list(filter(lambda x: (x%2==0),my_list))
# print(new_list)

# strings = ['aitu','enu','kbtu']
# upper_cased = list(map(lambda string: string.upper(), strings))
# print(upper_cased)

# strings = ['aitu','enu', 'python', 'programming', 'code']
# filtered_strings = list(filter(lambda x: len(x) > 5, strings))
# print(filtered_strings)

# fahrenheit_temperatures = [32, 68, 86, 104]
# celsius_temperatures = list(map(lambda x: (5/9) * (x - 32), fahrenheit_temperatures))
# print(celsius_temperatures)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# prime_numbers = list(filter(lambda x: is_prime(x), numbers))
# print(prime_numbers)


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# result = list(map(lambda x, y: x**2 + y**2, list1, list2))
# print(result)

# strings = ['radar', 'hello', 'level', 'madam', 'deified']
# palindromes = list(filter(lambda x: x == x[::-1], strings))
# print(palindromes)

# strings = ['hello', 'world', 'python', 'programming', 'code']
# lengths = list(map(lambda x: len(x), strings))
# print(lengths)

# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# print(positive_numbers)

# def generate_fibonacci(n):
#     fib_sequence = [0, 1]
#     if n <= 2:
#         return fib_sequence[:n]
#     else:
#         fib_sequence.extend(map(lambda x, y: x + y, fib_sequence[-2:], fib_sequence[-1:] + [0] * (n - 2)))
#         return fib_sequence
# n = 10
# print(generate_fibonacci(n))

# Given a list of strings, use filter and lambda to create a new list
# containing only pairs of anagrams
# strings = ['listen', 'enlist', 'silent', 'hello', 'world', 'python']
# anagrams = list(filter(lambda x: sorted(x[0]) == sorted(x[1]), [(x, y) for x in strings for y in strings if x != y]))
# print(anagrams)

#
# .Given a list of strings, use filter and lambda to create a new list containing
# only strings that consist entirely of consonants. (2 points)
# def contains_only_consonants(string):
#     vowels = 'aeiouAEIOU'
#     return all(char not in vowels for char in string)
# string_list = ["hello", "world", "python", "programming", "Yerassyl", "crypt"]
# consonant_strings = list(filter(lambda x: contains_only_consonants(x), string_list))
# print(consonant_strings)




# .Given a list of numbers, use map and lambda to create a new list where
# each element is the rolling average of the last three elements in the original
# list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# rolling_average = list(map(lambda i: sum(numbers[i-2:i+1])/3, range(2, len(numbers))))
# print(rolling_average)

# Given a list of integers, use filter and lambda to create a new list
# containing only perfect square numbers.
# import math
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,16]
# perfect_squares = list(filter(lambda x: math.isqrt(x)**2 == x, numbers))
# print(perfect_squares)