coins = [500, 100, 50, 10]

n = int(input())
count = 0
temp = 0

while n > 0:
    for i in range(len(coins)):
        if n // coins[i] != 0:
            temp = n // coins[i]
            n = n - coins[i]*temp
            count = count + temp

print(count)