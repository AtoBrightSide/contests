from collections import deque
from heapq import *

def solution(ppl):
    max_heap = [[-ppl[i], i + 1] for i in range(len(ppl))]
    heapify(max_heap)

    talks = []
    while max_heap:
        soc1, per1 = heappop(max_heap)
        if max_heap:
            soc2, per2 = heappop(max_heap)
        if min(abs(soc1), abs(soc2)) > 0:
            talks.append([per1, per2])

        if abs(soc1):
            heappush(max_heap, [soc1 + 1, per1])
        if abs(soc2):
            heappush(max_heap, [soc2 + 1, per2])
    
    print(len(talks))
    for talk in talks:
        print(*talk)
    
if __name__ == "__main__":
    for _ in range(eval(input())):
        eval(input())
        ppl = [int(x) for x in input().split()]
        solution(ppl)
