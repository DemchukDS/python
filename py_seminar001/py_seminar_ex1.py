n = int(input("Enter the numbers of kilometers, thet the auto trevels per day: "))
m = int(input("Enter the numbers of kilometers, thet the auto trevels: "))

# if m % n == 0:
#     result = int(m / n)
#     if result == 1:
#         print(f"Auto will be in the way {result} day!")
#     else:
#         print(f"Auto will be in the way {result} days!")
# else:
#     result = int(m / n + 1)
#     print(f"Auto will be in the way {result} days!")
    
#result = (m + n - 1) // n 
result = -(-m // n)
print(result)