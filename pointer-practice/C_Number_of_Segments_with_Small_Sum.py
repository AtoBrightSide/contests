def main():
    n, s = input().split()
    print(solution([int(x) for x in input().split()], eval(s)))

def solution(nums, s):
    L = len(nums)
    if s >= sum(nums):
        return (L * (L + 1)) // 2
    
    count = left = sum_so_far = 0
    for right, num in enumerate(nums):
        sum_so_far += num
        while sum_so_far > s:
            count += right - left
            sum_so_far -= nums[left]
            left += 1

    return count

main()