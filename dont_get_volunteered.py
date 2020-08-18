"""
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
"""
def getBoardPos(pt):
    return ((pt//8, pt%8))

def isValid(pos, i, j):
    return max(pos[0]+j, pos[1]+i) < 8 and min(pos[0]+j, pos[1]+i) >= 0

def solution(src, dest):
    dest = getBoardPos(dest)
    visited = []
    q = []
    q.append((getBoardPos(src), 0))
    
    while len(q) > 0:
        curr = q.pop(0)
        if curr[0] == dest:
            return curr[1]

        if curr[0] in visited:
            continue

        pos = curr[0]
        visited.append(pos)
        
        for i in [-1,1]:
            for j in [-2,2]:
                if isValid(pos, i, j):
                    q.append(((pos[0]+j, pos[1]+i), curr[1]+1))

                if isValid(pos, j, i):
                    q.append(((pos[0]+i, pos[1]+j), curr[1]+1))

    return -1

print(solution(19,36))