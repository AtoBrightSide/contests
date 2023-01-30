from collections import defaultdict
import bisect


def main():
    t = eval(input())
    for _ in range(t):
        n, q = input().split()
        heights = input().split()
        heights = [int(x) for x in heights]
        ques = input().split()
        ques = [int(x) for x in ques]
        solve(heights, ques)


def solve(h, q):
    prefix = [h[0]]
    for i in range(1, len(h)):
        prefix.append(prefix[-1] + h[i])
        h[i] = max(h[i-1], h[i])

    for e in q:
        if h[-1] <= e:
            print(prefix[-1], end=" ")
        elif e < h[0]:
            print(0, end=" ")
        else:
            can_walk = bisect.bisect_right(h, e)
            print(prefix[can_walk - 1], end=" ")
    print()


main()
