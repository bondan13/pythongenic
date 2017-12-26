data = [9, 3, 9, 3, 9, 7, 9]
val = {}

for i in data:
    if val.get(i): del val[i]
    else: val[i] = True

for key in val:
    print key
    break