data = [2, 3, 1, 5]
dict = {}

for i in data:
    dict[i] = i

index = 1
for x in dict:
    if not dict.get(index):
        print index
        break
    index += 1