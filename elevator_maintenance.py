from functools import cmp_to_key

def sort_version(v1, v2):
    v1 = v1.split(".")
    v2 = v2.split(".")
    for i in range(min(len(v1), len(v2))):
        if int(v1[i]) > int(v2[i]):
            return True
        elif int(v1[i]) < int(v2[i]):
            return False
    return len(v1) > len(v2)

def make(func):
    def compare(x, y):
        return 1 if func(x,y) else -1
    return compare

def solution(l):
    return sorted(l, key=cmp_to_key(make(sort_version)))
