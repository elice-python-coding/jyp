n = input()
if len(n) // 2 != 0:
    print("ERROR")
else:
    middle = (len(n) // 2)

    left = [int(i) for i in n[:middle]]
    right = [int(i) for i in n[middle:]]

    if sum(left) == sum(right):
        print("LUCKY")
    else:
        print("READY")