from collections import defaultdict


def main():
    n = eval(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    print(solve(nums))


def solve(nums):
    best = 0
    l = 0
    
    for r in range(1, len(nums)):
        if nums[r] < nums[r - 1]:
            l = r
        else:
            best = max(best, r - l)

    return best + 1

main()
