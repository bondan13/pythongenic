data = [18, 2, 5, 3, 4, 6, 11, 5, 1]

length = len(data) - 1

for i in range(length):
    for j in range(length):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
        print data
    length -= 1