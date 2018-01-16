data = ['A', 'B', 'C', 'D', 'E']
combination = 3
l = [0,1,2]
length = 5

x = []

# abc abd abe acd ace ade

for i in range(0, length, 1):
    if i > 0 :
        if l[2] < length-1:
            l[2] = l[2] + 1
        else:
            l[1] = l[1] + 1
            l[2] = l[1] + 1
    print l
    x.append(data[l[0]] + data[l[1]] + data[l[2]])

print x