from collections import defaultdict
import bisect


def main():
    t = eval(input())
    for _ in range(t):
        l, r, a = input().split()
        print(solve(int(l), int(r), int(a)))


def solve(l, r, a):
    if a == 1:
        return r

    if r < a:
        return (r // a) + (r % a)

    

    return max((r // a) + (r % a), (a - 1) + 5)


main()
