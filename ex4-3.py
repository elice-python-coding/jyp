location = input()
count = 0

x_char = location[0]
x = 0
y = int(location[1])
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
field = []
move = [1, 2, -1, -2]

for i in range(len(alphabet)):
        if x_char == alphabet[i]:
            x = i + 1

for i in range(1, 9):
    for j in range(1, 9):
        field.append([i, j])

for i in range(2):
    for j in range(2):
        if [x + move[2*i], y + move[2*j+1]] in field:
            count += 1
        if [x + move[2*i+1], y + move[2*j]] in field:
            count += 1


print(count)
