def main():
    n, s = input().split()
    print(solution([int(x) for x in input().split()], eval(s)))

def solution(nums, s):
    sum_so_far = 0
    left = length = 0
    for right, num in enumerate(nums):
        sum_so_far += num    
        while sum_so_far > s:
            sum_so_far -= nums[left]
            left += 1
        length = max(length, right - left + 1)
    
    return length

main()