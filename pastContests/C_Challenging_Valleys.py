import math

def main():
    for _ in range(eval(input())):
        n = eval(input())
        nums = [float("inf")] + [int(x) for x in input().split()] + [float("inf")]
        print(solution(nums))


def solution(nums):
    
    L = len(nums)
    if L == 1:
        return "YES"

    valley = False
    
    isValley = lambda i, l, r: nums[l] > nums[i] < nums[r]
    checker = [[-1, -1]] * (L - 2)
    print(checker)
    for i in range(1, L - 1):
        if nums[i - 1] > nums[i]:
            checker[i] = [nums[i - 1], -1]
        if i != 1 and nums[i - 1] == nums[i]:
            checker[i] = checker[i - 1]
    
    for i in range(L - 2, 0, -1):
        if nums[i + 1] > nums[i]:
            checker[i][1] = nums[i + 1]
        if i != L - 2 and nums[i + 1] == nums[i]:
            checker[i][1] = checker[i + 1][1]

    print(checker)

    
    return "NO"


main() 