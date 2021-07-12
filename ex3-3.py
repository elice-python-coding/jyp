#-*- coding:utf-8 -*-

n, m = map(int, input().split())

# 두번째 줄 데이터를 (2차원) 리스트로 받는 법을 몰라서 답지 참고함
# 입력 데이터를 공백 기준으로 각각의 숫자로 나누기

result = 0


for i in range(n):
    data = list(map(int, input().split())) # 입력데이터를 숫자로 나누고, 리스트로 받기
    
    min_value = 1000000
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)


# 입력 에러가 납니다~ 

# Traceback (most recent call last):
#  File "ex3-3.py", line 3, in <module>
#    n, m = map(int, input().split())
#  File "<string>", line 1
#    3 3
#      ^
# SyntaxError: unexpected EOF while parsing

