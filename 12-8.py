S = input()
result = [S[i] for i in range(len(S))]
result.sort()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = 0

for i in range(len(S)):
    if result[i] in num:
        count += 1

nums = result[:count]
chars = result[count:]

print(''.join(chars)+''.join(nums))