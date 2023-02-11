from collections import defaultdict
from collections import deque
from heapq import *
from collections import Counter


def inp():
    n, d = input().split()
    ppl = []
    for _ in range(int(n)):
        m, f = input().split()
        ppl.append([int(m), int(f)])

    print(solution(ppl, int(d)))


def solution(ppl, d):
    ppl.sort()
    l = r = 0
    curr = best = 0
    while r < len(ppl):
        while r < len(ppl) and abs(ppl[l][0] - ppl[r][0]) < d:
            curr += ppl[r][1]
            r += 1
        best = max(best, curr)
        curr -= ppl[l][1]
        l += 1
    return best


inp()
