x = 83744
highscore = 0
score = 0
binary = ''
has1 = False


while True:
    c = x % 2
    x = x / 2
    if c == 0 and has1:score += 1
    elif c == 1:
        has1 = True
        if score > highscore: highscore = score
        score = 0
    binary = str(c) + binary
    if x == 0: break

print highscore
print binary