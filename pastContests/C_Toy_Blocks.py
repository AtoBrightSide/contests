from collections import defaultdict, Counter, deque
from math import inf


def main():
    for _ in range(eval(input())):
        print(solution(eval(input()), [int(x) for x in input().split()]))


def solution(n, nums):
    nums.sort()
    total = sum(nums)
    ans = inf
    for i, num in enumerate(nums):
        use = (-1 if i != n - 1 else -2)
        toBeAdded = ((n - 1) * nums[use]) - (total - num)
        if toBeAdded >= num:
            ans = min(ans, toBeAdded - num)
        else:
            diff = abs(toBeAdded - num) % (n - 1)
            ans = min(ans, diff)

    return ans


main()
