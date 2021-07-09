n, m, k = map(int, input().split())
nums = input().split()
temp = []
index = []

for i in range(len(nums)):
    nums[i] = int(nums[i])

while len(nums) > 0:
    max_num = max(nums)
    temp.append(max_num)
    index.append(nums.index(max_num))
    nums.remove(max_num)



sum = (temp[0]*k + temp[1])*(m//(k+1))+temp[0]*(m%(k+1))
    
print(n)
print(m)
print(k)
print(sum)
