def solution(l):
    count = [0] * len(l)
    out = 0
    
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                count[i] += 1
                out += count[j]
    return out

print(solution([1, 2, 3, 4, 5, 6]))
