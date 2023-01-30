from collections import defaultdict
from collections import deque
from heapq import *
from collections import Counter
import bisect


def main():
    t = eval(input())
    for _ in range(t):
        n = eval(input())
        a = input().split()
        a = [int(x) for x in a]
        print(solution(a, n))


def solution(nums, n):
    def counter(num):
        if num % 2:
            return 0
        return 1 + counter(num // 2)

    count = 0
    can_use = []
    for i, num in enumerate(nums):
        if (i + 1) % 2 == 0:
            can_use.append(counter(i + 1))
        count += counter(num)

    if count >= n:
        return 0

    used = 1
    can_use.sort()
    while can_use:
        count += can_use.pop()
        if count >= n:
            return used
        used += 1

    return -1


main()
# import sys
# import threading
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# thread = threading.Thread(target=main)
# thread.start(); thread.join()
