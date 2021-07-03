import random

# range 2 - 10
x = [i for i in range(2,11)]

for i in range(0,94):
    divisor = random.choice(x)
    quotient = random.randint(10, 99)
    dividend = divisor * quotient
    print(f'{dividend} / {divisor} =')
