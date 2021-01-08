t = int(input("").rstrip())

for i in range(t):
    n, m = map(int, input("").rstrip().split())
    bottom = []
    left = []
    count = 0
    xs = input().rstrip().split()
    for i in range(n):
        bottom.append(int(xs[i]))
    ys = input().rstrip().split()
    for i in range(m):
        left.append(int(ys[i]))
    for x in bottom:
        if x in left:
            count += 1
    """for T in range(1, 100):
        for x in range(n):
            for y in range(m):
                if bottom[x] == T and left[y] == T
        bottom = [x+1 for x in bottom]
        left = [y+1 for y in left]
        if (T in bottom) and (T in left):
            count += 1"""
    """for x in bottom:
        for y in left:
            for T in range(1, max(bottom+left)+1):
                if x == T and y == T:
                    count += 1"""
    print(count)
