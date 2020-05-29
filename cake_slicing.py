def solution(s):
    n = len(s)
    for i in range(1, n//2+1, 1 if n % 2 == 0 else 2):
        slice = s[:i]
        size = i
        valid = True
        if n % size == 0:
            for j in range(i, n, size):
                if s[j : j + size] != slice:
                    valid = False
                    break
            if valid:
                return n // size
    return 0

print(solution("abcabcabc"))