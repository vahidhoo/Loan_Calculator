import math

degree = int(input())

radians = math.radians(degree)

cotangent = round(math.cos(radians) / math.sin(radians), 10)

print(cotangent)
