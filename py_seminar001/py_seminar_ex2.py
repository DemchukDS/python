a = 21
b = 21
c = 21
# sumOfStudents = a + b + c

# if a % 2 != 1 and b % 2 != 1 and c % 2 != 1:
#     print(f"The minimal number of tables are {int((a+b+c) / 2)}!")
# elif a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
#     if a % 2 == 1:
#         sumOfStudents += 1
#         if b % 2 == 1:
#             sumOfStudents += 1
#         elif c % 2 == 1:
#             sumOfStudents += 1
#     elif b % 2 == 1:
#         sumOfStudents += 1
#         if c % 2 == 1:
#             sumOfStudents += 1
#     elif c % 2 == 1:
#         sumOfStudents += 1

# if sumOfStudents % 2 == 1:
#     print(int(sumOfStudents / 2 + 1))
# else:
#     print(int(sumOfStudents / 2))

print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)