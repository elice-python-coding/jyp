import time
start = time.time()  # 시작 시간 저장

# N = int(input())
# nums = list(int(input()) for _ in range(N))
# print(nums)
# for time test
nums = [15, 27, 12]
# 1) 내장 함수 이용
# nums.sort(reverse=True)
# nums = sorted(nums, reverse=True)
# nums.reverse()
# print(nums)

# 2) 계수 정렬 사용 - 역순이 아님;;
count = [0] * (max(nums)+1) # 리스트 선언, 모든 값은 0으로 초기화
for i in range(len(nums)):
      count[nums[i]] += 1 # 각 데이터의 인덱스 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
     for j in range(count[i]):
          print(i, end=' ') # 띄어쓰기로 값을 구분, 각 값의 등장 횟수만큼 인덱스 출력

# 3) 교재 풀이
# N = 3
# result = [] 
# for i in range(N):
    # nums.append(int(input()))
#    result.append(nums[i])
#result.sort(reverse=True)
#for i in range(N):
#    print(result[i],end=" ")

# 시간 계산
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간