n = 123321
resultRight = 0
resultLeft = 0
while n > 999:
    number = n % 10
    n = int(n/10)
    resultRight += number

while n > 0:
    number = n % 10
    n = int(n/10)
    resultLeft += number

if resultRight != resultLeft:
    print('no')
else:
    print('yes')    