A = [-1000, 1000]
# A = [-3, -1, -2, -4, -3]
# A = [3, 1, 2, 4, 3]

length = len(A)
count = 0

for i in A:
    count += i

x = count // 2
if x < 0: x += 1


count2 = 0
count3 = 0
index = 0
for i in A:
    lt = True if x > 0 and count2 > 0 else False

    if index == 0: count2 += i
    elif lt is True and count2 < x and (index + 1) < length: count2 += i
    elif lt is False and count2 > x and (index + 1) < length: count2 += i
    else: count3 += i
    index += 1

print abs(count2-count3)