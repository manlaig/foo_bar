"""
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
"""

INT_MAX = 2147000000

def get(map, point):
    return map[point[0]][point[1]];

def inBounds(point, map):
    return point[0] >= 0 and point[0] < len(map) and point[1] < len(map[0]) and point[1] >= 0

def helper(curr, map, visited, wall_erased=False, length=1):

    if curr[0] == len(map)-1 and curr[1] == len(map[0])-1:
        return length

    # to avoid cycling
    if (curr, wall_erased) in visited and length >= visited[(curr, wall_erased)]:
        return INT_MAX

    visited[(curr, wall_erased)] = length

    left = (curr[0], curr[1]-1)
    right = (curr[0], curr[1]+1)
    up = (curr[0]-1, curr[1])
    down = (curr[0]+1, curr[1])

    leftLen = INT_MAX
    if inBounds(left, map):
        if get(map, left) == 1 and not wall_erased:
            leftLen = helper(left, map, visited, True, length+1)
        elif get(map, left) == 0:
            leftLen = helper(left, map, visited, wall_erased, length+1)

    rightLen = INT_MAX
    if inBounds(right, map):
        if get(map, right) == 1 and not wall_erased:
            rightLen = helper(right, map, visited, True, length+1)
        elif get(map, right) == 0:
            rightLen = helper(right, map, visited, wall_erased, length+1)

    upLen = INT_MAX
    if inBounds(up, map):
        if get(map, up) and not wall_erased:
            upLen = helper(up, map, visited, True, length+1)
        elif get(map, up) == 0:
            upLen = helper(up, map, visited, wall_erased, length+1)

    downLen = INT_MAX
    if inBounds(down, map):
        if get(map, down) == 1 and not wall_erased:
            downLen = helper(down, map, visited, True, length+1)
        elif get(map, down) == 0:
            downLen = helper(down, map, visited, wall_erased, length+1)

    return min(upLen, downLen, leftLen, rightLen)


def solution(map):
    if len(map) == 0 or len(map[0]) == 0:
        return 0
    visited = {}
    return helper((0,0), map, visited)

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))