def main():
    t = eval(input())
    for _ in range(t):
        n = input()
        print(*solution([int(x) for x in input().split()]))

def solution(nums):
    firstIndex = nums.index(max(nums))
    second = 0
    ans = []
    for i in range(len(nums)):
        if i != firstIndex:
            second = max(second, nums[i])
    
    # secondIndex = nums.index(second)
    for i in range(len(nums)):
        if i == firstIndex:
            ans.append(nums[i] - second)
        else:
            ans.append(nums[i] - nums[firstIndex])
    
    return ans

main()