hour = int(input()) 

hour_count = 60*60
min_count = 0
sec_count = 0

for i in range(min):
    if (i%10) == 3 or (i//10) == 3:
        min_count += 1
        sec_count = min_count

# min_count = 15
#print(min_count)

result = hour_count + ((min_count * 60) + ((60-min_count) * sec_count))*hour
print(result)