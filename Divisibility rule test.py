



divv = 7

# Divisor (2) The last digit is even (0, 2, 4, 6, or 8)
if divv == 2:
    num2 = 345676548
    print('True' if num2 % 10 % 2 == 0 else 'False')

# Divisor (3) The sum of the digits must be divisible by 3
if divv == 3:
    num3 = '123'
    total = 0
    for i in range(len(num3)):
        total += int(num3[i])
    print('True' if total % 3 == 0 else 'False')

# Divisor (4) The last two digits form a number that is divisible by 4
if divv == 4:
    num4 = 3456789876540
    print('True' if num4 % 100 % 2 == 0 else 'False')

# Divisor (5) The last digit is 0 or 5
if divv == 5: 
    two_nums = [0, 5]
    num5 = 45678550
    print('True'if num5 % 10 in two_nums else 'False')

# Divisor (6) It is divisible by 2 and by 3
if divv == 6:
    num6 = '1232345'
    total = 0
    for i in range(len(num6)):
        total += int(num6[i])
    print('True' if total % 3 == 0 and total % 2 == 0 else 'False')

# Divisor (7) it is divisible by 3 and 2 at the same time
if divv == 7:
    num7 = 18046
    total = 0
    list = []

    # If number bigger than 70 we will need to making him smaller
    if num7 > 70:
        # Add numbers to list separately
        for digit in str(num7):
            list.append(int(digit))



    print('True'if num7 % 3 == 0 and num7 % 2 == 0 else 'False')