from heapq import *
def main():
    for _ in range(eval(input())):
        eval(input())
        solution([int(num) for num in input().split()])

def solution(nums):
    max_num = len(nums)
    min_num = 1
    l, r = 0, len(nums) - 1
    while l < r and min_num < max_num:
        if nums[l] not in set([max_num, min_num]) and nums[r] not in set([max_num, min_num]):
            print(f"{l + 1} {r + 1}")
            return

        if nums[l] == min_num:
            min_num += 1
            l += 1
        elif nums[l] == max_num:
            max_num -= 1
            l += 1
        if nums[r] == min_num:
            min_num += 1
            r -= 1
        if nums[r] == max_num:
            max_num -= 1
            r -= 1
        

    print("-1")
    
main()