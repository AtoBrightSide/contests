def main():
    n, s = input().split()
    print(solution([int(x) for x in input().split()], eval(s)))

def solution(nums, s):
    if s > sum(nums):
        return -1
    left = sum_so_far = 0
    length = float("inf")
    for right, num in enumerate(nums):
        sum_so_far += num
        while sum_so_far >= s:
            length = min(length, right - left + 1)
            sum_so_far -= nums[left]
            left += 1
    
    return min(length, len(nums))

main()