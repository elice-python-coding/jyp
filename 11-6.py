food_times = list(map(int, input().split()))
k = int(input())


def solution(food_times, k):
    food_num = -1
    check = 0

    while k > 0:
        for i in range(len(food_times)):
            check = i // len(food_times)
            if food_times[check] != 0:
                food_times[check] = food_times[check] - 1
                k -= 1
            else:
                k -= 1
    
    food_num = (i+1) // len(food_times)

    return food_num


print(solution(food_times, k))