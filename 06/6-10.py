N = int(input())
nums = list(int(input()) for _ in range(N))
# 1) 내장 함수 이용
# print(nums.sort(reverse=True))
# print(sorted(nums, reverse=True))
# print(nums.reverse())

# 2) 계수 정렬 사용
count = [0] * (max(nums)+1) # 리스트 선언, 모든 값은 0으로 초기화
for i in range(len(nums)):
    count[nums[i]] += 1 # 각 데이터의 인덱스 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기로 값을 구분, 각 값의 등장 횟수만큼 인덱스 출력

