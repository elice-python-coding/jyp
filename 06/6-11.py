from operator import itemgetter, attrgetter, methodcaller
# 데이터를 숫자, 문자 동시에 따로 받을 수 없나?
# 입력 방법 1
N = int(input())
data = list(input().split() for _ in range(N))

for i in range(N):
    data[i][1] = int(data[i][1])

# 입력 방법 2
# N = int(input())
# data = []
# for i in range(N):
#    name, grade = input().split()
#    grade = int(grade)
#    data.append([name, int(grade)])

# 파이썬 내장 라이브러리, 키를 이용한 정렬
# result = sorted(data, key=itemgetter(1))
# for i in range(len(result)):
#    print(result[i][0])

# refactoring
for name in sorted(data, key=itemgetter(1)): 
    print(name[0])
# 참고: https://fenderist.tistory.com/158 [Devman]