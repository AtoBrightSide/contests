def main():
    eval(input())
    print(solution([int(x) for x in input().split()]))

def solution(nums):
    ans = -1
    
    for i, num in enumerate(nums):
        if i > 0 and num >= nums[i - 1]:
            count += 1
            ans = max(ans, count)
        else:
            count = 1
    
    return max(ans, 1)

main()