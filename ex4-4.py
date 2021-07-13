size = list(input('size').split())
row = int(size[0])
column = int(size[1])

location = list(input('location').split())
x = int(location[0])
y = int(location[1])
d = int(location[2])

map = list(input() for _ in range(row))

count = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[x, y]]

while x < row and y < column:
    for i in range(4):
        check_x = x + direction[d-i][0]
        check_y = y + direction[d-i][1]

        if map[check_x][y] == "0" and [check_x, y] not in visited:
            x = x + check_x
            visited.append([x, y])
            count += 1
        elif map[x][check_y] == "0" and [x, check_y] not in visited:
            y = y + check_y
            visited.append([x, y])
            count += 1
        
    if map[x][y-1] == "1":
        break
    else:
        y = y - 1
        count += 1
        


print(count)