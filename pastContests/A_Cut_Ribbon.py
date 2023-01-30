import threading
import sys


def main():
    n, a, b, c = input().split()
    print(solution(int(n), [int(a), int(b), int(c)]))


def solution(n, pieces):
    return dp(n, pieces, {})


def dp(n, pieces, memo):
    if n <= 0:
        return 0 if n == 0 else -1
    # if n not in memo:
    best = -float("inf")
    for piece in pieces:
        curr = dp(n - piece, pieces, memo)
        if curr >= 0:
            best = max(best, curr + 1)
        # memo[n] = best
    return best


# main()
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
