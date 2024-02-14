# # 2)
# # def generate_screen():
# #     print("-" * 39)
# #     print("|" + " " *10 + "Roberto".ljust(28) + "|")
# #     print("|".ljust(39) + "|")
# #     print("|" + " " * 10 + "5786".ljust(28) + "|")
# #     print("|".ljust(39) + "|")
# #     print("|" + " " * 10 + "UNIFEI".ljust(28) + "|")
# #     print("-" * 39)
# # print(generate_screen())
#
#
#
# #  from math import pi
# # def circumference_of_circle(x: float) -> float:
# #     return 2 * pi * x
# # x = float(input('Enter the radius of the circle: '))
# # if x < 0 or x >= 10:
# #     print('Invalid input. Radius must be between 0 and 10.')
# # else:
# #     print(circumference_of_circle(x))
#
#
# #4) f1 = float(input("Enter the GDP fluctuation for the first year: "))
# # f2 = float(input("Enter the GDP fluctuation for the second year: "))
# # def calculate_total_gdp_fluctuation(f1, f2):
# #     return ((f1 + 100)/100) * ((f2+100)/100) - 1
# # print("The GDP fluctuation is:", calculate_total_gdp_fluctuation(f1,f2) )
#
#
#
#
# #5) citations = [0,1,3,5,6,]
# # def h_index(citations):
# #     n = len(citations)
# #     left, right = 0, n - 1
# #     while left <= right:
# #         mid = (left + right) // 2
# #         if citations[mid] == n - mid:
# #             return n - mid
# #         elif citations[mid] < n - mid:
# #             left = mid + 1
# #         else:
# #             right = mid - 1
# #     return n - left
# # print(h_index(citations))
#
#
#
#
#
# #6) game = 'yes'
# # while game == 'yes':
# #
# #    num = str(int(input('enter secret numbers:')))
# #
# #
# #
# #    attempt = True
# #
# #    while attempt:
# #
# #        player_num = input("your guess: ")
# #
# #        bulls = 0
# #
# #        cows = 0
# #
# #        for i in range(4):
# #
# #            if num[i] == player_num[i]:
# #
# #                bulls += 1
# #
# #            elif player_num[i] in num:
# #
# #                cows += 1
# #
# #        if bulls == 4:
# #
# #            print("4A!YOU WIN!")
# #
# #            game = input('Do you want restart game?(yes or no): ')
# #
# #            attempt = False
# #
# #        else:
# #
# #            print(f'{bulls}A, {cows} B')
#
#
#
#
# #7) import math
# # def numSquares(n):
# #
# #     dp = [0] * (n + 1)
# #
# #     for i in range(1, n + 1):
# #
# #         dp[i] = i
# #
# #
# #         for j in range(1, int(math.sqrt(i)) + 1):
# #
# #             dp[i] = min(dp[i], 1 + dp[i - j*j])
# #
# #     return dp[n]
# # print(numSquares(int(input('enter number'))))
#
#
#
# #8) from collections import Counter
# # def checkInclusion(s1, s2):
# #     len_s1 = len(s1)
# #     len_s2 = len(s2)
# #
# #     if len_s1 > len_s2:
# #         return False
# #
# #     freq_s1 = Counter(s1)
# #     freq_window = Counter(s2[:len_s1])
# #
# #     if freq_s1 == freq_window:
# #         return True
# #
# #     for i in range(len_s1, len_s2):
# #         char_out = s2[i - len_s1]
# #         if freq_window[char_out] == 1:
# #             del freq_window[char_out]
# #         else:
# #             freq_window[char_out] -= 1
# #
# #         char_in = s2[i]
# #         freq_window[char_in] += 1
# #
# #         if freq_s1 == freq_window:
# #             return True
# #
# #     return False
# #
# # s1 = "ab"
# # s2 = "eidbaooo"
# # result = checkInclusion(s1, s2)
# # print(result)
#
#
# # my_list = [1, 2, 3, 4, 5]
# # new_list = list(map(lambda x: x**2, my_list))
# # print(new_list)
#
# # my_list = [1, 2, 3, 4, 5]
# # new_list = list(filter(lambda x: (x%2==0),my_list))
# # print(new_list)
#
# # strings = ['aitu','enu','kbtu']
# # upper_cased = list(map(lambda string: string.upper(), strings))
# # print(upper_cased)
#
# # strings = ['aitu','enu', 'python', 'programming', 'code']
# # filtered_strings = list(filter(lambda x: len(x) > 5, strings))
# # print(filtered_strings)
#
# # fahrenheit_temperatures = [32, 68, 86, 104]
# # celsius_temperatures = list(map(lambda x: (5/9) * (x - 32), fahrenheit_temperatures))
# # print(celsius_temperatures)
#
# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
# # numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # prime_numbers = list(filter(lambda x: is_prime(x), numbers))
# # print(prime_numbers)
#
#
# # list1 = [1, 2, 3, 4, 5]
# # list2 = [6, 7, 8, 9, 10]
# # result = list(map(lambda x, y: x**2 + y**2, list1, list2))
# # print(result)
#
# # strings = ['radar', 'hello', 'level', 'madam', 'deified']
# # palindromes = list(filter(lambda x: x == x[::-1], strings))
# # print(palindromes)
#
# # strings = ['hello', 'world', 'python', 'programming', 'code']
# # lengths = list(map(lambda x: len(x), strings))
# # print(lengths)
#
# # numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# # positive_numbers = list(filter(lambda x: x > 0, numbers))
# # print(positive_numbers)
#
# # def generate_fibonacci(n):
# #     fib_sequence = [0, 1]
# #     if n <= 2:
# #         return fib_sequence[:n]
# #     else:
# #         fib_sequence.extend(map(lambda x, y: x + y, fib_sequence[-2:], fib_sequence[-1:] + [0] * (n - 2)))
# #         return fib_sequence
# # n = 10
# # print(generate_fibonacci(n))
#
# # Given a list of strings, use filter and lambda to create a new list
# # containing only pairs of anagrams
# # strings = ['listen', 'enlist', 'silent', 'hello', 'world', 'python']
# # anagrams = list(filter(lambda x: sorted(x[0]) == sorted(x[1]), [(x, y) for x in strings for y in strings if x != y]))
# # print(anagrams)
#
# #
# # .Given a list of strings, use filter and lambda to create a new list containing
# # only strings that consist entirely of consonants. (2 points)
# # def contains_only_consonants(string):
# #     vowels = 'aeiouAEIOU'
# #     return all(char not in vowels for char in string)
# # string_list = ["hello", "world", "python", "programming", "Yerassyl", "crypt"]
# # consonant_strings = list(filter(lambda x: contains_only_consonants(x), string_list))
# # print(consonant_strings)
#
#
#
#
# # .Given a list of numbers, use map and lambda to create a new list where
# # each element is the rolling average of the last three elements in the original
# # list.
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # rolling_average = list(map(lambda i: sum(numbers[i-2:i+1])/3, range(2, len(numbers))))
# # print(rolling_average)
#
# # Given a list of integers, use filter and lambda to create a new list
# # containing only perfect square numbers.
# # import math
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,16]
# # perfect_squares = list(filter(lambda x: math.isqrt(x)**2 == x, numbers))
# # print(perfect_squares)
#
#
# # Given an integer n, return true if it is a power of four. Otherwise, return false.
# # An integer n is a power of four, if there exists an integer x such that n == 4x
# # .
# # def is_power_of_four(n):
# #     if n == 1:
# #         return True
# #     if n < 4 or n % 4 != 0:
# #         return False
# #     return is_power_of_four(n // 4)
# # print(is_power_of_four(16))
# # print(is_power_of_four(5))
#

