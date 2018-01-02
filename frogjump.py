X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
A= [2,2,2,2,2,2]
r = -1
z = len(A)
dic = {}

if z < X: print r

index = 0
for i in A:
    if i <= X and not dic.get(i):
        dic[i] = index

    if len(dic) == X:
        r = i
        break
    index += 1

print r