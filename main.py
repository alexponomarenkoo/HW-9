 ####task 1
 # Користувач вводить із клавіатури номер дня тижня (1-7).
 # Необхідно вивести на екран назви дня тижня.
 # Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.\


# a = int(input("Enter day number: "))
# if a == 1:
#    print("Monday")
# elif a == 2:
#    print("Tuesday")
# elif a == 3:
#    print("Wednesday")
# elif a == 4:
#    print("Thursday")
# elif a == 5:
#    print("Friday")
# elif a == 6:
#    print("Saturday")
# elif a == 7:
#    print("Sunday")

####task 2
# Користувач вводить два числа.
#  Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання


# a = int(input("First number: "))
# b = int(input("Second number: "))
# if a != b and a < b:
#    print(str(a) + " " + str(b))
# elif a != b and a > b:
#    print(str(b) + " " + str(a))
# else:
#    print("a = b")
####task 3
# Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат


# while True:
#     s = input("Select action (+, -, *, /): ")
#
#     if s in ('+', '-', '*', '/'):
#         a = float(input("a = "))
#         b = float(input("b = "))
#         if s == '+':
#             print("%.2f" % (a + b))
#         elif s == '-':
#             print("%.2f" % (a - b))
#         elif s == '*':
#             print("%.2f" % (a * b))
#         elif s == '/':
#             if b != 0:
#                 print("%.2f" % (a / b))
#             else:
#                 print("Impossible to divide by 0!")
#     else:
#         print("Invalid operation!")
