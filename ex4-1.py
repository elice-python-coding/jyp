x = 1
y = 1

n = int(input())
data = list(input().split())

for i in range (len(data)):
    if y < n and data[i] == "R":
        y += 1
    elif y > 1 and data[i] == "L":
        y -= 1
    elif x > 1 and data[i] == "U":
        x -= 1
    elif x < n and data[i] == "D":
        x += 1

print(x, y)
    