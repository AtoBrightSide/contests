from collections import defaultdict
import bisect


def main():
    print(solve(input()))


def solve(s):
    flag = False
    moves = 0
    lows = ups = 0
    for ch in s:
        if flag and ch.isupper():
            moves += 1
        flag = flag or ch.islower()
        lows += 1 if ch.islower() else 0
        ups += 1 if ch.isupper() else 0
    
    return min(moves, lows, ups, len(s) - moves - 1)


main()
