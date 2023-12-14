n = 100
res = 0
while n > 0:
    number = n % 10
    n = int(n/10)
    res += number
print(res)