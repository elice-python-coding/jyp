n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
max_b = []
min_a = []

# 내장 함수 이용
arr_a.sort()
arr_b.sort()
i = 0

while k > 0:
    arr_a[i] = arr_b[-(i+1)]
    k -= 1
    i += 1

print(sum(arr_a))