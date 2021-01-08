t = int(input("").rstrip())


def number_of_zeros_binary(binary):
    b_n = str(binary)
    num_of_zero = 0
    for i in b_n:
        if i == "0":
            num_of_zero += 1
    # len(binary_num) - num_of_zero = number of ones
    return num_of_zero


result = []
for test_case in range(t):
    n, c0, c1, h = input("").split()
    n = int(n)
    c0 = int(c0)
    c1 = int(c1)
    h = int(h)
    binary_num = input("").rstrip()
    total_cost = 0
    if c0 > c1:
        if c0 - c1 > h:
            total_cost += (h * number_of_zeros_binary(binary_num)) + n * c1
        else:
            total_cost += ((number_of_zeros_binary(binary_num) * c0) + ((n-number_of_zeros_binary(binary_num)) * c1))
    elif c1 > c0:
        if c1 - c0 > h:
            total_cost += (h*(n-number_of_zeros_binary(binary_num))) + n * c0
        else:
            total_cost += ((number_of_zeros_binary(binary_num) * c0) + ((n-number_of_zeros_binary(binary_num)) * c1))
    elif c1 == c0:
        total_cost += c0 * n
    result.append(total_cost)


for i in range(t):
    print("{}".format(result[i]))

