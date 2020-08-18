def solution(x, y):
    if not x.isdigit() or not y.isdigit():
        return "impossible"
    
    x = int(x)
    y = int(y)
    count = 0
    while x >= 1 and y >= 1:
        if x == 1 and y == 1:
            return str(count)

        if min(x, y) == 1:
            return str(count + max(x, y) - 1)

        if x > y:
            factor = x // y
            x -= y * factor
        else:
            factor = y // x
            y -= x * factor

        count += factor
    
    return "impossible"

print(solution('10', '13'))