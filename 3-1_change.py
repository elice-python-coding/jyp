price = int(input())
change = 1000 - price
temp = 0
coin = [500, 100, 50, 10, 5, 1]

for i in range(len(coin)):
        temp = temp + (change//coin[i])
        change = change - coin[i]*(change//coin[i])


print(temp)