#
# 2)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def mergeTwoLists(list1, list2):
#     dummy = current = ListNode()
#
#     while list1 and list2:
#         current.next, list1, list2 = (list1, list1.next, list2) if list1.val < list2.val else (list2, list1, list2.next)
#         current = current.next
#
#     current.next = list1 or list2
#
#     return dummy.next
#
#
# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
#
# list1_values = list(map(int, input().split()))
# list2_values = list(map(int, input().split()))
#
# list1 = ListNode()
# current = list1
# for value in list1_values:
#     current.next = ListNode(value)
#     current = current.next
# list1 = list1.next
#
# list2 = ListNode()
# current = list2
# for value in list2_values:
#     current.next = ListNode(value)
#     current = current.next
# list2 = list2.next
#
# merged_list = mergeTwoLists(list1, list2)
#
# print("Merged Linked List:")
# printLinkedList(merged_list)
#
# 3)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def removeElements(head, val):
#     dummy = ListNode(0)
#     dummy.next = head
#     current = dummy
#
#     while current.next:
#         if current.next.val == val:
#             current.next = current.next.next
#         else:
#             current = current.next
#
#     return dummy.next
#
#
# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
#
# list_values = list(map(int, input().split()))
# val_to_remove = int(input())
#
# head = ListNode()
# current = head
# for value in list_values:
#     current.next = ListNode(value)
#     current = current.next
# head = head.next
#
# new_head = removeElements(head, val_to_remove)
#
# print("Modified Linked List:")
# printLinkedList(new_head)
#
# 4)
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#
#     fib = [0] * (n + 1)
#     fib[1] = 1
#
#     for i in range(2, n + 1):
#         fib[i] = fib[i - 1] + fib[i - 2]
#
#     return fib[n]
#
#
# n = int(input())
#
# result = fibonacci(n)
# print(f"F{result}")
#
# 5)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def isPalindrome(head):
#     values = []
#
#     while head:
#         values.append(head.val)
#         head = head.next
#
#     return values == values[::-1]
#
#
# def createLinkedList(values):
#     dummy = current = ListNode()
#     for value in values:
#         current.next = ListNode(value)
#         current = current.next
#     return dummy.next
#
#
# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
#
# values = list(map(int, input().split()))
#
# head = createLinkedList(values)
#
# result = isPalindrome(head)
#
# print(result)
# 6)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def addTwoNumbers(l1, l2):
#     dummy = current = ListNode()
#     carry = 0
#
#     while l1 or l2 or carry:
#         digit_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
#
#         carry = digit_sum // 10
#
#         current.next = ListNode(digit_sum % 10)
#
#         current = current.next
#         l1 = l1.next if l1 else None
#         l2 = l2.next if l2 else None
#
#     return dummy.next
#
#
# def createLinkedList(values):
#     dummy = current = ListNode()
#     for value in values:
#         current.next = ListNode(value)
#         current = current.next
#     return dummy.next
#
#
# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
#
# values1 = list(map(int, input().split()))
# values2 = list(map(int, input().split()))
#
# l1 = createLinkedList(values1)
# l2 = createLinkedList(values2)
#
# result = addTwoNumbers(l1, l2)
# print()
# printLinkedList(result)
#
# 7)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def swapPairs(head):
#     dummy = ListNode(0)
#     dummy.next = head
#     current = dummy
#
#     while current.next and current.next.next:
#         first_node = current.next
#         second_node = current.next.next
#
#         first_node.next = second_node.next
#         second_node.next = first_node
#         current.next = second_node
#
#         current = current.next.next
#
#     return dummy.next
#
#
# def createLinkedList(values):
#     dummy = current = ListNode()
#     for value in values:
#         current.next = ListNode(value)
#         current = current.next
#     return dummy.next
#
#
# def printLinkedList(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
#
# values = list(map(int, input().split()))
#
# head = createLinkedList(values)
#
# result = swapPairs(head)
# print()
# printLinkedList(result)
#
# 8)
#
# def lastRemaining(n):
#     arr = list(range(1, n + 1))
#     left_to_right = True
#
#     while len(arr) > 1:
#         if left_to_right:
#             arr = arr[1::2]
#         else:
#             arr = arr[:-1:2]
#         left_to_right = not left_to_right
#
#     return arr[0]
#
#
# n = int(input())
#
# result = lastRemaining(n)
# print(f"{result}")
#
# 9)
#
# def countGoodNumbers(n):
#     MOD = 10 ** 9 + 7
#
#     def power(x, y):
#         result = 1
#         x = x % MOD
#         while y > 0:
#             if y % 2 == 1:
#                 result = (result * x) % MOD
#             y = y // 2
#             x = (x * x) % MOD
#         return result
#
#     even_count = power(5, (n + 1) // 2)
#     odd_count = power(4, n // 2)
#
#     total_count = (even_count * odd_count) % MOD
#
#     return total_count
#
#
# n = int(input())
#
# result = countGoodNumbers(n)
# print(f"{result}")
#
# 10)
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def allPossibleFBT(n):
#     if n % 2 == 0:
#         return []
#
#     memo = {}
#
#     def generateTrees(n):
#         if n in memo:
#             return memo[n]
#
#         if n == 1:
#             return [TreeNode(0)]
#
#         result = []
#         for left_nodes in range(1, n, 2):
#             for left_tree in generateTrees(left_nodes):
#                 for right_tree in generateTrees(n - 1 - left_nodes):
#                     root = TreeNode(0)
#                     root.left = left_tree
#                     root.right = right_tree
#                     result.append(root)
#
#         memo[n] = result
#         return result
#
#     return generateTrees(n)
#
#
# n = int(input())
#
# result = allPossibleFBT(n)
# print("List of all possible full binary trees with", n, "nodes:")
# for tree in result:
#     print(tree)
#
#
