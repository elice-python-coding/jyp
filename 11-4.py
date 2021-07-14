num = int(input())
coins = list(map(int, input().split()))
memo = []
final_memo = []
def combinations(arr, n): 
    result =[] 
    if n == 0: 
        return [[]] 
    
    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in combinations(rest_arr, n-1): 
            result.append([elem]+C) 
    
    return result

for i in range(num):
    memo.append(combinations(coins, i+1))

for i in range(num):
    for j in range(len(memo[i])):
        sum_elem = sum(memo[i][j])
        final_memo.append(sum_elem)

print(memo)
print(final_memo)


for i in range(1,100000):
    if i not in final_memo:
        print(i)
        break



    