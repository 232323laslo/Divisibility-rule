



divv = int(input('enter your divisor: '))

# Divisor (2) The last digit is even (0, 2, 4, 6, or 8)
if divv == 2:
    num2 = int(input('enter your num: '))
    print('True' if num2 % 10 % 2 == 0 else 'False')

# Divisor (3) The sum of the digits must be divisible by 3
if divv == 3:
    num3 = input('enter your num: ')
    total = 0
    for i in range(len(num3)):
        total += int(num3[i])
    print('True' if total % 3 == 0 else 'False')

# Divisor (4) The last two digits form a number that is divisible by 4
if divv == 4:
    num4 = int(input('enter your num: '))
    print('True' if num4 % 100 % 2 == 0 else 'False')

# Divisor (5) The last digit is 0 or 5.
if divv == 5: 
    two_nums = [0, 5]
    num5 = int(input('enter your num: '))
    print('True' if num5 % 10 in two_nums else 'False')

# Divisor (6) It is divisible by 2 and by 3
if divv == 6:
    num3 = input('enter your num: ')
    total = 0
    for i in range(len(num3)):
        total += int(num3[i])
    print('True' if total % 3 == 0 and total % 2 == 0 else 'False')

# Divisor (7) it is divisible by 3 and 2 at the same time.
    