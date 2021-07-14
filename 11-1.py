n = int(input())
member = list(map(int, input().split()))

count = 0
rest = len(member)
member.sort(reverse=True)

while rest > 0:
    rest = len(member) - max(member)
    del member[:max(member)]
    count += 1

print(count)
# test case 4 / 3 2 2 2 failed
# Do retry 