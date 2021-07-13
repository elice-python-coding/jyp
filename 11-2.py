s = list(map(int, input()))

result = 0

for i in range(len(s)):
    if i == 0:
        result = s[i]
    elif i > 0 and s[i] !=0 and s[i-1] == 0:
        result += s[i]
    elif i > 0 and s[i] != 0 and s[i-1] != 0:
        result *= s[i]
    
print(result)