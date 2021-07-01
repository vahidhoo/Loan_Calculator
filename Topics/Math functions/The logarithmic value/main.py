import math

num_1 = abs(int(input()))
num_2 = int(input())

if num_2 > 1:
    log = round(math.log(num_1, num_2), 2)
else:
    log = round(math.log(num_1), 2)

print(log)
