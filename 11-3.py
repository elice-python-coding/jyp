s = list(map(int, input()))
cluster = []

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        pass
    else:
        cluster.append(i)

#print(cluster)
print((len(cluster)+1)//2)
