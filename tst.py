

def problem(n):
    p1 = n ** n
    p2 = 6 * n * n
    p3 = 63 * n
    p4 = 3
    ans = p1 - p2 - p3 + p4
    print(ans)

problem(7)