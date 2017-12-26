data = [1212, 212, 31, 411, 422, 53, 64, 755, 89]
l_data = len(data)
rotation = 200
rotation = rotation % l_data
print rotation
data_left = []
data_right = []
r_data = l_data - (rotation + 1)

index = 0
for i in data:
    if index > r_data: data_left.append(data[index])
    else: data_right.append(data[index])
    index += 1

print data_left + data_right