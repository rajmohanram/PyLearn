import random

for i in range(0,94):
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    num1 = max(x, y)
    num2 = min(x,y)
    print(f'{num1} + {num2} =')
