t = int(input("").rstrip())


def divisors(integer):
    integer = int(integer)
    divisor = []
    for num in range(2, integer):
        if n % num == 0:
            divisor.append(num)
    return divisor


steps = []

for test_case in range(t):
    n = input("").rstrip()
    n = int(n)
    count_steps = 0
    """divisor = []
    for num in range(2, n):
        if n % num == 0:
            divisor.append(num)"""
    while n > 1:
        if not divisors(n):
            n = n - 1
            count_steps += 1
        else:
            n = n/max(divisors(n))
            """divisor.pop(-1)"""
            count_steps += 1
    steps.append(count_steps)


for i in range(t):
    print("{}".format(steps[i]))

