from collections import defaultdict
from heapq import heapify, heappush


def main():
    for _ in range(eval(input())):
        monsters = eval(input())
        health = [int(x) for x in input().split()]
        strength = [int(x) for x in input().split()]
        print(solution(health, strength, monsters))


def solution(h, s, n):
    m = []
    for i in range(n):
        m.append([h[i], s[i], i])

    new_m = sorted(m, key=lambda x: x[1])

    time = sum(h)
    for hlth, strgth, idx in new_m:
        m[idx][0] = -1
        if idx > 0:
            curr = idx - 1
            while curr >= 0 and m[curr][0] == -1:
                curr -= 1
            if curr >= 0:
                time += strgth
        if idx < len(m) - 1:
            curr = idx + 1
            while curr < len(m) and m[curr][0] == -1:
                curr += 1
            if curr < len(m):
                time += strgth

    return time


main()
