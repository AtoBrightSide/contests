from collections import defaultdict

def main():
    for _ in range(eval(input())):
        input()
        print(solution([int(x) for x in input().split()]))

def solution(nums):
    if sorted(nums) == nums:
        return 0
    tracker = defaultdict(int)
    for i, num in enumerate(nums):
        tracker[num].append(i)
    
    return

main()