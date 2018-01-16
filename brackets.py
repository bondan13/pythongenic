def solution(S):
    couple = {'{':'}', '[': ']', '(': ')'}
    single = []

    for i in S:
        if couple.get(i): single.append(i)
        else:
            a = len(single)
            if not a: return 0
            if couple.get(single[a-1]) == i: del single[a-1]
            else: return 0

    if len(single): return 0
    return 1