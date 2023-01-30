from collections import Counter
def main():
    t = eval(input())
    for _ in range(t):
        n = eval(input())
        print(*solution([int(x) for x in input().split()]))

def solution(nums):
    ans = len(nums) - len(set(nums)) - 1
    if ans < 0:
        return [1, 1]
    
    window = set([nums[0]])
    for i in range(1, len(nums)):
        window.add(nums[i])
        if i - len(window) == ans:
            return [1, i + 1]
    
    window = set([nums[-1]])
    for i in range(len(nums) - 2, -1, -1):
        window.add(nums[i])
        if len(nums) - i - len(window) == ans:
            return [i + 1, len(window)]

main()