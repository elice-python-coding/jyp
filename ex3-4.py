n, k = map(int, input().split())
count = 0

while n > 3:
    if n == 2:
        print(1)
    elif n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1

print(count)
