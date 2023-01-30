from collections import defaultdict


def main():
    t = eval(input())
    for _ in range(t):
        print(solve(input(), input()))


def solve(p, h):
    reference = sorted(p)
    r = len(p)
    l = 0
    while r <= len(h):
        if reference == sorted(h[l:r]):
            return "YES"
        r += 1
        l += 1

    return "NO"


main()
