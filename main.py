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

#6) original_list = [1, 2, 3, 4, 5]
# squared_list = list(map(lambda x: x ** 2, original_list))
# print(squared_list)


