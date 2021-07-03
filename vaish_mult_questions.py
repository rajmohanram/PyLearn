import random

# range 3 - 16
x = [i for i in range(2,11)]

for i in range(0,94):
    multiplier = random.choice(x)
    multiplicand = random.randint(10, 99)
    print(f'{multiplicand} * {multiplier} =')
